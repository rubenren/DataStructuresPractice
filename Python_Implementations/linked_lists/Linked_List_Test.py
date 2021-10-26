from linked_list import LinkedList
import unittest

class TestingLinkedList(unittest.TestCase):

    def setUp(self):
        self.ll = LinkedList()

    @unittest.skip("Want to test if other tests are working")
    def test_size(self):
        self.assertEqual(self.ll.size(), 0)

        self.ll.push_back(1)
        self.ll.push_back(2)
        self.assertEqual(self.ll.size(), 2)

        self.ll.pop_back()
        self.assertEqual(self.ll.size(), 1)

    def test_empty(self):
        self.assertTrue(self.ll.is_empty())

        self.ll.push_back(1)
        self.assertFalse(self.ll.is_empty())

if __name__ == '__main__':
    unittest.main()