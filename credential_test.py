# !usr/bin/env python3.9  helps to know which python version you used.
import unittest  # Importing the unittest module
from credential import Credentials


class TestCredentials(unittest.TestCase):
    def setUp(self):
        """
          a method that defines test cases for the credentials class behaviours.
         """
        self.new_credentials = Credentials("Teri","1234")

    def test_init(self):
        '''
         test case to know if credentials has been initialized well
         '''
        self.assertEqual(self.new_credentials.username,"Teri")
        self.assertEqual(self.new_credentials.password,"1234")

    def test_save_credentials(self):
        '''
        To test if credentials are saved in credential list
        '''
        self.new_credentials.test_save_credentials
        self.assertEqual(len(Credentials.credentials_list), 1)

    def tearDown(self):
        '''
        A test to clean up after each test case has run.
        '''
        Credentials.credentials_list = []
   
    def test_delete_credentials(self):
      '''
      Test method to delete our credentials from credentials_list
      '''
      self.new_credentials.save_credentials()
      test_credentials=Credentials("Teri", "1234")
      test_credential.save_credentials()
      self.new_credentials.delete_credential()
      self.assertEqual(len(Credentials.credentials_list),1)


if __name__ == '__main__':
    unittest.main()
