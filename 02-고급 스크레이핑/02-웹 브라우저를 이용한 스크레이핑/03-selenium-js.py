from selenium import webdriver

# PhantomJS 드라이버 추출하기
browser = webdriver.Chrome(executable_path=r"C:\chromedriver\chromedriver.exe")
browser.implicitly_wait(3)

# 적당한 웹페이지 열기
browser.get("https://google.com")

# 자바스크립트 실행하기
r = browser.execute_script("return 100 + 50")
print(r) 