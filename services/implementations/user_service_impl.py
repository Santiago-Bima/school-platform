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
    if existing_user:
      print('There is already a user with the same username. Please choose another one.')
      print()
      return False
    
    result = self._repository.insert(user)
    if result:
      print(f'The user: {user.username} has been logged in.')
    
    return result

  def get_by_username(self, username):
    username = username.lower()
    user_data = self._repository.get_user_by_name(username)
    if not user_data:
      print("There isn't a user with that username")
      print()
      return False

    return User(id=user_data[0], username=user_data[1], password=user_data[2], user_type=UserType(user_data[3]))

  def user_validation(self, username, password):
    username = username.lower()
    user = self.get_by_username(username)
    
    if not user or user.password != password:
      print('Invalid username or password')
      return False

    return User(id=None, username=user.username, user_type=user.user_type)

  def get_all(self):
    users_data = self._repository.get_all()
    users = [
      User(
        id=user_data[0], username=user_data[1], user_type=UserType(user_data[3]).name,
        subscriptions=[
          Subscription(subject=self._subject_repository.get_by_id(sub_data[1]))
          for sub_data in self._subscriptions_repository.get_by_user(user_data[0])
        ]
      )
      for user_data in users_data
    ]
    return users

  def update(self, user, id):
    user.username = user.username.lower().strip()
    user.password = user.password.strip()

    existing_user = self._repository.get_user_by_name(user.username)
    if existing_user and existing_user[0] != id:
      print('There is already a user with the same username. Please choose another one.')
      print()
      return False

    result = self._repository.update(user, id)
    if result:
      print(f'The user: {user.username} has been updated.')
    return result
  
  def delete(self, id):
    if self._repository.delete(id):
      print('The user has been deleted')
    print()
  
  def get_by_id(self, id):
    user_data = self._repository.get_user_by_id(id)
    if not user_data:
      print("User not found")
      return None

    return User(id=id, username=user_data[1], password=user_data[2], user_type=UserType(user_data[3]))