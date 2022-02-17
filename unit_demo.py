

import unittest
class UnitDemo(unittest.TestCase): #类名继承
    def test_01(self):             #函数名称必须以test开头
        print('这是测试用例1')

if __name__ == '__main__':
    unittest.main()
