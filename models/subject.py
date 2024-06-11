from school_platform.models.grade import Grade

class Subject:
  def __init__(self, id=None, name=None, price=None, begining_date=None, final_date=None, grade=None, subscriptions=None):
    self._id = id
    self._name = name
    self._price = price
    self._begining_date = begining_date
    self._final_date = final_date
    self._grade = grade if grade is not None else Grade.FIRST
    self._subscriptions = subscriptions if subscriptions is not None else []

  def __str__(self):
    return f'{self._name} {self._grade.name}: ${self._price} ({self._begining_date} - {self._final_date})'
    
  @property
  def id(self):
      return self._id
      
  @id.setter
  def id(self, id):
      self._id = id

  @property
  def name(self):
      return self._name

  @name.setter
  def name(self, name):
      self._name = name

  @property
  def price(self):
      return self._price

  @price.setter
  def price(self, price):
      self._price = price

  @property
  def begining_date(self):
      return self._begining_date

  @begining_date.setter
  def final_date(self, begining_date):
      self._begining_date = begining_date
      
  @property
  def final_date(self):
      return self._final_date

  @final_date.setter
  def final_date(self, final_date):
      self._final_date = final_date

  @property
  def grade(self):
      return self._grade

  @grade.setter
  def grade(self, grade):
      self._grade = grade
      
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