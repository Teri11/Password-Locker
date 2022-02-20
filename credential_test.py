# !usr/bin/env python3.9  helps to know which python version you used.
import unittest  # importing unittestb module
from credentials import credentials


class TestCredentials(unittest.TestCase):
    def setUp(self):
        """
          a method that defines test cases for the credentials class behaviours.
         """
        self.new_credentials = credentials("Augustine", "1234")

    def test_init(self):
        '''
         test case to know if credentials has been initialized well
         '''
        self.assertEqual(self.new_credentials.username,"Augustine")
        self.assertEqual(self.new_credentials.password,"1234")