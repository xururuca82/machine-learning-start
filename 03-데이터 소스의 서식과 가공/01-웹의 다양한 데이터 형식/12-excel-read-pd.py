import pandas as pd

# 엑셀 파일 열기
filename = "stat_104102.xlsx"
sheet_name = "Sheet0"
book = pd.read_excel(filename, sheet_name=sheet_name, header=2) # 첫 번째 줄부터 헤더

print(book)
# 2017년 인구로 정렬
book = book.sort_values(by="2017", ascending=False)
print(book)