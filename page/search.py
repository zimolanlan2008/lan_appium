from test1.page.basepage import BasePage


class Search(BasePage):
    """
    搜索页面相关操作
    传个参数value
    """
    def search(self,value):
        self._params["value"] = value
        self.steps("../page/search.yaml")

