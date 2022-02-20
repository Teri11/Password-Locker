#!/usr/bin/env python3.9
from user import User
from credentials import credentials

# user details


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

    # credentials details


def create_credentials(credentials):
    ''' 
    create new credentials
    '''
    new_credentials = (username, password)
    return new_credentials


def save_credentials(credentials):
    '''
    Function to save credentials
    '''
    credentials.save_credentials()


def delete_credentials(credentials):
    '''
    To delete credentials generated
    '''
    return credentials.delete_credentials(credentials)


def display_credentials():
    """
    It will display credentials
    """
    return credentials.display_credentials()


def find_by_credentials(credentials):
    """
    To find an account
    """
    return credentials.find_by_acc(credentials)


def main():
    print("Hello,Welcome to Portal Accounts,What is your Name?")
    username = input()

    print(
        f"Hello {username}.\nUse the codes below to make your experience better with us")
    print('\n')
    print('*'*100)
    while True:
        print("Use the short codes here to access:\ncu-create new user\ndu-Display new user\nfu-find user\nlog-login to your account\nex-exit user list")
        short_code = input().lower()
        if short_code == 'cu':
            print("Create New User😀 Account😀")
            print('*'*100)
            print("Enter your User Name ...")
            name = input()
            print("Enter password ...")
            password = input()
            # save_users(create_user(username,password))
            print('*'*100)
            print(f"Hello {username}\nUser Name:{name}.\nPortal Account has been created successfully.\nPlease proceed to login to access your account")
            print('*'*100)

        elif short_code == 'log' or short_code == 'du':
            print('*'*100)
            print("Enter your User Name...")
            username = input()
            print("Enter your password ...")
            password = input()
            print(f"{name} Logged in to Portal Account successfully")
            print('*'*100)

            while True:
                print("Use the short codes to check your credentials:gc-to generate credentials,sc-to save credentials,dp-to display credentials,ex-to exit")
                print('*'*100)
                short_code = input().lower()
                if short_code == "sc":
                    print("Username...")
                    username = input()
                    print("Password...")
                    password = input()
                    print('*'*100)
                    # save_credentials(create_credentials(username,password))
                    print(
                        f"Your username and password Portal Account details have been saved successfully.")
                    print("*"*100)
                     
                elif short_code == 'dp':
                       if display_credentials():
                        print("This is a list of your credentials")
                        print('*'*100)
                       for display in display_credentials():
                           print(
                        f"Username:{display.username} \n Password:{display.password}")
                       else:
                           print("Your credentials are not currently available")
                           print("--"*100)
                elif short_code == 'ex':
                      print("Logged out successfully")
                      print('*'*100)
                      break

                elif short_code =="gc":
                    print("User")
                    print("*"*100)
                    print ("Username:")
                    username = input()
                    print ("password:")
                    password = input()
                    print('*'*100)

                     
          







              


if __name__ == '__main__':

    main()
