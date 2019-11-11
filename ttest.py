import unittest
from tkinter import Tk
import assignment

root2 = Tk()
a = assignment.Student_info(root2)


class TestNewAlgorithm(unittest.TestCase):
    def test_sort(self):

        array_test = [('11', 'Babita', 'Lamjung', '9810133910', 'Hacking'),
                          ('12', 'Adana', 'Kathmandu', '9803635098', 'Security')]
        expected_result = [('12', 'Adana', 'Kathmandu', '9803635098', 'Security'),('11', 'Babita', 'Lamjung', '9810133910', 'Hacking'),]

        a.sortcombo.set('Id')
        ac_result=a.bubbleSort(array_test)
        self.assertEqual(expected_result,ac_result)


    def test_search(self):
        array_test = [('11', 'Babita', 'Lamjung', '9810133910', 'Hacking'),
                      ('12', 'Adana', 'Kathmandu', '9803635098', 'Security')]
        expected_result = [('11', 'Babita', 'Lamjung', '9810133910', 'Hacking')]
        a.searchentry.delete(0, 'end')
        a.searchentry.insert(0, 'Babita')
        ac_result = a.search(array_test)
        self.assertEqual(expected_result, ac_result)



if __name__ == '__main__':
    unittest.main()
