import logging

#log configuration
logging.basicConfig(filename='logs/bakery.log', \
    filemode='a', format='%(name)s - %(levelname)s - %(message)s')

class Bakery:
    def __init__(self, *args, **kwargs):
        self.bakery_items = {}
        self.bakery_packs = {}
    
    def add_bakery_item(self,name,code):
        try:
            self.bakery_items[code]=name
            logging.info('Bakery item {} with name {} added.'.format(code,name))
        except Exception as e:
            logging.error('Failed to add item in bakery list.')
            logging.error(e.with_traceback)
            return False
        else:
            return True

    def get_bakery_item(self,code):
        if code in self.bakery_items.keys():
            return self.bakery_items[code]
        else:
            logging.error('Bakery item with code {} not available.'.format(code))
            return None

    def add_bakery_item_pack(self,code,size,price):
        try:
            if code not in self.bakery_packs.keys():
                self.bakery_packs[code] = {size:price}
            else:
                self.bakery_packs[code].update({size: price})
            logging.info('Bakery item {} with size {} and price {} added.'\
                .format(code,size,price))
        except Exception as e:
            logging.error('Failed to add pack item in list.')
            logging.error(e.with_traceback)
            return False
        else:
            return True

    def get_bakery_item_pack(self,code,size):
        if code in self.bakery_packs.keys() and size in self.bakery_packs[code].keys():
            return self.bakery_packs[code][size]
        else:
            logging.error('Bakery item with code {} and size {} not available.'.format(code,size))
            return None