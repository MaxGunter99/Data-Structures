import unittest
from lru_cache import LRUCache


class CacheTests(unittest.TestCase):
    def setUp(self):
        self.cache = LRUCache(3)
        # self.cache = LRUCache(10)

    # test with limit of 3
    def test_cache_overwrite_appropriately(self):
        self.cache.set('item1', 'z')
        self.cache.set('item1', 'a')
        self.cache.set('item2', 'b')
        self.cache.set('item3', 'c')

        self.assertEqual(self.cache.get('item1') , 'a')
        self.assertEqual(self.cache.get('item2'), 'b')

    def test_cache_insertion_and_retrieval(self):
        self.cache.set('item1', 'a')
        self.cache.set('item2', 'b')
        self.cache.set('item3', 'c')

        self.assertEqual(self.cache.get('item1'), 'a')
        self.cache.set('item4', 'd')

        self.assertEqual(self.cache.get('item1') , None)
        self.assertEqual(self.cache.get('item3'), 'c')
        self.assertEqual(self.cache.get('item4'), 'd')

    def test_cache_nonexistent_retrieval(self):
        self.assertIsNone(self.cache.get('nonexistent') , None)



    # # Test with limit of 10
    # def test_custom_tests(self):

    #     self.cache.set('item10', 'k')
    #     self.cache.set('item11', 'o')
    #     self.cache.set('item12', 'p')
    #     self.cache.set('item13', 'y')
    #     self.cache.set('item14', 'u')
    #     self.assertEqual(self.cache.get('item10'), 'k')
    #     self.cache.set('item15', 'Hey There')
    #     self.cache.set('item16', 'www.testing.com')
    #     self.cache.set('item17', 'object_unknown')
    #     self.cache.set('item18', 'k')
    #     self.cache.set('item19', 'o')
    #     self.cache.set('item20', 'p')
    #     self.cache.set('item21', 'p')
    #     self.cache.set('item21', 'updated the value')

    #     self.assertEqual(self.cache.get('item11'), 'o')
    #     self.assertEqual(self.cache.get('item15'), 'Hey There')
    #     self.assertEqual(self.cache.get('item10'), None)
    #     self.assertEqual(self.cache.get('item21'), 'updated the value')



if __name__ == '__main__':
    unittest.main()
