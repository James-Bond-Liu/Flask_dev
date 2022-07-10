def connect_to_database():
    pass

class DB():
    def __init__(self):
        self.conn = connect_to_database()

    def query(self, sql):
        self.conn.execute(sql)

    def close(self):
        self.close()

class Project(DB):
    table = 'project_info'

    def list_all(self):
        self.query(f'SELECT * FROM {Project.table}')
        res = self.conn.fetchall()
        return res

    def get_by_id(self, id):
        self.query(f'SELECT * FROM {Project.table} WHERE id={id}')
        res = self.conn.fetone()
        return res

"""
然后在视图函数中直接调用Project中的不同方法即可
"""