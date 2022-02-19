#!usr/bin/env python3.8  helps to know which python version you used.
import unittest
from user import User

class TestUser(unittest.TestCase):
   def setUp(self):
       """
         Test class that defines test cases for the user class behaviours.
        """
   
   
       self.new_user = User("Augustine","1234") # create user object
   
   def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_user.username,"Augustine")
        self.assertEqual(self.new_user.password,"1234")


if __name__ == '__main__':
    unittest.main()
  