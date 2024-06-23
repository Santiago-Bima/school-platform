class Mark:
  def __init__(self, id_mark=None, id_subscription=None, mark=None, date=None):
    self._id_mark = id_mark
    self._id_subscription = id_subscription
    self._mark = mark,
    self._date = date
  
  def __str__(self):
    return f'{self._date}: {self._mark[0]}'
  
  @property
  def id_mark(self):
    return self._id_mark

  @id_mark.setter
  def id_mark(self, id):
    self._id_mark = id
  
  @property
  def id_subscription(self):
    return self._id_subscription

  @id_subscription.setter
  def id_subscription(self, id):
    self._id_subscription = id
  
  @property
  def mark(self):
    return self._mark
  
  @mark.setter
  def mark(self, mark):
    self._mark = mark
  
  @property
  def date(self):
    return self._date
  
  @date.setter
  def date(self, date):
    self._date = date
    