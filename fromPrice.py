from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time
import random
import requests

driver = webdriver.Chrome(executable_path='/Users/sasakiryou/Downloads/chromedriver')
driver.get("https://www.amazon.co.jp/b?ie=UTF8&node=8443136051")
# カテゴリから支援先を選ぶ（ランダムに選択）
# todo: 現在は１ページ目しか取得出来ないので、２ページ目以降も取得出来るようにする
# todo: 動物のページが取得出来ないのでできるようにする
categoryNum = random.randint(0, 1)
target = driver.find_element(By.ID,f"a-autoid-{categoryNum}-announce")
target.click()
# 選択したカテゴリのページに遷移
sightList = driver.find_elements(By.TAG_NAME,"h5")
length = len(sightList)
id = random.randint(0, length - 1)
goToPreviousPage = False
response = requests.get("http://127.0.0.1:8000/api/get/1").json()["donation_amount"]
# print(response.json()["donation_amount"],"response")
totalPrice = response
print(totalPrice,"totalPrice")
# 施設一覧を取得する処理
for i,elm in enumerate(sightList):
  index = 0
  print(i,"回目のループ",totalPrice)
  sightList = driver.find_elements(By.TAG_NAME,"h5")
  # print(sightList,"sightList")
  time.sleep(3)
  length = len(sightList)
  # print(length,"length")
  id = random.randint(0, length - 1)
  target = sightList[id]
  # print(id,"id",target,"target")
  target.find_element(By.XPATH,"../a").click()
  time.sleep(3)
  # ほしい物リストのページに遷移
  driver.find_element(By.XPATH,"//*[@id='list-view-switcher']").click()
  time.sleep(3)
  itemList = driver.find_elements(By.CLASS_NAME,"a-price-whole")
  if(itemList == []):
    print("商品がありませんでした")
    goToPreviousPage = True
    i+=1
    driver.back()
  # ほしい物リスト一覧を取得
  for index,element in enumerate(itemList):
    itemList = driver.find_elements(By.CLASS_NAME,"a-price-whole")
    # print(index,"index")
    element = itemList[index]
    # TODO: 配送料がある場合はそれも加算する必要がある
    price = int(element.text.replace(",", ""))
    prices = driver.find_elements(By.CLASS_NAME,"a-price-whole")
    target = driver.find_elements(By.PARTIAL_LINK_TEXT,"カートに入れる")
    nextPrice = 0
    print(price,"price")
    # ほしい物リストが2つ以上ある場合は、次の商品の価格を取得する
    if(len(itemList) > 0 and index + 1 <= len(itemList) - 1):
      nextPrice = int(itemList[index+1].text.replace(",", ""))
      print(nextPrice,"nextPrice")
    # 予算があり、商品の価格が予算を超えていない場合はカートに入れる
    if(totalPrice > 0 and totalPrice >= price): 
      # id = index
      target[index].click()
      totalPrice -= price
      print(totalPrice,price,nextPrice,"商品購入しました")
      # 予算がない場合はカートに入れる処理を終了する
      if(totalPrice < 500):
        goToPreviousPage=False
        print("予算に達しました1")
        break
      # 次の商品が予算を超えている場合の処理
      elif( totalPrice < nextPrice):
        print(totalPrice,nextPrice,index,"totalPrice<nextPrice")
        # 予算を超えている地点からリスト内を見る
        for j in range(index+1,len(itemList)):
          print(j,"j",index,"index")
          nextPrice = int(itemList[j].text.replace(",", ""))
          # 次の商品が予算オーバーしている場合、次の次の商品の状況を確認する
          if( totalPrice < nextPrice):
            # 次の次の商品がある場合
            if(j+1<=len(itemList)-1):
              j+=1
              nextNextPrice = int(itemList[j].text.replace(",", ""))
              if(totalPrice < nextNextPrice):
                print("予算に達しました2")
                goToPreviousPage=False
                nextNextPrice = 0
                nextPrice = 0
                break
              else:
                element = itemList[j]
                price = int(element.text.replace(",", ""))
                target[j].click()
                totalPrice -= price
                print(totalPrice,price,nextPrice,"商品購入しました2")
                j+=1
            else:
              print("予算に達しました3")
              goToPreviousPage=False
              nextPrice = 0
              break
          else:
            # j+=1
            print(totalPrice,nextPrice,"totalPrice<nextPrice2")
            element = itemList[j]
            price = int(element.text.replace(",", ""))
            target[j].click()
            totalPrice -= price
            print(totalPrice,price,nextPrice,"商品購入しました3")
      # 次の商品がないが予算が500円以上ある場合
      elif(nextPrice == 0 and totalPrice > 500):
        goToPreviousPage=True
        driver.back()
        break
      print(totalPrice,"totalPrice")
      time.sleep(3)
      # 予算に達していない場合前のページに戻り、次の商品を選択する
      if(0<totalPrice<500):
        goToPreviousPage=False
        break
      # elif(totalPrice<nextPrice):
      #   goToPreviousPage=True
      #   driver.back()
      #   break
      else:
        print("now1")
        goToPreviousPage=True
        driver.back()
        # break
    # 次の商品がある場合は再度ループを回す
    elif(totalPrice >0 and nextPrice != 0):
      index+=1
      print("indexを増やしました")
    else:
      print("todo:違うページを見に行く実装をする")
      goToPreviousPage = True
      driver.back()
      time.sleep(3)
      break
    index += 1
    # print(id,"番目の商品をカートに入れました")
  time.sleep(3)
  # 次のページにいく
  print("now2")
  if(goToPreviousPage==False):
    break
