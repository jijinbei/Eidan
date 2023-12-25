from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from time import sleep
from lib import MyDriver

def drag_word(driver: MyDriver):
    answers = []
    for i in range(1, 11):
        answer_element = driver.find_element(by=By.XPATH, value=driver.review_Xpath('/html/body/div[2]/div/div/div/div[',3,f']/div[2]/div[2]/div[{i}]'))
        answer_meaning = answer_element.get_attribute("meaning")
        answers.append({"element": answer_element, "meaning": answer_meaning})

    words = []
    for i in range(1, 11):
        word_element = driver.find_element(by=By.XPATH, value=driver.review_Xpath('/html/body/div[2]/div/div/div/div[',3,f']/div[2]/div[3]/div[{i}]/span'))
        word_meaning = word_element.get_attribute("meaning")
        words.append({"element": word_element, "meaning": word_meaning})

    # meaningがおなじものを探す
    sorted_words = []
    for answer in answers:
        for word in words:
            if answer["meaning"] == word["meaning"]:
                sorted_words.append(word)
                break

    # drag and drop
    action = ActionChains(driver)
    for answer, sorted_word in zip(answers, sorted_words):
        action.drag_and_drop(sorted_word["element"], answer["element"])
    action.perform()

def click_word(driver:MyDriver, num):
    if num == 16:
        X = 4
    else:
        X = 3
    
    if driver.is_review == True:
        X += 1

    button = []
    
    for width in range(1,5):
        for height in range(1, 6):
            element = driver.find_element(by=By.XPATH, value=f"/html/body/div[2]/div/div/div/div[{X}]/div[3]/div[{width}]/ul/li[{height}]")
            word = element.get_attribute("word_name")
            button.append({"element": element, "word": word})
    
    for problem_num in range(20):
        word = driver.find_element(by=By.XPATH, value=f"/html/body/div[2]/div/div/div/div[{X}]/div[2]/h2").text
        for num in range(20):
            if word == button[num]["word"]:
                button[num]["element"].click()
                driver.implicitly_wait(0.5)
                break
    
    sleep(0.5)