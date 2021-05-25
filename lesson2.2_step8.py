from selenium import webdriver
import time
import os

value1 = "Ivan"
value2 = "Ivanov"
value3 = "Ivan_Ivanov@gmail.com"

try: 
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_xpath("//div/input[1]")
    input1.send_keys(value1) 
    input2 = browser.find_element_by_xpath("//div/input[2]")
    input2.send_keys(value2)
    input3 = browser.find_element_by_xpath("//div/input[3]")
    input3.send_keys(value3)

    file_button = browser.find_element_by_css_selector("#file")
    

    current_dir = os.path.abspath(os.path.dirname(__file__)) 
    file_path = os.path.join(current_dir, 'file.txt')
    file_button.send_keys(file_path)

    button = browser.find_element_by_tag_name("button")
    button.click()
    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()