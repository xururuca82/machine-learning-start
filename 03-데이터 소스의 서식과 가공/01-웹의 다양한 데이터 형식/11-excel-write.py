import openpyxl
# 엑셀 파일 열기
filename = "stat_104102.xlsx"
book = openpyxl.load_workbook(filename)

# 활성화된 시트 추출하기
sheet = book.active

# 서울을 제외한 인구를 구해서 쓰기
for i in range(0, 10):
    total = int(sheet[str(chr(i + 66)) + "4"].value.replace(",", ""))
    seoul = int(sheet[str(chr(i + 66)) + "5"].value.replace(",", ""))
    output = total - seoul
    print("서울 제외 인구 = ", output)
    # 쓰기
    sheet[str(chr(i + 66)) + "24"] = output
    cell = sheet[str(chr(i + 66)) + "24"]
    # 폰트와 색상 변경하기
    cell.font = openpyxl.styles.Font(size=14, color="FF0000")
    cell.number_format = cell.number_format

# 엑셀 파일 저장하기
filename = "population.xlsx"
book.save(filename)
print("ok")
