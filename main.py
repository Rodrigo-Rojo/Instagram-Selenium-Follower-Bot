from selenium import webdriver
import time
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

PASSWORD = "Password"
chrome_driver = "D:\Development\chromedriver.exe"
FACEBOOK_LOGIN = "LoginID"
driver = webdriver.Chrome(executable_path=chrome_driver)
driver.get("https://www.instagram.com/")
time.sleep(2)
driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[5]/button').click()
time.sleep(2)
driver.find_element_by_name("email").send_keys(FACEBOOK_LOGIN + Keys.TAB + PASSWORD + Keys.ENTER)
time.sleep(10)
driver.get("https://www.instagram.com/soymaletas/")
time.sleep(5)

# try:
#     driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/div[2]/div/div/div/span/span[1]/button').click()
# except NoSuchElementException:
#     driver.find_element_by_xpath(
#         '//*[@id="react-root"]/section/main/div/header/section/div[2]/div/div/div/span/span[1]').click()

try:
    driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a').click()
except NoSuchElementException:
    driver.find_element_by_xpath('//*[@id="react-root"]/div/div/section/main/div/header/section/ul/li[2]/a').click()

pop_up_window = WebDriverWait(
    driver, 2).until(EC.element_to_be_clickable(
    (By.XPATH, "//div[@class='isgrP']")))
time_off = time.time() + 30
# Scroll till Followers list is there
while time.time() < time_off:
    driver.execute_script(
        'arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;',
        pop_up_window)
    time.sleep(1)
time.sleep(5)
follow_buttons = driver.find_elements_by_css_selector(".PZuss button")
print(follow_buttons)
for button in follow_buttons:
    button.click()
    time.sleep(3)
