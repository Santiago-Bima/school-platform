from school_platform.services.implementations.mark_service_impl import MarkServiceImpl
from school_platform.models.mark import Mark
from school_platform.utils.validate_date import date_validation

class MarkController:
  def __init__(self):
    self._mark_service = MarkServiceImpl()
  
  def get_marks(self, id_subscription):
    return self._mark_service.get_by_subscription(id_subscription)
  
  def insert(self, id_subscription):
    print()
    
    mark = Mark(id_subscription = id_subscription)
    
    while True:
      number = int(input('Insert the mark: '))
      
      if number < 1 or number > 10:
        print('The mark must be between 1 and 10')
        print()
        continue
      
      mark.mark = number
      break
    
    while True:
      date = str(input('Insert the date (format: yyyy-MM-dd): '))
      if not date_validation(date):
        print("The format is wrong")
        continue
        
      mark.date = date
      break
    
    self._mark_service.insert(mark)
    print()
  
  def update(self):
    pass
  
  def delete(self):
    pass