from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains as ac
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
driver = webdriver.Chrome()
url = 'http://www.baidu.com'
driver.get(url)

class A():
    # 鼠标移动显示事件
    # "更多"的name='tj_briicon'
    def test(self):
        element = driver.find_element_by_name('tj_briicon')
        ac(driver).move_to_element(element).perform()
        time.sleep(10)
        # 新版本
        element = driver.find_element(By.NAME, 'tj_briicon')
        ac(driver).move_to_element(element).perform()
        time.sleep(10)
    # 键盘事件
    def test1(self):
        str = input("请输入信息：")
        print("你输入的信息是: ", str)

    # 清空输入方法
    def test2(self):
        element0 = driver.find_element_by_id('kw')
        element0.clear()
        print('已清空')
        element0.send_keys('自动化测试')
        print('输入值')
        time.sleep(3)

    # 点击方法
        element1 = driver.find_element_by_id('su')
        element1.click()
        print('已点击')
    # 窗口最大化
    # 最大化窗口
        driver.maximize_window()

    #滚动网页
        target = driver.find_element_by_xpath('//a[text()="下一页 >"]')
        driver.execute_script("arguments[0].scrollIntoView();", target)
        time.sleep(6)



    # 浏览器导航
    def test3():
        # 前进
        driver.forward()
        print('前进')
        time.sleep(5)
        # 后退
        driver.back()
        print('后退')
        time.sleep(5)
        # 刷新
        driver.refresh()

    # 浏览器切换窗口
    def test4(self):
        driver.switch_to_window(driver.window_handles[0])

    # 等待时间
    def test5(self):
    # 强制等待（不管你浏览器是否加载完了，程序都得等待30秒）
        time.sleep(30)
    # 隐性等待 是设置了一个最长等待时间，如果在规定时间内网页加载完成，则执行下一步，否则一直等到时间截止，然后执行下一步。在全局变量内
    # 注意这里有一个弊端，那就是程序会一直等待整个页面加载完成，也就是一般情况下你看到浏览器标签栏那个小圈不再转，才会执行下一步
        driver.implicitly_wait(30)
    # 显性等待（指定的元素是否加载完，加载完了就执行下一步，否则继续每隔x秒去判断）
        element1 = driver.find_element_by_id('kw')
        WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located(element1))

    def test6(self):
        element2 = driver.find_element_by_xpath("//div[@id='u1']//a[text()='登录']")
        element3 = driver.find_element_by_id('kw')
        ac(driver).drag_and_drop(element1, element2).perform()
    def test7(self):
        driver.get_screenshot_as_file("C:\\Users\\qshang\\OneDrive - DXC Production\\Pictures\\Screenshots\\baidu.jpg")


if __name__ == '__main__':
    A().test7()


