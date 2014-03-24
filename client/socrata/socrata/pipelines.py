import sqlite3

class SocrataPipeline(object):
    def __init__(self):
        self.conn = sqlite3.connect('project.db')
        self.cur = self.conn.cursor()

    def process_item(self, item, spider):
        self.cur.execute("insert into data (text, url, views) values(?,?,?)", (item['text'][0], item['url'][0], item['views'][0]))
        self.conn.commit()
        return item
