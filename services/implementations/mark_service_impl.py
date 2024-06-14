from school_platform.services.mark_service import MarkService
from school_platform.repositories.mark_repository import MarkRepository
from school_platform.models.mark import Mark

class MarkServiceImpl(MarkService):
  def __init__(self):
    self._repository = MarkRepository()
  
  def get_by_subscription(self, id_subscription):
    marks = self._repository.get_by_subscription(id_subscription)
    
    if not marks:
      print("There aren't any marks")
      return False
    
    mark_objects = []
    for i in marks:
      mark = Mark(id_subscription = i[0], mark=i[1], id_mark=i[2], date=i[3])
      mark_objects.append(mark)
      
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
    
    return False  
    
    