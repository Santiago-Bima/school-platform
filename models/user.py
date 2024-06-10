from models.user_type import UserType

class User:
  def __init__(self, id=None, username=None, password=None, user_type=None, suscriptions=None):
    self._id = id
    self._username = username
    self._password = password
    self._user_type = user_type if user_type is not None else UserType.STUDENT
    self._suscriptions = suscriptions if suscriptions is not None else []

  def __str__ (self):
    return f'{self._username} - type: {self._user_type} - suscriptions: {self._suscriptions}'

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
  def suscriptions(self):
      return self._suscriptions

  @suscriptions.setter
  def suscriptions(self, suscriptions):
      self._suscriptions = suscriptions
      
  def add_suscription(self, suscription):
    self._suscriptions.append(suscription)
  
  def remove_suscription(self, suscription):
    if suscription in self._suscriptions:
      self._suscriptions.remove(suscription)