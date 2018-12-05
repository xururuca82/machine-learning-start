import sqlite3

# 데이터베이스 연결하기
filepath = "test2.sqlite"
conn = sqlite3.connect(filepath)

# 테이블 생성하기
cur = conn.cursor()
cur.execute("drop table if exists items")
cur.execute("""create table items (
    item_id integer primary key,
    name text,
    price integer)""")
conn.commit()

# 데이터 넣기
cur = conn.cursor()
cur.execute("insert into items (name,price) values (?,?)", ("Orange", 5200))
conn.commit()

# 여러 데이터 연속으로 넣기
cur = conn.cursor()
data = [("Mango", 7700), ("Kiwi", 4000), ("Grape", 8000), ("Peach", 9400), ("Persimmon", 7000), ("Banana", 4000)]
cur.executemany("insert into items(name,price) values(?,?)", data)
conn.commit()

# 4000~7000원 사이의 데이터 추출하기
cur = conn.cursor()
price_range = (4000, 7000)
cur.execute("select * from items where price>=? and price<=?", price_range)
fr_list = cur.fetchall()
for fr in fr_list:
    print(fr)
