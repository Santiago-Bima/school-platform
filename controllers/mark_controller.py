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
  
  def update(self, mark):
    print(mark)
    print()
    
    mark.mark = mark.mark[0]
    while True:
      while True:
        change_mark = str(input('New mark? y/n: ')).lower().strip()
        if change_mark != 'y' and change_mark != 'n':
          print('The input is wrong, try again')
          print()
          continue
        
        if change_mark == 'y':
          while True:
            new_mark = int(input('Insert the new mark: '))
            if new_mark < 1 or new_mark > 10:
              print("The mark must be between 1 and 10")
              continue
            mark.mark = new_mark
            break
        break
      
      print()
      while True:
        change_date = str(input('New date? y/n: ')).lower().strip()
        if change_date != 'y' and change_date != 'n':
          print('The input is wrong, try again')
          print()
          continue
        
        if change_date == 'y':
          while True:
            new_date = str(input('Insert the new date: '))
            if not date_validation(new_date):
              print("The format is wrong")
              continue
            mark.date = new_date
            break
        break
      
      rta = self._mark_service.update(mark, mark.id_mark)
      if rta:
        print()
        break
  
  def delete(self):
    pass