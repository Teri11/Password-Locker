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


def save_user(user):
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
  print("Hello,Welcome to Portal Accounts,What is your username?")
  username =input()

  print(f"Hello {username}.What do you want to do in the Portal?")
  print('\n')

  while True:
    print("Use the short codes here to access:cu-create new user,du-Display new user,fu-find user,login-log in to your account.ex-exit user list")
    short_code = input().lower()




































if __name__ == '__main__':

    main()



   

