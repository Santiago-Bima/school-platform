from services.user_service import UserService
from school_platform.repositories.user_repository import UserRepository
from school_platform.models.user import User
from school_platform.models.user_type import UserType
from school_platform.repositories.subscription_repository import SubscriptionRepository
from school_platform.repositories.subject_repository import SubjectRepository
from school_platform.models.subscription import Subscription


class UserServiceImpl(UserService):
  def __init__(self):
    self._repository = UserRepository()
    self._subscriptions_repository = SubscriptionRepository()
    self._subject_repository = SubjectRepository()
  
  def insert_user(self, user):
    user.username = user.username.lower()
    user.password = user.password.strip()
    
    existing_user = self._repository.get_user_by_name(user.username)
    if existing_user is not None:
      print('There is already a user with the same username. Please choose another one.')
      print()
      return False
    
    result = self._repository.insert(user)
    if result:
      print(f'The user: {user.username} has been logged in.')
      return result
    else:
      return False

  def get_by_username(self, username):
    username = username.lower()
    user = self._repository.get_user_by_name(username)
    
    if user is None:
      print("There isn't an user with that username")
      return False

    user = User(id=user[0], username=user[1], password=user[2], user_type=UserType(user[3]))
    
    return user

  def user_validation(self, username, password):
    username = username.lower()
    user = self.get_by_username(username)
    
    if not user:
      return False
    
    if user.password == password:
      user_dto = User(id=None, username=user.username, user_type=user.user_type)
      return user_dto
    
    print('The password is invalid')
    return False

  def get_all(self):
    rta = self._repository.get_all()
    users = []
    for i in rta:
      subscriptions = self._subscriptions_repository.get_by_user(i[0])
      subscriptions_objects = []
      for j in subscriptions:
        subject = self._subject_repository.get_by_id(j[1])
        subscription = Subscription(subject=subject)
        subscriptions_objects.append(subscription)
      user = User(username=i[1], user_type=UserType(i[3]).name, id=i[0], subscriptions=subscriptions_objects)
      users.append(user)
    
    return users

  def update(self, user, id):
    user.username = user.username.lower().strip()
    user.password = user.password.strip()
    
    existing_user = self._repository.get_user_by_name(user.username)
    if existing_user and existing_user[0] != id:
      print('There is already an user with the same username. Please choose another one.')
      print()
      return False
    
    result = self._repository.update(user, id)
    if result:
      print(f'The user: {user.username} has been updated.')
      return result
    else:
      return False
  
  def delete(self, id):
    if self._repository.delete(id):
      print('The user has been deleted')
    print()
  
  def get_by_id(self, id):
    user = self._repository.get_user_by_id(id)

    user = User(id=id, username=user[1], password=user[2], user_type=UserType(user[3]))
    
    return user