from school_platform.services.implementations.user_service_impl import UserServiceImpl
from school_platform.models.user import User
from school_platform.models.user_type import UserType

class UserController:
  def __init__(self):
    self._service = UserServiceImpl()
  
  def access(self):
    print('Log In: ')
    print('------------')
    
    attemps = 0
    
    while True:
      if attemps == 3:
        return False
      
      username = str(input('Username: '))
      psw = str(input('User password: '))
      print()
      
      validation = self._service.user_validation(username, psw)
      
      if not validation:
        attemps += 1
      else:
        return validation
  
  def insert(self):
    print()
    print('Insert new user')
    while True:
      username = str(input('Insert the username: '))
      if username == '' or username.isspace():
        print("The username can't be empty")
        continue
      
      psw = str(input('Insert the password: '))
      if psw == '' or psw.isspace() or len(psw) < 6 or len(psw) > 8:
        print("The password can't be empty, and must be between 6 and 8 chars")
        continue
      
      while True:
        usr_type = int(input("It's Student (1) or Admin (2): "))
        if usr_type < 1 or usr_type > 2:
          print("The number it's wrong, try again")
          print()
        break
    
      user = User(username=username, password=psw, user_type=UserType(usr_type))
      rta = self._service.insert_user(user)
      if rta:
        print()
        break
  
  def get_all(self):
    users = self._service.get_all()
    for i in users:
      print(i.__str__())
    print()
  
  def update(self, usr_name):
    print()
    print('Edit user')
    
    while True:
      username = str(input('Insert the username: '))
      if username == '' or username.isspace():
        print("The username can't be empty")
        continue
      
      user = self._service.get_by_username(username)
      if not user:
        continue
      
      break
    
    print()
    print(f'Editing {username}')
    user_updated = User(username=user.username, password=user.password, user_type=user.user_type)
    while True:
      while True:
        change_username = str(input('New username? y/n: '))
        change_username = change_username.lower().strip()
        if change_username != 'y' and change_username != 'n':
          print('The input is wrong, try again')
          print()
          continue
        
        if change_username == 'y':
          while True:
            new_username = str(input('Insert the new username: '))
            if new_username == '' or new_username.isspace():
              print("The username can't be empty")
              continue
            user_updated.username = new_username
            break
        break
      
      while True:
        change_psw = str(input('New password? y/n: '))
        change_psw = change_psw.lower().strip()
        if change_psw != 'y' and change_psw != 'n':
          print('The input is wrong, try again')
          print()
          continue
      
        if change_psw == 'y':
          while True:
            new_psw = str(input('Insert the password: '))
            if new_psw == '' or new_psw.isspace() or len(new_psw) < 6 or len(new_psw) > 8:
              print("The password can't be empty, and must be between 6 and 8 chars")
              continue
              
            user_updated.password = new_psw
            break
        break
      
      while True:
        change_type = str(input('Change user type? y/n: '))
        change_type = change_type.lower().strip()
        if change_type != 'y' and change_type != 'n':
          print('The input is wrong, try again')
          print()
          continue
      
        if change_type == 'y':
          if user.user_type.value == 1:
            new_usr_type = 2
          else:
            new_usr_type = 1
          
          user_updated.user_type = UserType(new_usr_type)  
        break
    
      rta = self._service.update(user_updated, user.id)
      if rta:
        print()
        if usr_name == user.username:
          return True
        break
  
  def delete(self, usr_name):
    print()
    users = self._service.get_all()
    for i in range(len(users)):
      print(f"{i} - {users[i].username}")
    print()
    
    while True:
      nro = int(input('Which user you want to delete? (insert number): '))
      if nro < -1 or nro > len(users):
        print('It must be a number of the list')
        continue
      break 
    
    id = users[nro].id
    self._service.delete(id)
    if usr_name == users[nro].username:
      return True