from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 

def get_user_info(povis_id, povis_pw):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument("--single-process")
    chrome_options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    driver.get('https://pams.postech.ac.kr/postech/client/index.do')

    driver.find_element("name", "userId").send_keys(povis_id)
    driver.find_element("name", "userPw").send_keys(povis_pw)

    driver.find_element("id", "loginBtn").click()
    driver.get('https://pams.postech.ac.kr:443/postech/clientPortfolio/r/m/selectPortfolioList.do')


    #기본정보 불러오기
    basicInfo_list = []
    table = driver.find_element("xpath", '//*[@id="movebox1"]/div/table')
    tbody = table.find_element("tag name", "tbody")
    trs = tbody.find_elements("tag name", "tr")

    for tr in trs:
        tds = tr.find_elements("tag name", "td")
        for td in tds:
            basicInfo_list.append(td.text)  


    #이력서 불러오기
    resume_list = []

    table = driver.find_element("xpath", '//*[@id="movebox2"]/div/table')
    tbody = table.find_element("tag name", "tbody")
    trs = tbody.find_elements("tag name", "tr")

    for tr in trs:
        tds = tr.find_elements("tag name", "td")
        for td in tds:
            resume_list.append(td.text)


    #교내활동 불러오기
    schoolAct_list = []

    #div = driver.find_element("id", "mCSB_4_container")
    #table = div.find_element("tag name", "table")
    #tbody = table.find_element("tag name", "tbody")
    #trs = tbody.find_elements("tag name", "tr")

    #for tr in trs:
     #   tds = tr.find_elements("tag name", "td")
      #  for td in tds:
       #     schoolAct_list.append(td.text)


    #학생단체활동 불러오기
    clubAct_list = []

    #div = driver.find_element("id", "mCSB_3_container")
    #table = div.find_element("tag name", "table")
    #tbody = table.find_element("tag name", "tbody")
    #trs = tbody.find_elements("tag name", "tr")

    #for tr in trs:
     #  tds = tr.find_elements("tag name", "td")
      #  for td in tds:
      #      clubAct_list.append(td.text)


    #봉사활동 불러오기
    volunteer_list = []

    #div = driver.find_element("id", "mCSB_1_container")
    #table = div.find_element("tag name", "table")
    #tbody = table.find_element("tag name", "tbody")
    #trs = tbody.find_elements("tag name", "tr")

    #for tr in trs:
     #   tds = tr.find_elements("tag name", "td")
      #  for td in tds:
       #     volunteer_list.append(td.text)


    #대외활동 불러오기
    extraAct_list = []

    #div = driver.find_element("id", "mCSB_2_container")
   # table = div.find_element("tag name", "table")
   # tbody = table.find_element("tag name", "tbody")
   # trs = tbody.find_elements("tag name", "tr")

   # for tr in trs:
    #    tds = tr.find_elements("tag name", "td")
     #   for td in tds:
      #      extraAct_list.append(td.text)

            
    driver.close()

    return basicInfo_list, resume_list, schoolAct_list, clubAct_list, volunteer_list, extraAct_list
