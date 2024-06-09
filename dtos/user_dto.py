from school_platform.models.user_type import UserType

class UserDto():
  def __init__(self, id=0, username='', user_type='', suscriptions=None):
    self._id = id
    self._username = username
    self._user_type = user_type
    self._suscriptions = suscriptions if suscriptions is not None else []
  
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
  
  def __str__(self):
    return f"{self._username} - {self._user_type} - {self._suscriptions}"