import yaml
from appium import webdriver
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By


class BasePage:
    # 创建一个黑名单，用来放弹窗这种，底下for循环遍历
    # _black_list = [(By.ID,"image_cancel")]
    _black_list = []
    _error_cont = 0
    _error_max = 10
    _params = {}

    # 增加冒号：声明用的类型
    def __init__(self, driver: WebDriver = None):
        # 声明一个driver,driver 用的是webdriver
        self._driver = driver

        # 封装一个方法

    def find(self, by, locator=None):
        try:
            element = self._driver.find_elements(*by) if isinstance(by, tuple) else self._driver.find_element(by,
                                                                                                              locator)
            self._error_cont = 0
            return element
        except Exception as e:
            # 防止死循环，遍历如果这个元素没有找到就走下面流程，错误次数加1，最后这个次数最大为10
            self._error_cont += 1
            if self._error_cont >= self._error_max:
                raise e

            for black in self._black_list:
                elements = self._driver.find_elements(*black)
                if len(elements) > 0:
                    elements[0].click()
                    return self.find(by, locator)

    def send(self,value,by,locator=None):
        try:
            self.find(by,locator).send_keys(value)
            self._error_cont = 0
        except Exception as e:
            self._error_cont += 1
            if self._error_cont >= self._error_max:
                raise e

            for black in self._black_list:
                elements = self._driver.find_elements(*black)
                if len(elements) > 0:
                    elements[0].click()
                    return self.send(value,by,locator)
            raise e

    # 怎么读yaml文件
    def steps(self, path):
        # open 要跟一个close,with直接带close
        with open(path, encoding="utf-8") as f:
            steps: list[dict] = yaml.safe_load(f)
            # 可以反复读取，如果yaml里面多个列表内容
            for step in steps:
                if "by" in step.keys():
                    element = self.find(step["by"], step["locator"])
                if "action" in step.keys():
                    if "click" == step["action"]:
                        # self.find(step["by"], step["locator"]).click()
                        element.click()
                    if "send" == step["action"]:
                        # 把value的值取出来，对content进行解析如果文件有{value}那么久进行替换，可以替换成变量，自己定义
                        content: str = step["value"]
                        # 替换params的key,哪个key呢？进行循环
                        for pararm in self._params:
                            # 这里做个替换，如果yaml文件里面的大货号value命中了其中字典的一个值，就把字典的值替换
                            content = content.replace("{%s}" % pararm, self._params[pararm])
                        element.send_keys(content)
                        self.send(content,step["by"],step["locator"])
