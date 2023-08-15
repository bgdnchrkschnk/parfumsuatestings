from enum import Enum
from locators.base_locators import BaseLocators

class BasePageLocators(Enum):
    GENERAL_MENU_TOPIC = '.menu-list__item>a[href$={data_category}]'