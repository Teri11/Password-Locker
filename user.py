class User:
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
     delete method deletes user details from a  saved account list
  
    '''
    User.user_list.remove(self)

    @classmethod
    def find_user(cls, username):
        for user in cls.user_list:
            if user.username == username:
                return  user

  