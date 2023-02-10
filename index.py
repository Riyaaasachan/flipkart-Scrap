from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup as bs
import time
import pandas as pd

driver=webdriver.Chrome(executable_path="D:\chromedriver.exe")
driver.maximize_window()

website='https://www.flipkart.com/search?q=samsung+mobiles'
website='https://www.flipkart.com/search?q=samsung+mobiles'
driver.get(website)

driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
time.sleep(1)
   

modelName=driver.find_elements(By.XPATH, '//*[@id="container"]/div/div[3]/div[1]/div[2]/div/div/div/div/a/div[2]/div[1]/div[1]')
spect=driver.find_elements(By.XPATH, 'rgWa7D:nth-child(1)')
price=driver.find_elements(By.XPATH, '//*[@id="container"]/div/div[3]/div[1]/div[2]/div/div/div/div/a/div[2]/div[2]/div[1]/div[1]/div[1]')

model_name =[]
specification =[]
Price =[]

for i in modelName:
    model_name.append(i.text)
for j in spect:
        specification.append(j.text) 
for k in price:
    try:
        Price.append(k.text) 
    except:
        Price.append("No Data")    

print(len(model_name))
print(len(specification))
print(len(Price))
print(Price)

df =pd.DataFrame({'Title':model_name,'Specification':specification,'Price':Price})
df.to_csv('data',index =False)