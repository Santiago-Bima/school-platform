from school_platform.models.grade import Grade

class Subject:
  def __init__(self, id=0, name='', price=0, begining_date='', final_date='', grade=None, suscriptions=None):
    self._id = id
    self._name = name
    self._price = price
    self._begining_date = begining_date
    self._final_date = final_date
    self._grade = grade if grade is not None else Grade.FIRST
    self._suscriptions = suscriptions if suscriptions is not None else []

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