# ここで引っかかる場合がある
  # todo: 欲しいものが贈れない商品の場合があるので、その場合の処理も追加する必要がある
print("カートに入れる処理終了")
driver.find_element(By.ID,"sc-buy-box-ptc-button").click()
url = driver.current_url
mail = "axshot@yahoo.co.jp"
target = driver.find_element(By.ID,"ap_email").send_keys(mail)
driver.find_element(By.ID,"continue").click()
time.sleep(3)
passWord = "3391sanda"
target = driver.find_element(By.ID,"ap_password").send_keys(passWord)
driver.find_element(By.ID,"signInSubmit").click()
# todo:urlが変わらない場合があるので、処理を分ける必要がある
# TODO:ログイン状態が保持されている場合はスリープするとうまくいかないから処理を分ける必要がある
# time.sleep(3)
# url = driver.current_url
# print(url,"url")
# while url:
#   newUrl = driver.current_url
#   print(  url,newUrl,"ログイン中")
#   time.sleep(3)
#   if(url != newUrl):
#     time.sleep(3)
#     break
# todo: 最近寄付した施設の場合、１番上に来るので、ギフト用というテキストがあるかどうかで判断するようにする
# todo: 複数商品がある場合宛先を複数を選択する必要がある
driver.find_element(By.XPATH,"//*[@id='address-list']/div/div[1]/div/fieldset[2]/div[1]/span/div/label/input").click()
print("ここにいる１")
time.sleep(3)
driver.find_element(By.XPATH,"//*[@id='shipToThisAddressButton']/span/input").click()
print("ここにいる２")
time.sleep(10)
driver.find_element(By.XPATH,"//*[@id='orderSummaryPrimaryActionBtn']/span/input").click()
print("ここにいる３")
time.sleep(3)
target = driver.find_elements(By.XPATH,"//h4[contains(text(),'ご注文いただいた商品のいくつかに問題がありました')]")
print(target,"target")
if(target):
  print("商品がない")
  deleteImtes = driver.find_elements(By.XPATH,"//span[contains(text(),'削除')]")
  for deleteItem in deleteImtes:
    deleteItem.click()
  time.sleep(3)
# todo:登録していない場合はここからは本人に操作させる
lastNumbers ="5210120092920454"
# todo: 以下も出る時とでない時があるから分岐させる必要がある
target = driver.find_elements(By.XPATH,"//button[contains(text(),'注文を確定')]")
print(target,"target")
if(target):
  print("注文確定ボタンがある")
else:
  driver.find_element(By.XPATH, "//input[contains(@placeholder,'末尾  0454')]").send_keys(lastNumbers)
time.sleep(3)
driver.find_element(By.XPATH,"//button[contains(text(),'お客様のカードを照合します')]").click()
time.sleep(3)
driver.find_element(By.XPATH,"//button[contains(text(),'このお支払い方法を使う')]").click()
time.sleep(3)
# 注文を確定（テスト中は非表示）
# driver.find_element(By.XPATH,"//button[contains(text(),'注文を確定')]").click()
# time.sleep(3)