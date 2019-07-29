import unittest
class test:
    def a(self):
        return True

    def b(self):
        if self.a() is not False:
            print("Ok")

A=test()
A.b()


if __name__=="__main__":
    unittest.main()

