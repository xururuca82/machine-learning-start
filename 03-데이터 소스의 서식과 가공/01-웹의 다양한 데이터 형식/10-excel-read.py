import openpyxl

# 엑셀 파일 열기
filename = "stat_104102.xlsx"
book = openpyxl.load_workbook(filename)

# 맨 앞의 시트 추출하기
sheet = book.worksheets[0]

# 시트의 각 행을 순서대로 추출하기
data = []
for row in sheet.rows:
    data.append([
        row[0].value,
        row[10].value,
    ])

# 필요없는 줄(헤더, 단위, 연도, 계, 출처, 주석) 제거하기
del data[0:4]
del data[-2:]

# 정렬을 위해 인구수를 문자열에서 숫자로 변경
for d in data:
    d[1] = int(d[1].replace(",", ""))

# 데이터를 인구 순서로 정렬합니다.
data = sorted(data, key=lambda x: x[1])

# 하위 5위를 출력합니다.
for i, a in enumerate(data):
    if i >= 5:
        break
    print(i+1, a[0], a[1])
