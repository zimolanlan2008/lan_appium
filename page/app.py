"""
日常操作，启动之类
"""
from appium import webdriver

from test1.page.basepage import BasePage
from test1.page.main import Main


class App(BasePage):
    def start(self):
        _package = 'com.xueqiu.android'
        _activity = '.common.MainActivity'
        if self._driver is None:
            desired_caps = {}
            desired_caps['platformName'] = 'Android'
            desired_caps['platformVersion'] = '6.0'
            desired_caps['deviceName'] = '127.0.0.1:7555'
            desired_caps['appPackage'] = _package
            desired_caps['appActivity'] = _activity
            desired_caps['noReset'] = 'True'
            # 保留之前的记录，如果想重新启动可以去掉这个配置
            # desired_caps['dontStopAppOnReset'] = 'true'
            desired_caps['skipDeviceInitialization'] = 'true'
            desired_caps['unicodeKeyBoard'] = 'true'
            desired_caps['resetKeyBoard'] = 'true'

            self._driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
            self._driver.implicitly_wait(10)
        else:
            self._driver.start_activity(_package,_activity)
        return self
    def main(self):
        return Main(self._driver)