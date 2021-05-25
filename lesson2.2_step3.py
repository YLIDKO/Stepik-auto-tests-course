from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time


try: 
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    num1 = browser.find_element_by_id("num1")
    num2 = browser.find_element_by_id("num2")
    x=num1.text
    y=num2.text

    sum = int(x) + int(y)


    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(str(sum))


    button = browser.find_element_by_css_selector("button")
    button.click()
    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()