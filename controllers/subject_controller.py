from school_platform.services.implementations.subject_service_impl import SubjectServiceImpl
from school_platform.services.implementations.user_service_impl import UserServiceImpl
from school_platform.models.subject import Subject
from school_platform.utils.validate_date import date_validation
from school_platform.models.grade import Grade

class SubjectController:
  def __init__(self):
    self._service = SubjectServiceImpl()
    self._user_serv = UserServiceImpl()
  
  def get_all(self):
    print()
    subjects = self._service.get_all()
    for i in range(len(subjects)):
      print(str(i) + ' ' + subjects[i].__str__())
    print()
    
    return subjects
  
  def get_details(self):
    subjects = self.get_all()
    while True:
      subject_nro = int(input('Which subject you want to see in detail? \n Choose a number: '))
      if subject_nro < 0 or subject_nro > len(subjects)-1:
        print('The number must be any of the list')
        print()
        continue
      break
    
    rta = self._service.get_by_name_and_grade(subjects[subject_nro].name, subjects[subject_nro].grade.value)
    print()
    print(f'Subject: {rta.name}')
    for i in rta.subscriptions:
      user = self._user_serv.get_by_id(i.user.id)
      print(f'-- {user.username} - Average mark: {i.get_average()}')
    print()
  
  
  def update(self):
    subjects = self.get_all()
    while True:
      subject_nro = int(input('Which subject you want to edit? \n Choose a number: '))
      if subject_nro < 0 or subject_nro > len(subjects)-1:
        print('The number must be any of the list')
        print()
        continue
      break
    
    old_subject = self._service.get_by_name_and_grade(subjects[subject_nro].name, subjects[subject_nro].grade.value)
    
    print()
    print(f'Editing {old_subject.name} {old_subject.grade.name}')
    
    subject_updated = Subject(name=old_subject.name, price=old_subject.price, begining_date=old_subject.begining_date, final_date=old_subject.final_date, grade=old_subject.grade)
    
    while True:
      while True:
        change_name = str(input('New name? y/n: '))
        change_name = change_name.lower().strip()
        if change_name != 'y' and change_name != 'n':
          print('The input is wrong, try again')
          print()
          continue
        
        if change_name == 'y':
          while True:
            new_name = str(input('Insert the new name: '))
            if new_name == '' or new_name.isspace():
              print("The name can't be empty")
              continue
            subject_updated.name = new_name
            break
        break
      
      while True:
        change_price = str(input('New price? y/n: '))
        change_price = change_price.lower().strip()
        if change_price != 'y' and change_price != 'n':
          print('The input is wrong, try again')
          print()
          continue
      
        if change_price == 'y':
          while True:
            new_price = int(input('Insert the price: '))
            if new_price < 0:
              print("The password can't minor than 0")
              continue
              
            subject_updated.price = new_price
            break
        break
      
      while True:
        change_begining_date = str(input('Change begining date? y/n: '))
        change_begining_date = change_begining_date.lower()
        if change_begining_date != 'y' and change_begining_date != 'n':
          print('The input is wrong, try again')
          print()
          continue
      
        if change_begining_date == 'y':
          while True:
            new_begining_date = str(input('Insert the date (format: yyyy-MM-dd): '))
            if not date_validation(new_begining_date):
              print("The format is wrong")
              continue
              
            subject_updated.begining_date = new_begining_date
            break
        break
        
      while True:
        change_final_date = str(input('Change final date? y/n: '))
        change_final_date = change_final_date.lower()
        if change_final_date != 'y' and change_final_date != 'n':
          print('The input is wrong, try again')
          print()
          continue
      
        if change_final_date == 'y':
          while True:
            new_final_date = str(input('Insert the date (format: yyyy-MM-dd): '))
            if not date_validation(new_final_date):
              print("The format is wrong")
              continue
              
            subject_updated.final_date = new_final_date
            break
        break
      
      while True:
        change_grade = str(input('Change grade? y/n: '))
        change_grade = change_grade.lower()
        if change_grade != 'y' and change_grade != 'n':
          print('The input is wrong, try again')
          print()
          continue
      
        if change_grade == 'y':
          while True:
            new_grade = int(input('Insert the grade (1 2 3): '))
            if new_grade < 1 or new_grade > 3:
              print("The number is wrong")
              continue
              
            subject_updated.grade = Grade(new_grade)
            break
        break
    
      rta = self._service.update(subject_updated, old_subject.id)
      if rta:
        print()
        break