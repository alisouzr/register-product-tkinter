import sqlite3 as lite

con = lite.connect('dados.db')

def insert_data(data):
    with con:
        cur = con.cursor()
        query = "INSERT INTO inventario(name, description, value, available) VALUES(?,?,?,?)"
        cur.execute(query, data)

def update_data(data):
    with con:
        cur = con.cursor()
        query = "UPDATE inventario SET name=?, description=?, value=?, available=? WHERE id =?"
        cur.execute(query, data)

def delete_data(id):
    with con:
        cur = con.cursor()
        query = "DELETE FROM inventario WHERE id=?"
        cur.execute(query, id)


def view_data():
    view = []
    with con:
        cur= con.cursor()
        query = "SELECT * FROM inventario"
        cur.execute(query)

        rows = cur.fetchall()
        for row in rows:
            view.append(row)
    return view