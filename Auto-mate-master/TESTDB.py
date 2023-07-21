import sqlite3

con=sqlite3.connect('automate.db')
cursor=con.cursor()

rows = cursor.execute('Select * from current_user')
#rows = cursor.execute('describe current_user')
for row in rows:
    print(row)
#con.commit()
con.close()