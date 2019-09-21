import sqlite3


class DatabaseManager:
    def __init__(self, database_filename):
        self.connection = sqlite3.connect(database_filename)  # <1>

    def __del__(self):
        self.connection.close()  # <2>

    def _execute(self, statement, values=None):  # <1>
        with self.connection:
            cursor = self.connection.cursor()
            cursor.execute(statement, values or [])  # <2>
            return cursor

    def create_table(self, table_name, columns):
        columns_with_types = [  # <1>
            f'{column_name} {data_type}'
            for column_name, data_type in columns.items()
        ]
        self._execute(  # <2>
            f'''
            CREATE TABLE IF NOT EXISTS {table_name}
            ({', '.join(columns_with_types)});
            '''
        )

    def drop_table(self, table_name):
        self._execute(f'DROP TABLE {table_name};')

    def add(self, table_name, data):
        placeholders = ', '.join('?' * len(data))
        column_names = ', '.join(data.keys())  # <1>
        column_values = tuple(data.values())  # <2>

        self._execute(
            f'''
            INSERT INTO {table_name}
            ({column_names})
            VALUES ({placeholders});
            ''',
            column_values,  # <3>
        )

    def delete(self, table_name, criteria):  # <1>
        placeholders = [f'{column} = ?' for column in criteria.keys()]
        delete_criteria = ' AND '.join(placeholders)
        self._execute(
            f'''
            DELETE FROM {table_name}
            WHERE {delete_criteria};
            ''',
            tuple(criteria.values()),  # <2>
        )

    def select(self, table_name, criteria=None, order_by=None):
        criteria = criteria or {}  # <1>

        query = f'SELECT * FROM {table_name}'

        if criteria:  # <2>
            placeholders = [f'{column} = ?' for column in criteria.keys()]
            select_criteria = ' AND '.join(placeholders)
            query += f' WHERE {select_criteria}'

        if order_by:  # <3>
            query += f' ORDER BY {order_by}'

        return self._execute(  # <4>
            query,
            tuple(criteria.values()),
        )
