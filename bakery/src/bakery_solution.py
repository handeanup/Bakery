
class Bakery:
    def __init__(self, *args, **kwargs):
        self.bakery_items = {}
        self.bakery_packs = {}
    
    def add_bakery_item(self,name,code):
        self.bakery_items[code]=name
        return len(self.bakery_items)

    def get_bakery_item(self,code):
        pass

    def add_bakery_item_pack(self,code,size=0,price=0):
        self.bakery_packs.update({code:{size:price}})
        return len(self.bakery_packs)

    def get_bakery_item_pack(self,code,size=0):
        pass