import sqlite3

# sqlite 데이터베이스 연결하기
dbpath = "test.sqlite"
conn = sqlite3.connect(dbpath)

# 테이블을 생성하고 데이터 넣기
cur = conn.cursor()
cur.executescript("""
/* item 테이블이 이미 있다면 제거하기 */
drop table if exists items;

/* 테이블 생성하기 */
create table items(
    item_id integer primary key,
    name text unique,
    price integer
);

/* 데이터 넣기 */
insert into items(name, price)values('Apple', 800);
insert into items(name, price)values('Orange', 780);
insert into items(name, price)values('Banana', 430);
""")

# 위의 조작을 데이터베이스에 반영하기
conn.commit()

# 데이터 추출하기
cur = conn.cursor()
cur.execute("select item_id,name,price from items")
item_list = cur.fetchall()

# 출력하기
for it in item_list:
    print(it)