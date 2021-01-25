from  commen import method
from test_data import test_data
from selenium import webdriver
driver=webdriver.Chrome()
driver.implicitly_wait(10)
url=test_data.data.get("url")
username=test_data.data.get("username")
password=test_data.data.get("password")
key=test_data.data.get("key")
print(url,username,password,key)
num=method.sear_fun(driver,url,username,password,key)
print(num)
if key in num:
    print("搜索到数据")
else:
    print("没有搜索到")