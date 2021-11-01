from selenium import webdriver
import chromedriver_autoinstaller
import time


def classname(class_name):
    try:
        driver.find_element_by_class_name("{0}".format(class_name))
        return True
    except:
        return False


chrome_ver = chromedriver_autoinstaller.get_chrome_version().split('.')[0]

try:
    driver = webdriver.Chrome(f'./{chrome_ver}/chromedriver.exe')
except:
    chromedriver_autoinstaller.install(True)
    driver = webdriver.Chrome(f'./{chrome_ver}/chromedriver.exe')

driver.implicitly_wait(10)

driver.maximize_window()

driver.get("https://hcs.eduro.go.kr/#/relogin")
time.sleep(2)

driver.find_element_by_id("btnConfirm2").click()
driver.find_element_by_class_name("searchBtn").click()
driver.find_element_by_id("sidolabel").click()
driver.find_element_by_xpath("/html/body/div/div/div/div/div/div[2]/div[1]"
                             "/table/tbody/tr[1]/td/select/option[6]").click()
driver.find_element_by_id("crseScCode").click()
driver.find_element_by_xpath("/html/body/div/div/div/div/div/div[2]/div[1]"
                             "/table/tbody/tr[2]/td/select/option[5]").click()
school = driver.find_element_by_id("orgname")
school.send_keys("학교")
driver.find_element_by_class_name("searchBtn").click()
time.sleep(0.1)
driver.find_element_by_xpath("/html/body/div/div/div/div/div/div[2]/div[1]/ul/li/a").click()
time.sleep(0.001)
driver.find_element_by_class_name("layerFullBtn").click()
name = driver.find_element_by_xpath("/html/body/app-root/div/div[1]/div[2]/div/div[2]/div/div[1]/table/tbody/tr["
                                    "2]/td/input")
name.send_keys("이름")
time.sleep(0.1)
bir = driver.find_element_by_id("birthday_input")
bir.send_keys("생년월일")
driver.find_element_by_id("btnConfirm").click()
time.sleep(0.5)
driver.find_element_by_xpath('//*[@id="password"]').click()
PASSWORD = '비밀번호'
for i in PASSWORD:
    driver.execute_script("arguments[0].click();", driver.find_element_by_xpath(f"//*[@aria-label='{i}']"))

time.sleep(1.5)
driver.find_element_by_id("btnConfirm").click()
time.sleep(0.7)
driver.find_element_by_xpath('/html/body/app-root/div/div[1]/div[2]/div/section[2]/div[2]/ul/li/a/em').click()
time.sleep(0.7)
driver.find_element_by_xpath('/html/body/app-root/div/div[1]/div[2]/div/div[2]/div[2]'
                             '/div[2]/dl[1]/dd/ul/li[1]/input').click()
driver.find_element_by_xpath('/html/body/app-root/div/div[1]/div[2]/div/div[2]/div[2]'
                             '/div[2]/dl[2]/dd/ul/li[1]/input').click()
driver.find_element_by_xpath('/html/body/app-root/div/div[1]/div[2]/div/div[2]/div[2]'
                             '/div[2]/dl[3]/dd/ul/li[1]/input').click()
driver.find_element_by_xpath('/html/body/app-root/div/div[1]/div[2]/div/div[2]/div[2]/input').click()
