import sqlite3
con=sqlite3.connect('db.sqlite3')
work=()
for i in con.execute('SELECT name FROM sqlite_master WHERE type="table";'):
    print(i[0],con.execute(f'pragma table_info({i[0]})').fetchall())
for i in con.execute('select * from auth_user;'):print(i)
#con.execute('delete from auth_user;')
con.commit()
for i in con.execute('select * from auth_user;'):print(i)