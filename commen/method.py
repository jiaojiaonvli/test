# 浏览器驱动只执行一次，所以作为参数传入
# 打开浏览器函数
import time
def open_url(browser,url):
    browser.get(url)
    browser.implicitly_wait(10)
# 登录函数
def login_fun(browser,username,password):
    browser.find_element_by_id("username").send_keys(username)
    browser.find_element_by_id("password").send_keys(password)
    # 记住账号
    browser.find_element_by_xpath("//input[@id='rememberUserCode']/following-sibling::ins").click()
    browser.find_element_by_id("btnSubmit").click()
# 搜索函数
def sear_fun(browser,url,username,password,key):
    open_url(browser,url)
    login_fun(browser,username,password)
    page_name = browser.find_element_by_xpath("//p").text
    browser.find_element_by_xpath("//span[contains(text(),'零售出库')]").click()
    page_id = browser.find_element_by_xpath("//div[text()='零售出库']/..").get_attribute("id")
    print(page_id)
    id_frame = page_id + "-frame"  # 得到iframe id
    browser.switch_to.frame(browser.find_element_by_xpath("//iframe[@id='{}']".format(id_frame)))
    # 找到搜索框输入数据
    browser.find_element_by_id("searchNumber").send_keys(key)
    browser.find_element_by_xpath("//*[@id='searchBtn']/span/span").click()
    time.sleep(1)  # 隐式等待+强制等待的使用
    # 获得单据编码的号码(文本)
    num = browser.find_element_by_xpath("//tr[@id='datagrid-row-r1-2-0']//td[@field='number']/div").text
    return num
