class Credentials:
    '''
     credential class to assist creation of new instance of credentials
     '''

    credentials_list = []
  

    def _init_(self, username, password):
        '''
        To check if the credentials are initialized properly
        '''
        self.username = username
        self.password = password

    def save_credentials(self):
        '''
        test case to save new credentials
        '''
        Credentials.credentials_list.append(self)

    def delete_credentials(self):
        '''
        delete_credentials method deletes a saved credential from the list
        '''
        Credentials.credentials_list.remove(self)

    def display_credentials(self):
        '''
        Display created credentials
        '''
        Credentials.credentails_list.display(self)


@classmethod
def find_credentials(cls, credentials):
    for Credentials in cls.credentials_list:
        if user.credentials == credentials:
            return credentials
