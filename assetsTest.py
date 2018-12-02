import unittest

class assert_test(unittest.TestCase):

    @classmethod
    def setUp(self):
        print ("Yes")

    def test(self):
        x = False
        assert not x

    def test1(self):
        global a
        a = 1
        global b
        b = 2
        print ("In tet1")
        self.assertNotEqual(a,b)

    def tearDown(self):
        print ("destroy variable of setup class")

if __name__=="__main__":
    unittest.main(verbosity=2)