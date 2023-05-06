# import requests
# from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path='/Users/sasakiryou/Downloads/chromedriver')
driver.get("https://www.amazon.co.jp/b?ie=UTF8&node=8443136051")
target = driver.find_element(By.ID,"a-autoid-0-announce")
target.click()
url = driver.current_url
driver.get(url)
target = driver.find_element(By.TAG_NAME,"h5")
target.find_element(By.XPATH,"..").click()
url = driver.current_url
driver.get(url)
print(url)
for element in driver.find_elements(By.CLASS_NAME,"a-price-whole"):
  price = int(element.text.replace(",", ""))
  if(price < 4000): 
    target = driver.find_element(By.PARTIAL_LINK_TEXT,"カートに入れる").click()
    time.sleep(3)
    print(url)
    # loc = target.location
    # # print(loc)
    # x, y = loc['x'], loc['y']
    # actions = ActionChains(driver)
    # actions.move_by_offset(x, y)
    # actions.click()
    # actions.perform()
    # url = driver.current_url
    # driver.switch_to.window(driver.window_handles[0])
    # target = driver.find_element(By.ID,"pab-declarative-IDMRFYKKHDKIL")
    # driver.execute_script('return arguments[0].innerText', target)
    # ActionChains(driver)\
    #     .click_and_hold(target)\
    #     .perform()
    # target = driver.find_element(By.XPATH,'//a[text()="カートに入れる"]')
    # print(target)
    exit()
# response = requests.get(url)
# soup = BeautifulSoup(response.text, "html.parser")

# prices = 0
# for element in soup.find_all("span", attrs={"class": "a-price-whole"}):
#   price = int(element.getText().replace(",", ""))
#   if price < 4000:
#     # target = element.find_element(By.ID,"itemAction_IDMRFYKKHDKIL")
#     target = soup.find("a",text="お客様サポート")
#     print(target)
#     # target.click()
#     exit()
    
    
#   prices += int(price.replace(",", ""))
#   print(element.getText())
# print(prices)