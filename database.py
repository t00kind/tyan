import sqlite3 as sq

db = sq.connect('tg.db')
cur = db.cursor()


cur.execute("CREATE TABLE IF NOT EXISTS content(name TEXT, desc TEXT, photo TEXT, author TEXT, code INTEGER PRIMARY KEY) ")
db.commit()
async def add_all(data):
        cur.execute("INSERT INTO content (name, desc, photo, author, code) VALUES (?, ?, ?, ?, ?)", (data['name'], data['desc'], data['photo'], data['author'], data['code']))
        db.commit()



async def find_by_id(id):
    g = cur.execute(f"SELECT * FROM content WHERE code == {id}")
    az = g.fetchall()[0]
    res = {
    'name': az[0],
    'desc': az[1],
    'photo': az[2],
    'author': az[3],
    "code": az[4]
    }
    return res
def get_all():
    g = cur.execute(f"SELECT * FROM content")
    return g.fetchall()
    