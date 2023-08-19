class ShoppingList:
    """初始化购物清单，shopping_list是字典，包含商品和商品价格
    shopping_list={"牙刷": 5, "沐浴露“: 15, "电池": 7}"""
    def __init__(self, shopping_list):
        self.shopping_list = shopping_list
    """返回购物清单上有多少商品"""
    def get_item_count(self):
        return len(self.shopping_list)
    """返回购物清单上商品总价"""
    def get_total_price(self):
        total_price = 0
        for price in self.shopping_list.values():
            total_price = total_price + price
        return total_price

