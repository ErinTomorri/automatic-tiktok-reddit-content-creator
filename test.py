from lib2to3.pgen2 import driver


def scraper():
    comments = driver.find_elements_by_css_selector('div[id^=t1_][tabindex]')