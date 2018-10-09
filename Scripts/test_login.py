import sys,os
sys.path.append(os.getcwd())

import allure
from Page.page_login import PageLogin
from Base.get_driver import get_driver


class TestLogin():
    def setup_class(self):
        # 实例化PageLogin
        self.login = PageLogin(get_driver())
    def teardown_class(self):
        # 退出driver驱动
        self.login.driver.quit()
    def test_login(self):
        # 登录操作
        self.login.page_login("13331172859","123456")
        try:
            # 断言登录是否成功
            assert "lj0918" in self.login.page_get_nickname()
            print('登录成功')
            # 退出操作
            self.login.page_login_logout()
        except:
            # 失败 截图
            self.login.base_getimage()
            with open('./Image/failed.png','rb') as f:
                allure.attach('登录失败描述：',f.read(),allure.attach_type.PNG)
            # 抛出异常
            raise