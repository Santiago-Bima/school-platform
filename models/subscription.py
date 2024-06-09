from user import User
from subject import Subject

class Suscription:
  def __init__ (self, subject=None, user=None, inscription_date='', id_suscription=0, marks=None):
    self._subject = subject if subject is not None else Subject()
    self._user = user if user is not None else User()
    self._inscription_date = inscription_date
    self._id_suscription = id_suscription
    self._marks = marks if marks is not None else []

  @property
  def subject(self):
    return self._subject
  
  @subject.setter
  def subject(self, subject):
    self._subject = subject
  
  @property
  def user(self):
    return self._user
  
  @user.setter
  def user(self, user):
    self._user = user
  
  @property
  def inscription_date(self):
    return self._inscription_date
  
  @inscription_date.setter
  def inscription_date(self, inscription_date):
    self._inscription_date = inscription_date
  
  @property
  def id_suscription(self):
    return self._id_suscription
  
  @id_suscription.setter
  def id_suscription(self, id_suscription):
    self._id_suscription = id_suscription
    
  @property
  def marks(self):
    return self._marks
  
  @marks.setter
  def marks(self, marks):
    self._marks = marks
    
  def add_mark(self, mark):
    self._marks.append(mark)
  
  def remove_mark(self, mark):
    if mark in self._marks:
      self._marks.remove(mark)
    