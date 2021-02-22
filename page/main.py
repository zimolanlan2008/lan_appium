"""
主要操作方法
首页点击到行业页面，点击搜索，输入一些内容，查询
return传一个参数driver，命中app启动时候else，复用基本方法
"""
from test1.page.basepage import BasePage
from test1.page.market import Market



class Main(BasePage):
    def goto_market(self):
        # ..代表上一级目录，指向test1这个目录
        self.steps("../page/main.yaml")
        return Market(self._driver)



