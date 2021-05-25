from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)


    price= WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, 'price'), "$100"))
    book_button = browser.find_element_by_css_selector("#book")
    book_button.click()
    
    
    
    
    x = browser.find_element_by_id("input_value")
    value = calc(int(x.text))

    answer = browser.find_element_by_css_selector("#answer")
    answer.send_keys(value)
        
    submit_button = browser.find_element_by_css_selector("#solve")
    submit_button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()