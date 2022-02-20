class credentials:
    '''
     credential class to assist creation of new instance of credentials
     '''

    credentials_list = []

    def __init__(self, username, password):
        '''
        To check if the credentials are initialized properly
        '''
        self.username = username
        self.password = password

    def save_credentials(self):
        '''
        test case to save new credentials
        '''
        credentials.credentials_list.append(self)

    def delete_credentials(self):
        '''
        delete_credentials method deletes a saved credential from the list
        '''
        credentials.credentials_list.remove(self)
    @classmethod
    def display_credentials(cls):
        '''
        Display created credentials
        '''
        
        return cls.credentials_list


    @classmethod
    def find_credentials(cls, username):
      for user in cls.credentials_list:
        if user.username == username:
            return user
        return False
