from school_platform.services.mark_service import MarkService
from school_platform.repositories.mark_repository import MarkRepository
from school_platform.models.mark import Mark

class MarkServiceImpl(MarkService):
  def __init__(self):
    self._repository = MarkRepository()
  
  def get_by_subscription(self, id_subscription):
    marks = self._repository.get_by_subscription(id_subscription)
    
    if not marks:
      return False
    
    mark_objects = [Mark(id_subscription=i[3], mark=i[1], id_mark=i[0], date=i[2]) for i in marks]
    return mark_objects
  
  def insert(self, mark):
    
    marks = self._repository.get_by_date(mark.date)
    
    if marks:
      print('There is already a mark in the same day, choose another day')
      print()
      return False
    
    result = self._repository.insert(mark)
    if result:
      print('The mark has been registered')
      print()
    
    return result
    
  def update(self, mark, id_mark):
    rta = self._repository.update(mark, id_mark)
    
    if rta:
      print('The mark has been updated')
      
    return rta
  
  def delete(self, id_mark):
    return self._repository.delete(id_mark)