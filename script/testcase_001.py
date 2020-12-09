import unittest
from ddt import ddt,unpack,file_data,data
@ddt
class Test_001(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print('一个类只执行一遍')
    def setUp(self) -> None:
        print('一个用例执行一遍')
    def tearDown(self) -> None:
        print('一个用例执行一遍')
    def test_case01(self):
        print(1)
    def test_case02(self):
        print(2)
    @classmethod
    def tearDownClass(cls) -> None:
        print('一个类只执行一遍')
if __name__ == '__main':
    unittest.main()