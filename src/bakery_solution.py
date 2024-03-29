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
            self.bakery_items[code]=name
            logging.info('Bakery item with name {} and code {} added.'.\
                format(name,code))
        except KeyError as e:
            logging.error('Failed to add item in bakery list.')
            logging.error(e.with_traceback)
            return False
        else:
            return True

    def get_bakery_item(self,code):
        if code in self.bakery_items.keys():
            return self.bakery_items[code]
        else:
            logging.error('Bakery item with code {} not available.'.\
                format(code))
            raise ValueError('Bakery item with code {} not available.'.\
                format(code))

    def add_bakery_item_pack(self,code,size,price):
        try:
            if code not in self.bakery_packs.keys():
                self.bakery_packs[code] = {size:price}
            else:
                self.bakery_packs[code].update({size: price})
            logging.info('Bakery item {} with size {} and price {} added.'\
                .format(code,size,price))
        except KeyError:
            logging.error('Failed to add pack item in list.')
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
            raise ValueError('Bakery item with code {} and size {} not available.'\
                .format(code,size))

    def __get_pack_util(self,pack_list, requested_size, result_pack, \
        result_size, result_list ):
        if result_size == requested_size:
            result_list.append(result_pack.copy())
            return True
        else:
            for pack in pack_list:
                if result_size + pack <= requested_size:
                    result_size += pack
                    result_pack.append(pack)
                    if self.__get_pack_util(pack_list, requested_size, \
                        result_pack, result_size, result_list):
                        return True
                    result_size -= pack
                    result_pack.remove(pack)
            return False

    def __get_total_price_and_pack_details(self, code, result_list):
        final_price = 0
        pack_combo = {}
        for pack in result_list[0]:
            pack_price = self.bakery_packs[code][pack]
            final_price += pack_price
            if pack not in pack_combo.keys():
                pack_combo[pack] = [1,pack_price]
            else:
                count = pack_combo[pack][0]
                price = pack_combo[pack][1]
                pack_combo[pack] = [count+1,price+pack_price]
        return float(format(final_price,'.2f')), pack_combo
            

    def order_bakery_item(self, code, order_size):
        # Check for item present in bakery or not
        if code not in self.bakery_packs.keys():
            logging.error('Requested item {} not available.'.format(code))
            raise ValueError('Could not find item {} in bakery list.'.format(code))
        pack_list = list(self.bakery_packs[code].keys())
        pack_list.sort(reverse=True)
        result_pack = []
        result_list = []
        if self.__get_pack_util(pack_list, order_size, \
            result_pack, 0, result_list):
            return self.__get_total_price_and_pack_details(code,result_list)
        else:
            logging.error(\
                "Requested order of {} for {} could not be placed as no combination available.".\
                format(order_size,code))
            raise ValueError('Could not find any combination of {} packs for order {}'.format(code,order_size))