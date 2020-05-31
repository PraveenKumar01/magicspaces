import psycopg2

con = psycopg2.connect(host="localhost",
                       database="users",
                       user="postgres",
                       password="Newyear#123",)

# Cursor
cur = con.cursor()

cur.execute("select * from public.users")

rows = cur.fetchall()

fusername = 'praveenkumarm'

# for r in rows:
#     print(f"username {r[0]} password {r[1]}")

cur.execute("select * from users where username=username",'test')

row =cur.fetchall()

print(row)

# img =str(row[]).split(';')

# print(img[0])
# print(str(row[0]).split(';'))

    # db_user = print(f"username {row[0]}")



