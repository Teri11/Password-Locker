#!usr/bin/env python3.8  helps to know which python version you used.
import unittest
from user import User


class TestUser(unittest.TestCase):
   def setUp(self):
       """
         Test class that defines test cases for the user class behaviours.
        """

       self.new_user = User("Augustine", "1234")  # create user object

   def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_user.username, "Augustine")
        self.assertEqual(self.new_user.password, "1234")

   def test_save_user(self):
      '''
        test_save_user  case to test if the user object is saved into the user list
      '''
      self.new_user.save_user()  # saving the new user
      self.assertEqual(len(User.user_list), 1)

   
   def test_save_multiple_contact(self):
     '''
    test_save_multiple_user to check if we can save multiple user objects to our user_list
    '''
     self.new_user.save_user()



      
      








if __name__ == '__main__':
    unittest.main()

    
  