# !usr/bin/env python3.9  helps to know which python version you used.
import unittest #importing unittestb module
from credentials import credentials
class TestCredentials(unittest.TestCase):
     def setUp(self):
       """
         a method that defines test cases for the credentials class behaviours.
        """
       self.new_credentials = credentials("Augustine","1234")
        
