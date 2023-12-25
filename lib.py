from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from time import sleep

class MyDriver(Chrome):
    def __init__(self, opt):
        super().__init__(options=opt)
    
    def review_Xpath(self, path1, num, path2):
        if self.is_review == True:
            Xpath = path1 + str(num + 1) + path2
        elif self.is_review == False:
            Xpath = path1 + str(num) + path2
        else:
            print("復習モードかどうか判定されていません")
        return Xpath
    

    def click_button(self, Xpath): #ボタンのクリック
        button = self.find_element(by=By.XPATH, value = Xpath)
        self.implicitly_wait(2)
        button.click()
        sleep(0.5)
    
    def review_button(self, path1, num, path2):
        Xpath = self.review_Xpath(path1, num, path2)
        self.click_button(Xpath)
    

    def review_or_not(self):
        message = self.find_element(by= By.XPATH, value='/html/body/div[2]/div/div/div/div[3]').text
        self.implicitly_wait(2)
        if message == "復習モードです。解答しても成績には反映されません。":
            self.is_review = True
        else:
            self.is_review = False
    
    def question_number(self):
        Xpath = self.review_Xpath('/html/body/div[2]/div/div/div/div[',3,']/div/div/div[2]/h3/span')
        return int(self.find_element(by = By.XPATH, value= Xpath).text)


# 問題の種類と番号を入力
def set_problem():
    while True:
        problem = input("a or b: ")
        number = int(input("何番ですか？: "))

        if problem == 'a':
            number = number % 20
            return f'/html/body/div[2]/div/div[3]/div[4]/div/div[2]/div[2]/div[2]/div[{number}]/button'
        elif problem == 'b':
            number = number % 10
            return f'/html/body/div[2]/div/div[3]/div[4]/div/div[2]/div[3]/div[2]/div[{number}]/button'
        else:
            print("a, bを入力してください")
