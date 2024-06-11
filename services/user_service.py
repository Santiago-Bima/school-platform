from abc import ABC, abstractclassmethod

class UserService(ABC):
  @abstractclassmethod
  def insert_user(self, user):
    pass
  
  @abstractclassmethod
  def get_by_username(self, username):
    pass
  
  @abstractclassmethod
  def get_all(self):
    pass
  
  @abstractclassmethod
  def user_validation(self, username, password):
    pass
  
  @abstractclassmethod
  def update(self, user, id):
    pass
  
  @abstractclassmethod
  def delete(self, id):
    pass
  
  @abstractclassmethod
  def get_by_id(self, id):
    pass