import sys
from abc import ABC, abstractmethod
from datetime import datetime

import requests

from persistence import BookmarkDatabase  # <1>

persistence = BookmarkDatabase()  # <2>


class Command(ABC):
    @abstractmethod
    def execute(self, data):
        raise NotImplementedError('Commands must implement an execute method')


class AddBookmarkCommand(Command):
    def execute(self, data, timestamp=None):
        data['date_added'] = timestamp or datetime.utcnow().isoformat()
        persistence.create(data)  # <3>
        return True, None


class ListBookmarksCommand(Command):
    def __init__(self, order_by='date_added'):
        self.order_by = order_by

    def execute(self, data=None):
        return True, persistence.list(order_by=self.order_by)  # <4>


class DeleteBookmarkCommand(Command):
    def execute(self, data):
        persistence.delete(data)  # <5>
        return True, None


class QuitCommand(Command):
    def execute(self, data=None):
        sys.exit()


class ImportGitHubStarsCommand(Command):
    def _extract_bookmark_info(self, repo):
        return {
            'title': repo['name'],
            'url': repo['html_url'],
            'notes': repo['description'],
        }

    def execute(self, data):
        bookmarks_imported = 0

        github_username = data['github_username']
        next_page_of_results = f'https://api.github.com/users/{github_username}/starred'

        while next_page_of_results:
            stars_response = requests.get(
                next_page_of_results,
                headers={'Accept': 'application/vnd.github.v3.star+json'},
            )
            next_page_of_results = stars_response.links.get('next', {}).get('url')

            for repo_info in stars_response.json():
                repo = repo_info['repo']

                if data['preserve_timestamps']:
                    timestamp = datetime.strptime(
                        repo_info['starred_at'],
                        '%Y-%m-%dT%H:%M:%SZ'
                    )
                else:
                    timestamp = None

                bookmarks_imported += 1
                AddBookmarkCommand().execute(
                    self._extract_bookmark_info(repo),
                    timestamp=timestamp,
                )

        return True, bookmarks_imported


class EditBookmarkCommand(Command):
    def execute(self, data):
        persistence.edit(data['id'], data['update'])  # <6>
        return True, None
