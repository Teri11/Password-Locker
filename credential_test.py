# !usr/bin/env python3.9  helps to know which python version you used.
import unittest  # Importing the unittest module
from credential import Credentials


class TestCredentials(unittest.TestCase):
    def setUp(self):
        """
          a method that defines test cases for the credentials class behaviours.
         """
        self.new_credentials = Credentials("Teri", "1234")

    def test_init(self):
        '''
         test case to know if credentials has been initialized well
         '''
        self.assertEqual(self.new_credentials.username, "Mweteri")
        self.assertEqual(self.new_credentials.password, "1234")

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
        test_credentials = Credentials("Teri", "1234")
        test_credential.save_credentials()
        self.new_credentials.delete_credential()
        self.assertEqual(len(Credentials.credentials_list), 1)

        def test_display_credentials(self):
            """
            A test to displays all credentials saved by user
            """
            self.assertEqual(Credentials.display_credentials(),
                             credentials.credentials_list)

        def test_save_multiple_credentials(self):
            '''
               test_save_multiple_credentials to check if we can save multiple credentials
               objects to our credentials_list
               '''
            self.new_credentials.save_credentials()
            test_credentials = Credentials("Teri", "1234")
            test_credentials.save_credentials()
            self.assertEqual(len(Credentials.credentials_list), 2)
        def test_find_credentials(self):
           '''
           find a user using username and display information
           '''
        self.new_credentials.save_credentials()
        test_credentials = Credentials("Teri", "1234")
        test_credentials.save_credentials()
        found_credentials = Credentials.find_credentials("Mweteri")
        self.assertEqual(found_credentials.username, self.new_credentials.username)


if __name__ == '__main__':
    unittest.main()
