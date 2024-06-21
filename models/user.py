from models.user_type import UserType

class User:
  def __init__(self, id=None, username=None, password=None, user_type=None, subscriptions=None):
    self._id = id
    self._username = username
    self._password = password
    self._user_type = user_type if user_type is not None else UserType.STUDENT
    self._subscriptions = subscriptions if subscriptions is not None else []

  def __str__ (self):
    subjects = []
    for i in self._subscriptions:
      subjects.append(i.subject[1])
    return f'{self._username} - type: {self._user_type} - subscriptions: {subjects}'

  @property
  def id(self):
    return self._id

  @id.setter
  def id(self, id):
    self._id = id
  
  @property
  def username(self):
    return self._username
  
  @username.setter
  def username(self, username):
    self._username = username
    
  @property
  def password(self):
    return self._password
  
  @password.setter
  def password(self, password):
    self._password = password
    
  @property
  def user_type(self):
    return self._user_type
  
  @user_type.setter
  def user_type(self, user_type):
    self._user_type = user_type
  
  @property
  def subscriptions(self):
      return self._subscriptions

  @subscriptions.setter
  def subscriptions(self, subscriptions):
      self._subscriptions = subscriptions
      
  def add_subscription(self, subscription):
    self._subscriptions.append(subscription)
  
  def remove_subscription(self, subscription):
    if subscription in self._subscriptions:
      self._subscriptions.remove(subscription)