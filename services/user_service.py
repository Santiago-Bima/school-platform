from abc import ABC, abstractmethod

class UserService(ABC):
  @abstractmethod
  def insert_user(self, user):
    pass
  
  @abstractmethod
  def get_by_username(self, username):
    pass
  
  @abstractmethod
  def get_all(self):
    pass
  
  @abstractmethod
  def user_validation(self, username, password):
    pass
  
  @abstractmethod
  def update(self, user, id):
    pass
  
  @abstractmethod
  def delete(self, id):
    pass
  
  @abstractmethod
  def get_by_id(self, id):
    pass