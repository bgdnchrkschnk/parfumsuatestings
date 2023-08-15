from selenium.webdriver import Chrome, ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from locators.base_page import BasePageLocators

class BasePage:
    def __init__(self, webdriver:Chrome):
        self.__webdriver: Chrome = webdriver
        self.__actions = ActionChains(self.__webdriver)
        self.__wait = WebDriverWait(self.__webdriver, 20)


    def __get_menu_topic(self, data_category):
        return self.__wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, str(BasePageLocators.GENERAL_MENU_TOPIC).format(data_category))))


    @property
    def parfums_menu(self):
        # return self.__wait.until(EC.element_to_be_clickable(By.C))
