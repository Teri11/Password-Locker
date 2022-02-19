#!usr/bin/env python3.8  helps to know which python version you used.
import unittest
from user import User

class TestUser(unittest.TestCase):
  '''
  Test class thats defines test cases for the user class behavior

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
  '''

def setUp(self):
   '''
   Set up method to run before each test cases.
   '''
self.new_user = User("Augustine","1234") # create user object