import sqlite3

conn = sqlite3.connect('school_vans.db')

cur = conn.cursor()

cur.execute('''
    CREATE TABLE IF NOT EXISTS vans (
        id INTEGER PRIMARY KEY,
        name TEXT,
        latitude REAL,
        longitude REAL
    )
''')

def insert_van(name, lat, lon):
    conn = sqlite3.connect('school_vans.db')
    cur = conn.cursor()
    cur.execute('SELECT name FROM vans WHERE name=?',(name,))
    if cur.fetchone() == None:
        cur.execute('INSERT INTO vans (name,latitude, longitude) VALUES (?,?,?)',(name,lat,lon))
        conn.commit()
        cur.close()

def delete_van(name):
    conn = sqlite3.connect('school_vans.db')
    cur = conn.cursor()
    cur.execute('DELETE FROM vans WHERE name=(?)',(name,))
    conn.commit()
    cur.close()
def update_van(name, lat, lon):
    conn = sqlite3.connect('school_vans.db')
    cur = conn.cursor()
    cur.execute('UPDATE vans SET latitude=?, longitude=? WHERE name=?',(lat,lon,name))
    conn.commit()
    cur.close()
def display():
    conn = sqlite3.connect('school_vans.db')
    cur = conn.cursor()
    cur.execute('SELECT * FROM vans')
    for i in cur.fetchall():
        print(i)
    cur.close()
def get_van(name):
    conn = sqlite3.connect('school_vans.db')
    cur = conn.cursor()
    cur.execute('SELECT name, latitude, longitude FROM vans WHERE name=?',(name,))
    result = cur.fetchall()
    print(result)
    cur.close()
if __name__ == '__main__':
    insert_van("iniyan",23434,34543456)
    insert_van("sakthi",23434,34543456)
    insert_van("vikram",23434,34543456)
    display()
    print("----------------------------")
    delete_van("iniyan")
    display()
    print("----------------------------")
    update_van('sakthi', 123,321)
    display()
    print("----------------------------")
    get_van('sakthi')

