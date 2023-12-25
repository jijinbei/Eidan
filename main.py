from selenium.webdriver.common.by import By
from selenium.webdriver.chrome import service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from solve import drag_word, click_word
from lib import MyDriver, set_problem
import dotenv
import os

dotenv.load_dotenv()
username = os.getenv("LOG_IN_ID")
password = os.getenv("PASSWORD")

problem_xpath = set_problem()

# Chromeの起動オプションを設定
opt = Options()
opt.add_argument('--start-maximized')  # 起動時にウィンドウを最大化する
opt.add_experimental_option("detach", True)
# chrome_serv = service.Service(ChromeDriverManager().install())
driver = MyDriver(opt=opt)
driver.get("https://hirotan.jp/")
title = driver.title
driver.implicitly_wait(0.5)

#idとパスワードを入力
log_id_element = driver.find_element(by=By.XPATH, value="/html/body/div[2]/div/div/div/div/div[3]/div[2]/form/div[1]/div[2]/input")
submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")
log_pass_element = driver.find_element(by=By.XPATH, value="/html/body/div[2]/div/div/div/div/div[3]/div[2]/form/div[2]/div[2]/input")
submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")
log_id_element.send_keys(username)
log_pass_element.send_keys(password)
sleep(0.2)
driver.click_button('/html/body/div[2]/div/div/div/div/div[3]/div[2]/form/div[4]/input')
driver.implicitly_wait(10)
sleep(1)
driver.click_button(problem_xpath)

# 復習か予習かの判定
driver.review_or_not()

current_num = driver.question_number()

for num in range(current_num,17):
    # 問題を解く
    if num <= 10:
        driver.review_button('/html/body/div[2]/div/div/div/div[',3,']/div/p[2]/button')
        driver.review_button('/html/body/div[2]/div/div/div/div[',4,']/div[2]/div[3]/button[4]')
        driver.review_button('/html/body/div[2]/div/div/div/div[',2,']/div/p[2]/button')    
        drag_word(driver)
        driver.review_button('/html/body/div[2]/div/div/div/div[',3,']/div[2]/div[4]/div[1]/div/button')
        driver.review_button('/html/body/div[2]/div/div/div/div[',3,']/div[2]/div[4]/div[3]/div/button[1]')
    elif num <= 15:
        driver.review_button('/html/body/div[2]/div/div/div/div[',3,']/div/p[2]/button')
        driver.review_button('/html/body/div[2]/div/div/div/div[',4,']/div[2]/div[3]/button[4]')
        driver.click_button('/html/body/div[2]/div/div/div/div[2]/div/p[2]/button')        
        click_word(driver, num)
        driver.review_button('/html/body/div[2]/div/div/div/div[',3,']/div[2]/div[2]/div/button[1]')
    else:
        driver.click_button('/html/body/div[2]/div/div/div/div[2]/div/p[3]/button')
        driver.click_button('/html/body/div[2]/div/div/div/div[3]/div/p[3]/button')
        click_word(driver, 16)

driver.review_button('/html/body/div[2]/div/div/div/div[',4,']/div[2]/div[2]/div/button')
sleep(0.5)
driver.click_button('/html/body/div[2]/div/div/div/div[2]/div/button')
sleep(2)

print("終了しました")

driver.close()