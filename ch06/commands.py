import sys
from datetime import datetime

from database import DatabaseManager

db = DatabaseManager('bookmarks.db')  # <1>


class CreateBookmarksTableCommand:
    def execute(self):  # <2>
        db.create_table('bookmarks', {  # <3>
            'id': 'integer primary key autoincrement',
            'title': 'text not null',
            'url': 'text not null',
            'notes': 'text',
            'date_added': 'text not null',
        })


class AddBookmarkCommand:
    def execute(self, data):
        data['date_added'] = datetime.utcnow().isoformat()  # <1>
        db.add('bookmarks', data)  # <2>
        return 'Bookmark added!'  # <3>


class ListBookmarksCommand:
    def __init__(self, order_by='date_added'):  # <1>
        self.order_by = order_by

    def execute(self):
        return db.select('bookmarks', order_by=self.order_by).fetchall()  # <2>


class DeleteBookmarkCommand:
    def execute(self, data):
        db.delete('bookmarks', {'id': data})  # <1>
        return 'Bookmark deleted!'


class QuitCommand:
    def execute(self):
        sys.exit()  # <1>
