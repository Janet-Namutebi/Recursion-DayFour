import unittest

from app.sum_item_list import sum_items

class TestSumItem(unittest.TestCase):

    def test_sum_items(self):
        """Tests whether sum_items can add items in a list without another 
        list inside"""
        self.assertEqual(sum_items([3,7,8]), 18)
    
    def test_sum_items_with_inside_list(self):
        """Tests whether sum_items can add items in a list with another list inside"""
        self.assertEqual(sum_items([3,7,8,[8,9]]), 35)
    
    def test_sum_items_list_with_other_types(self):
        """Tests whether sum_items detect the types of items in a list to know that 
        they aren't integers"""
        self.assertEqual(sum_items([3,7,'v',[8,9]]), 27)
        
    def test_sum_items_insidelist_with_other_types(self):
        """Tests whether sum_items detect the types of items in the inside list to 
        know that they aren't integers"""
        self.assertEqual(sum_items([3,7,['q',9]]), 19)


if __name__ == "__main__":
    unittest.main()