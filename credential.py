class Credentials:
  '''
   credential class to assist creation of new instance of credentials
   '''

  credentials_list = [] 
  
  def _init_(self,username,password):
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