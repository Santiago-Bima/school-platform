import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from school_platform.controllers.user_controller import UserController
from school_platform.controllers.subject_controller import SubjectController
from school_platform.controllers.subscription_controller import SubscriptionController


def admin_actions(user_controller, subject_controller, username):
  log_out = False
  while True:
    if log_out:
      return 
    action = int(input('What you want to do? \n Subjects (0) \n Users (1) \n Log Out (2) \n Turn Off (3) \n'))
    print()
    
    if action == 0:
      while True:
    
        request = int(input('Options: \n See subjects (0) \n Edit subject (1) \n Insert subject (2) \n Delete subject (3) \n Marks menu (4) \n Go back (5) \n'))
        
        if request == 0:
          subject_controller.get_details()
          print()
        elif request == 1:
          subject_controller.update()
        elif request == 2:
          subject_controller.insert()
        elif request == 3:
          subject_controller.delete()
        elif request == 4:
          subject_controller.manage_marks()
        elif request == 5:
          print()
          break
        else:
          print('The number is wrong, try again')
    
    
    elif action == 1:
      while True:
        request = int(input('Options: \n See users (0) \n Edit user (1) \n Insert user (2) \n Delete user (3) \n Go back (4) \n'))
        
        if request == 0:
          user_controller.get_all()
        elif request == 1:
          if user_controller.update(username):
            log_out = True
            break
        elif request == 2:
          user_controller.insert()
        elif request == 3:
          if user_controller.delete(username):
            log_out = True
            break
        elif request == 4:
          print()
          break
        else:
          print('The number is wrong, try again')
    elif action == 2:
      return
    elif action == 3:
      return True
    else:
        print('The number is wrong, try again')

def students_actions(subscription_controller, subject_controller, username):
  log_out = False
  while True:
    if log_out:
      return 
    request = int(input('What you want to do? \n See subscriptions (0) \n Register in a subject (1) \n Delete a subscription (2) \n Log Out (3) \n Turn Off (4) \n'))
    print()

    if request == 0:
      subscription_controller.get_all(username)
      print()
    elif request == 1:
      subscription_controller.subscribe(username)
    elif request == 2:
      subscription_controller.desubscribe(username)
    elif request == 3:
      return
    elif request == 4:
      return True
    else:
      print('The number is wrong, try again')

def main():
  user_controller = UserController()
  subject_controller = SubjectController()
  subscription_controller = SubscriptionController()
  
  while True:
    log = user_controller.access()
    if not log:
      print('You have no more attemps, exiting programm')
      return
    
    print(f'Welcome {log.username}!!')
    print()

    if log.user_type.name == 'ADMIN':
      if admin_actions(user_controller, subject_controller, log.username):
        return
    else:
      if students_actions(subscription_controller, subject_controller, log.username):
        return
  
  
if __name__ == "__main__":
  main()