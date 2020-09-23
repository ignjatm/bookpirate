from selenium import webdriver
import time


book = input("URL OF ARCHIVE BOOK: ")
login = "https://archive.org/account/login"
email = # ACCOUNT EMAIL
passw = # ACCOUNT PASSWORD


driver = webdriver.Firefox()
driver.implicitly_wait(20)

driver.get(login)

email_form = driver.find_element_by_class_name("input-email")
password_form = driver.find_element_by_class_name("input-password")
login_button = driver.find_element_by_class_name("input-submit")


email_form.send_keys(email)
password_form.send_keys(passw)
login_button.click()

time.sleep(3)

driver.get(book)
borrow_button = driver.find_element_by_class_name("btn-primary")
driver.fullscreen_window()
borrow_button.click()
time.sleep(10)
fullscreen = driver.find_element_by_class_name("full")
fullscreen.click()

"""
pages_element = driver.find_element_by_class_name("BRcurrentpage")
pages = pages_element.text

current_page = int(pages.split("/")[0].strip())
total_page = int(pages.split("/")[1].strip())
"""


def screenshotpages(driver):
        
    pages_element = driver.find_element_by_class_name("BRcurrentpage")
    pages = pages_element.text

    current_page = int(pages.split("/")[0].strip())
    total_page = int(pages.split("/")[1].strip())

    next_page = driver.find_element_by_class_name("book_flip_next")
    prev_page = driver.find_elements_by_class_name("icon_left_arrow")
    while current_page > 1:
        prev_page.click()
        current_page = current_page - 1


    while current_page < total_page:
        time.sleep(5)
        driver.save_screenshot(str(current_page) + ".png")
        next_page.click()
        current_page = current_page + 1
screenshotpages(driver)
