import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options,)
driver.maximize_window()
driver.get("https://www.makemytrip.com/railways/")

iframe = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, 'webklipper-publisher-widget-container-notification-frame'))
)

driver.switch_to.frame(iframe)

close_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, 'webklipper-publisher-widget-container-notification-close-div'))
)
close_button.click()

driver.switch_to.default_content()


from_city = driver.find_element(By.XPATH, '//*[@id="top-banner"]/div[2]/div/div/div/div[2]/div/div[1]/label')
from_city.click()
time.sleep(2)

from_city_input = driver.find_element(By.XPATH, '//*[@id="top-banner"]/div[2]/div/div/div/div[2]/div/div[1]/div[1]/div/div/div/input')
from_city_input.send_keys("Delhi")
time.sleep(1)

select_from_city = driver.find_element(By.XPATH, '//*[@id="react-autowhatever-1-section-0-item-0"]')
select_from_city.click()
time.sleep(1)

to_city_input = driver.find_element(By.XPATH, '//*[@id="top-banner"]/div[2]/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/input')
to_city_input.send_keys("Lucknow")
time.sleep(1)

select_to_city = driver.find_element(By.XPATH, '//*[@id="react-autowhatever-1-section-0-item-0"]')
select_to_city.click()
time.sleep(1)

calendar_strafe_button = driver.find_element(By.XPATH, '//*[@id="top-banner"]/div[2]/div/div/div/div[2]/div/div[3]/div[1]/div/div/div/div[2]/div/div[1]/span[2]')
calendar_strafe_button.click()
calendar_strafe_button.click()
calendar_strafe_button.click()
time.sleep(2)

select_20_may = driver.find_element(By.XPATH, '//*[@id="top-banner"]/div[2]/div/div/div/div[2]/div/div[3]/div[1]/div/div/div/div[2]/div/div[2]/div[2]/div[3]/div[4]/div[2]')
select_20_may.click()
time.sleep(1)

select_class = driver.find_element(By.XPATH, '//*[@id="top-banner"]/div[2]/div/div/div/div[2]/div/div[4]/ul/li[3]')
select_class.click()

search_button = driver.find_element(By.XPATH, '//*[@id="top-banner"]/div[2]/div/div/div/div[2]/p/a')
search_button.click()
