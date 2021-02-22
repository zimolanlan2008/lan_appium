from test1.page.basepage import BasePage
from test1.page.search import Search

"""
1、行情页面：行情这个页面需要操作，点击搜索，然后返回到搜索页面
2、搜索页面：搜索页面单独建模，点击搜索输入信息，选择，点击

"""

class Market(BasePage):

    def goto_search(self):
        self.steps("../page/market.yaml")
        return Search(self._driver)