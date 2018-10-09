from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class Base():
    # 初始化浏览器参数
    def __init__(self, driver):
        self.driver = driver

    # 元素定位方法
    def base_find_element(self,loc,timeout=30,poll=0.5):
        return WebDriverWait(self.driver,timeout=timeout,poll_frequency=poll).until(lambda x:x.find_element(*loc))

    # 点击元素方法
    def base_click(self,loc):
        self.base_find_element(loc).click()

    # 文本框输入方法
    def base_input(self,loc,text):
        self.base_find_element(loc).send_keys(text)

    # 截图方法
    def base_getimage(self):
        Path = "./Image/failed.png"
        self.driver.get_screenshot_as_file(Path)

    # 页面滑动方法 el1元素滑动到el2元素(退出使用)
    def base_darg_and_drop(self,el1,el2):
        self.driver.drag_and_drop(el1,el2)

    # 获取元素文本方法(文本 变量接收或设置返回值)
    def base_get_text(self,loc):
        return self.base_find_element(loc).text

    # 获取toast方法
    def base_get_toast(self, message):
        # 模糊定位toast文本内容
        loc = By.XPATH,"//*[contains(@text,'"+message+"')]"
        return self.base_find_element(loc).text





