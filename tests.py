import unittest
from hashmap import Hashmap

class TestHashmap(unittest.TestCase):
    
    def test_get_with_non_existing_key(self):
        hashmap = Hashmap(10)
        self.assertEqual(hashmap.get("kajshdahsjkas"), None)  

    def test_insert_and_get(self):
        hashmap = Hashmap(10)
        hashmap.set("pi", 3.14)
        self.assertEqual(hashmap.get("pi"), 3.14)
        self.assertEqual(hashmap.count, 1)

    def test_collision(self):
        hashmap = Hashmap(10)
        hashmap.set("pi", 3.14)
        hashmap.set("wysi", 727)
        hashmap.set("www", 111)
        hashmap.set("awdsd", 27)
        hashmap.set("xd", 2)
        hashmap.set("xyz", 0)
        self.assertEqual(hashmap.count, 6)
        self.assertEqual(hashmap.size, 10)
        self.assertEqual(hashmap.get("pi"), 3.14)
        self.assertEqual(hashmap.get("wysi"), 727)
        self.assertEqual(hashmap.get("www"), 111)
        self.assertEqual(hashmap.get("awdsd"), 27)
        self.assertEqual(hashmap.get("xd"), 2)
        self.assertEqual(hashmap.get("xyz"), 0)

    def test_update(self):
        hashmap = Hashmap(10)
        hashmap.set("pi", 3.14)
        hashmap.set("pi", 3.1415926)
        self.assertEqual(hashmap.count, 1)
        self.assertEqual(hashmap.get("pi"), 3.1415926)
    
    def test_remove(self):
        hashmap = Hashmap(10)
        hashmap.set("pi", 3.14)
        self.assertTrue(hashmap.remove("pi"))
        self.assertEqual(hashmap.count, 0)
        self.assertIsNone(hashmap.get("pi"))

    def test_remove_with_non_existing_key(self):
        hashmap = Hashmap(10)
        self.assertEqual(hashmap.count, 0)
        self.assertFalse(hashmap.remove("kajshdahsjkas"))  
    
    def test_rehashing(self):
        hashmap = Hashmap(2)
        hashmap.set("pi", 3.14)
        hashmap.set("wysi", 727)
        self.assertEqual(hashmap.size, 4)
        self.assertEqual(hashmap.count, 2)
        self.assertEqual(hashmap.get("pi"), 3.14)
        self.assertEqual(hashmap.get("wysi"), 727)        

if __name__ == '__main__':
    unittest.main()