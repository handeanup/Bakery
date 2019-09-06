import pytest
from src.bakery_solution import Bakery

class TestBakery(object):
    
    def setup_method(self):
        self.bakery = Bakery()

    def test_check_bakery_object(self):
        assert isinstance(self.bakery, Bakery), 'Given object is not instance of Bakery class.'

    @pytest.mark.parametrize("code,pack,price,expected",[('VS5',2,6.99,1),('VS5',3,8.99,1),])
    def test_add_bakery_item_pack(self,code,pack,price,expected):
        observed = self.bakery.add_bakery_item_pack(code,pack,price)
        assert expected == observed, 'Failed to add item in bakery_item_pack list.'
    
    @pytest.mark.parametrize("name,code,expected",[('Vegemite Scroll','VS5',1),('Blueberry Muffin','MB11',1),])
    def test_add_bakery_item(self,name,code,expected):
        observed = self.bakery.add_bakery_item(name,code)
        assert expected == observed, 'Failed to add item in bakery_items list.'

    def teardown_method(self):
        del self.bakery