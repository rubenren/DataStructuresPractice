from linked_list import LinkedList
import unittest

class TestingLinkedList(unittest.TestCase):

    def setUp(self):
        self.ll = LinkedList()

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

    def test_value_at(self):
        for i in range(5):
            self.ll.push_back(1)
        self.ll.push_back(20)
        for i in range(5):
            self.ll.push_back(1)

        self.assertEqual(self.ll.value_at(5), 20)

    def test_push_front(self):
        for i in range(5):
            self.ll.push_front(i)

        self.assertEqual(self.ll.value_at(0), 4)

    def test_pop_front(self):
        self.ll.push_back(1)
        self.ll.push_back(2)
        self.ll.push_back(3)

        self.assertEqual(self.ll.pop_front(), 1)

    def test_push_back(self):
        self.ll.push_back(1)
        self.ll.push_back(2)
        self.ll.push_back(3)

        self.assertEqual(self.ll.value_at(0), 1)
        self.assertEqual(self.ll.value_at(2), 3)

    def test_pop_back(self):
        self.ll.push_back(1)
        self.ll.push_back(2)
        self.ll.push_back(3)

        self.assertEqual(self.ll.pop_back(), 3)
        self.assertEqual(self.ll.pop_back(), 2)
        self.assertEqual(self.ll.pop_back(), 1)

    def test_front(self):
        self.ll.push_back(1)
        self.ll.push_back(2)
        self.ll.push_back(3)

        self.assertEqual(self.ll.front(), 1)

    def test_back(self):
        self.ll.push_back(1)
        self.ll.push_back(2)
        self.ll.push_back(3)

        self.assertEqual(self.ll.back(), 3)

    def test_insert(self):
        self.ll.push_back(1)
        self.ll.push_back(2)
        self.ll.push_back(3)

        self.ll.insert(1, 25)
        self.assertEqual(self.ll.value_at(1), 25)

    def test_erase(self):
        self.ll.push_back(1)
        self.ll.push_back(2)
        self.ll.push_back(3)

        self.ll.erase(1)

        self.assertEqual(self.ll.size(), 2)
        self.assertEqual(self.ll.value_at(1), 3)

    def test_val_n_from_end(self):
        self.ll.push_back(1)
        self.ll.push_back(2)
        self.ll.push_back(3)
        self.ll.push_back(5)

        self.assertEqual(self.ll.value_n_from_end(1), 3)

    def test_reverse(self):
        self.ll.push_back(1)
        self.ll.push_back(2)
        self.ll.push_back(3)

        self.ll.reverse()

        self.assertEqual(self.ll.front(), 3)

    def test_remove_value(self):
        self.ll.push_back(1)
        self.ll.push_back(2)
        self.ll.push_back(3)
        self.ll.push_back(5)
        self.ll.push_back(3)

        self.ll.remove_value(3)

        self.assertEqual(self.ll.size(), 4)
        self.assertEqual(self.ll.value_at(2), 5)

if __name__ == '__main__':
    unittest.main()