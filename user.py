class user:
  '''
  class that generates an instance of user
  '''
  

user_list=[]

def __init__(self,username,password):
  '''
  a method that defines the properties on the class object
  '''
  
  self.username = username
  self.password = password

  def save_user(self):
     '''
        test case to check if the user is added to the user list
      '''
  User.user_list.append(self)

  def delete_user(self):
    '''
    to check if user details is deleted
    '''
    User.user_list.remove(self)