#!/usr/bin/env python3.9
from user import User
from credentials import credentials

#user details
def create_user(username, password):
    '''
    Creating new user
    '''
    new_user = (username, password)
    return new_user


def save_users(user):
    '''
       To save user details
    '''
    user.save_user()

def delete_user(user):
    '''
       Function will delete user info
    '''
    user.delete_user()

def find_user(user):
    '''
    To find user
    '''
    user.find_user()


def main():
  print("Hello,Welcome to Portal Accounts,What is your Name?")
  username =input()

  print(f"Hello {username}.Use the codes below to make your experience better with us")
  print('\n')

  while True:
    print("Use the short codes here to access:cu-create new user\ndu-Display new user\nfu-find user\nlogin-log in to your account\nex-exit user list")
    short_code = input().lower()
    if short_code =='cu':
      print("Create New User😀 Account😀")
      print('*'*100)
      print("Enter your User Name ...")
      name = input()
      print("Enter password ...")
      password = input()
      save_users(create_user(name,password))
      
      print('*'*100)
      print(f"Hello {username}\nUser Name:{name}.\nPortal Account has been created successfully.\nPlease proceed to login to access your account")
      print('*'*100)
      
    elif short_code == 'log' or short_code == 'du':
      print('*'*100)
      print("Enter your User Name...")
     
     
      



if __name__ == '__main__':

    main()



   

