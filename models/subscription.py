from school_platform.models.user import User
from school_platform.models.subject import Subject

class Subscription:
  def __init__ (self, subject=None, user=None, inscription_date=None, id_subscription=None, marks=None):
    self._subject = subject if subject is not None else Subject()
    self._user = user if user is not None else User()
    self._inscription_date = inscription_date
    self._id_subscription = id_subscription
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
  def id_subscription(self):
    return self._id_subscription
  
  @id_subscription.setter
  def id_subscription(self, id_subscription):
    self._id_subscription = id_subscription
    
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
  
  def get_average(self):
    total = 0
    for i in self._marks:
      total += i.mark[0]
    if len(self._marks) == 0:
      rta = 'There are no marks'
    else:
      rta = str(round(total/len(self._marks)))
    return rta

  def __str__ (self):
    return f'{self.subject.name} {self.subject.grade.name}: ${self.subject.price} - {self.inscription_date} Average: {self.get_average()}'