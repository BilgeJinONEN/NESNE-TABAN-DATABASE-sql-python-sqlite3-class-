import pandas as pd
import sqlite3

class Database:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.c = self.conn.cursor()

    def create_table(self, table_name, *columns):
        columns = str(columns)
        columns = columns.replace("'", "")
        columns = columns.replace('"', "")
        sql = f"CREATE TABLE IF NOT EXISTS {table_name}{columns}"
        self.c.execute(sql)
        self.conn.commit()

    def insert_data(self, table_name, *values):
        placeholder = ",".join(len(values) * ["?"])
        sql = f"INSERT INTO {table_name} VALUES({placeholder})"
        self.c.execute(sql, values)
        self.conn.commit()

    def fetch_data(self, table_name, condition=None):
        sql = f"SELECT * FROM {table_name}"
        if condition:
            sql += f' WHERE {condition}'
        self.c.execute(sql)
        return self.c.fetchall()

    def update_data(self, table_name, set_condition, condition):
        sql = f"UPDATE {table_name} SET {set_condition} WHERE {condition}"
        self.c.execute(sql)
        self.conn.commit()

    def delete_data(self, table_name, condition):
        sql = f"DELETE FROM {table_name} WHERE {condition}"
        self.c.execute(sql)
        self.conn.commit()

    def export_to_excel(self, table_name, file_name):
        self.c.execute(f"SELECT * FROM {table_name}")
        rows = self.c.fetchall()
        column_names = [description[0] for description in self.c.description]
        df = pd.DataFrame(rows, columns=column_names)
        df.to_excel(f"{file_name}.xlsx", index=False)
        print(f"Data has been exported to {file_name}.xlsx")

    def exists(self, table_name, condition):
        sql = f"SELECT * FROM {table_name} WHERE {condition}"
        self.c.execute(sql)
        data = self.c.fetchall()
        if data:
            return True
        else:
            return False
