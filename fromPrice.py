from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time
import random

driver = webdriver.Chrome(executable_path='/Users/sasakiryou/Downloads/chromedriver')
driver.get("https://www.amazon.co.jp/b?ie=UTF8&node=8443136051")
# カテゴリから支援先を選ぶ（ランダムに選択）
# todo: 現在は１ページ目しか取得出来ないので、２ページ目以降も取得出来るようにする
# todo: 動物のページが取得出来ないのでできるようにする
categoryNum = random.randint(0, 1)
target = driver.find_element(By.ID,f"a-autoid-{categoryNum}-announce")
target.click()
length = len(driver.find_elements(By.TAG_NAME,"h5"))
id = random.randint(0, length - 1)
target = driver.find_elements(By.TAG_NAME,"h5")[id]
target.find_element(By.XPATH,"../a").click()
time.sleep(3)
# ほしい物リストのページに遷移
list = driver.find_elements(By.CLASS_NAME,"a-price-whole")
totalPrice = 4000
for index,element in enumerate(list):
  price = int(element.text.replace(",", ""))
  target = driver.find_elements(By.PARTIAL_LINK_TEXT,"カートに入れる")
  length = len(target)
  if(price < 4000): 
    id = index
    totalPrice -= price
    target[id].click()
    time.sleep(3)
    break
time.sleep(3)
exit()
driver.find_element(By.ID,"sc-buy-box-ptc-button").click()
url = driver.current_url
mail = "axshot@yahoo.co.jp"
target = driver.find_element(By.ID,"ap_email").send_keys(mail)
driver.find_element(By.ID,"continue").click()
time.sleep(3)
passWord = "3391sanda"
target = driver.find_element(By.ID,"ap_password").send_keys(passWord)
driver.find_element(By.ID,"signInSubmit").click()
# TODO:ログイン状態が保持されている場合はスリープするとうまくいかないから処理を分ける必要がある
# time.sleep(3)
url = driver.current_url
while url:
  newUrl = driver.current_url
  time.sleep(3)
  if(url != newUrl):
    time.sleep(3)
    break
target = driver.find_element(By.XPATH,"//*[@id='address-list']/div/div[1]/div/fieldset[2]/div[1]/span/div/label/input").click()
time.sleep(3)
target = driver.find_element(By.XPATH,"//*[@id='shipToThisAddressButton']/span/input").click()
time.sleep(10)
target = driver.find_element(By.XPATH,"//*[@id='orderSummaryPrimaryActionBtn']/span/input").click()
time.sleep(3)
lastNumbers ="144"
# todo: 以下も出る時とでない時があるから分岐させる必要がある
target = driver.find_element(By.XPATH, "//input[contains(@placeholder,'末尾  0454')]").send_keys(lastNumbers)
time.sleep(3)
target = driver.find_element(By.XPATH,"//button[contains(text(),'お客様のカードを照合します')]").click()
# target = driver.find_element(By.XPATH,"//*[text()='お客様のカードを照合します']").click()
time.sleep(5)
# todo: 確定ボタンを押す処理を書く（テストでも購入してしまうので慎重に）

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