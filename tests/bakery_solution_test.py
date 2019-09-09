import pytest
from src.bakery_solution import Bakery

class TestBakery(object):
    
    @classmethod
    def setup_class(cls):
        cls.bakery = Bakery()

    def test_check_bakery_object(self):
        assert isinstance(TestBakery.bakery, Bakery), \
            'Given object is not instance of Bakery class.'

    @pytest.mark.parametrize("code,pack,price,expected",[('VS5',2,6.99,True),\
        ('VS5',3,8.99,True),])
    def test_add_bakery_item_pack(self,code,pack,price,expected):
        observed = TestBakery.bakery.add_bakery_item_pack(code,pack,price)
        assert expected == observed, 'Failed to add item in bakery_item_pack list.'
    
    @pytest.mark.parametrize("name,code,expected",[('Vegemite Scroll','VS5',True),\
        ('Blueberry Muffin','MB11',True),])
    def test_add_bakery_item(self,name,code,expected):
        observed = TestBakery.bakery.add_bakery_item(name,code)
        assert expected == observed, 'Failed to add item in bakery_items list.'

    @pytest.fixture(scope='function')
    def bakery_object(self,request):
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

    @pytest.mark.parametrize("code,size,expected",[('VS5',3,6.99),('VS5',5,8.99)])
    def test_get_bakary_item_pack(self,code, size, expected, bakery_object):
        assert bakery_object.get_bakery_item_pack(code,size) == expected, \
            'Wrong value fetched for code- {} and size- {}'.format(code,size)

    def test_get_bakary_item_with_wrong_code(self,bakery_object):
        with pytest.raises(ValueError):
            bakery_object.get_bakery_item('Blueberry cake')
            
    def test_get_bakary_item(self,bakery_object):
        assert bakery_object.get_bakery_item('VS5') == 'Vegemite Scroll'

    def test_get_bakary_item_pack_with_wrong_size(self,bakery_object):
        size = 8
        with pytest.raises(ValueError):
            bakery_object.get_bakery_item_pack('VS5',size)
            
    def test_get_bakary_item_pack_with_wrong_code(self,bakery_object):
        code = 'VS15'
        with pytest.raises(ValueError):
            bakery_object.get_bakery_item_pack(code,8)
    
    @pytest.mark.parametrize("code, order_size,expected,pack",[('VS5',10,17.98,[5]),\
        ('MB11',14,54.8,[8,2]),('CF',13,25.85,[5,3])])
    def test_order_bakery_items(self, code, order_size, expected, pack, bakery_object):
        price, pack_combo = bakery_object.order_bakery_item(code,order_size)
        assert price == expected, 'Expecting {} but got {}'.format(expected, price)
        observed = list(pack_combo.keys())
        observed.sort(reverse=True)
        assert observed == pack, 'Expecting {} but got {}'.format(pack,observed)

    def test_order_bakery_item_when_order_size_is_very_small(self,bakery_object):
        order_size = 1
        with pytest.raises(ValueError):
            bakery_object.order_bakery_item('VS5',order_size)

    def test_order_bakery_item_when_method_could_not_find_pack_combinations(self,bakery_object):
        order_size = 7
        with pytest.raises(ValueError):
            bakery_object.order_bakery_item('CF',order_size)

    @classmethod
    def teardown_class(cls):
        del TestBakery.bakery