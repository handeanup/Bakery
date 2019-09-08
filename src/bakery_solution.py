import logging

#log configuration
logging.basicConfig(filename='logs/bakery.log', \
    filemode='a', format='%(asctime)s : %(levelname)s : %(message)s')

class Bakery:
    def __init__(self, *args, **kwargs):
        self.bakery_items = {}
        self.bakery_packs = {}
    
    def add_bakery_item(self,name,code):
        try:
            self.bakery_items[name]=code
            logging.info('Bakery item with name {} and code {} added.'.\
                format(name,code))
        except KeyError as e:
            logging.error('Failed to add item in bakery list.')
            logging.error(e.with_traceback)
            return False
        else:
            return True

    def get_bakery_item(self,name):
        if name in self.bakery_items.keys():
            return self.bakery_items[name]
        else:
            logging.error('Bakery item with code {} not available.'.\
                format(name))
            return None

    def add_bakery_item_pack(self,code,size,price):
        try:
            if code not in self.bakery_packs.keys():
                self.bakery_packs[code] = {size:price}
            else:
                self.bakery_packs[code].update({size: price})
            logging.info('Bakery item {} with size {} and price {} added.'\
                .format(code,size,price))
        except KeyError as e:
            logging.error('Failed to add pack item in list.')
            logging.error(e.with_traceback)
            return False
        else:
            return True

    def get_bakery_item_pack(self,code,size):
        if code in self.bakery_packs.keys() and size in \
            self.bakery_packs[code].keys():
            return self.bakery_packs[code][size]
        else:
            logging.error('Bakery item with code {} and size {} not available.'\
                .format(code,size))
            return None

    def __get_pack_util(self,pack_list, requested_size, result_pack, \
        result_size, result_list ):
        if result_size == requested_size:
            result_pack.sort(reverse=True)
            if result_pack not in result_list:
                result_list.append(result_pack.copy())
            return 0
        else:
            for i,pack in enumerate(pack_list):
                if result_size + pack <= requested_size:
                    result_size += pack
                    result_pack.append(pack)
                    self.__get_pack_util(pack_list, requested_size, \
                        result_pack, result_size, result_list)
                    result_size -= pack
                    result_pack.remove(pack)

    def __get_total_price_and_pack_details(self, code, result_list):
        result_list = min(result_list,key=len)
        final_price = 0
        pack_combo = {}
        for i,pack in enumerate(result_list):
            pack_price = self.bakery_packs[code][pack]
            final_price += pack_price
            if pack not in pack_combo.keys():
                pack_combo[pack] = [1,pack_price]
            else:
                count = pack_combo[pack][0]
                price = pack_combo[pack][1]
                pack_combo[pack] = [count+1,price+pack_price]
        return float(format(final_price,'.2f')), pack_combo
            

    def order_bakery_item(self, name, order_size):
        code = self.get_bakery_item(name)
        pack_list = list(self.bakery_packs[code].keys())
        result_pack = []
        result_list = []
        self.__get_pack_util(pack_list, order_size, \
            result_pack, 0, result_list)
        if len(result_list) > 0 :
            return self.__get_total_price_and_pack_details(code,result_list)
        else:
            logging.error(\
                "Requested order of {} for {} could not be placed as no combination available.".\
                format(order_size,name))
            return None 