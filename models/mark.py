class Mark:
  def __init__(self, id_mark=0, id_suscription=0, mark=0, date=''):
    self._id_mark = id_mark
    self._id_suscription = id_suscription
    self._mark = mark,
    self._date = date
  
  @property
  def id_mark(self):
    return self._id_mark

  @id_mark.setter
  def id_mark(self, id):
    self._id_mark = id
  
  @property
  def id_suscription(self):
    return self._id_suscription

  @id_suscription.setter
  def id_suscription(self, id):
    self._id_suscription = id
  
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