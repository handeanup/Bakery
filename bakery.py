from src.bakery_solution import Bakery

def initialize_bakery_data():
    bk = Bakery()
    bk.add_bakery_item_pack('VS5',3,6.99)
    bk.add_bakery_item_pack('VS5',5,8.99)
    bk.add_bakery_item_pack('MB11',2,9.95)
    bk.add_bakery_item_pack('MB11',5,16.95)
    bk.add_bakery_item_pack('MB11',8,24.95)
    bk.add_bakery_item_pack('CF',3,5.95)
    bk.add_bakery_item_pack('CF',5,9.95)
    bk.add_bakery_item_pack('CF',9,16.95)
    bk.add_bakery_item('Vegemite Scroll','VS5')
    bk.add_bakery_item('Blueberry Muffin','MB11')
    bk.add_bakery_item('Croissant','CF')
    return bk

def main():
    #Get bakery object
    bk = initialize_bakery_data()
    with open('sample_input.txt','r') as fp:
        lines = fp.readlines()
        for line in lines:
            try:
                order_size, code = line.split()
            except ValueError:
                continue
            try:
                price,pack_obj = bk.order_bakery_item(code.strip(),int(order_size))
            except ValueError as e:
                print(str(e))
                continue    
            print('{} {} ${}'.format(order_size,code,price))
            for pack,l in pack_obj.items() :
                pak_price = bk.get_bakery_item_pack(code,pack)
                print('\t{} x {} ${}'.format(l[0],pack, pak_price))

if __name__ == "__main__":
    main()