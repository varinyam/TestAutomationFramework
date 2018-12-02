import unittest

class test_case_demo(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print ('#' *30)
        print ("From main setup method befoe all test")

    # def setUp(self):
    #     print ("Will run first before ant test case")

    def test_methodA(self):
        global a
        a=1
        global b
        b=2
        print ("Runnning A:{0}".format(a+b))

    def test_methodB(self):

        print ("Running B:{0}".format(a*b))

    # def tearDown(self):
    #     print ("Cleaning the values which are created by setup method and no longer needed for testing")

    @classmethod
    def tearDownClass(cls):
        print ('^' * 30)
        print ("Will run after every thing")

if __name__=="__main__":
  unittest.main(verbosity=2)