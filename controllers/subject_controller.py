from school_platform.services.implementations.subject_service_impl import SubjectServiceImpl
from school_platform.services.implementations.user_service_impl import UserServiceImpl
from school_platform.models.subject import Subject
from school_platform.utils.validate_date import date_validation
from school_platform.models.grade import Grade
from school_platform.controllers.mark_controller import MarkController

class SubjectController:
  def __init__(self):
    self._service = SubjectServiceImpl()
    self._user_serv = UserServiceImpl()
    self._mark_controller = MarkController()
  
  def get_all(self):
    print()
    subjects = self._service.get_all()
    for i in range(len(subjects)):
      print(str(i) + ' ' + subjects[i].__str__())
    
    return subjects
  
  def get_details(self):
    go_back = False
    subjects = self.get_all()
    print(f'{len(subjects)} Go back')
    print()
    while True:
      subject_nro = int(input('Which subject you want to see in detail? \n Choose a number: '))
      if subject_nro < 0 or subject_nro > len(subjects)-1:
        if subject_nro == len(subjects):
          go_back = True
          break
        print('The number must be any of the list')
        print()
        continue
      break
    if go_back:
      print()
      return
    
    rta = self._service.get_by_name_and_grade(subjects[subject_nro].name, subjects[subject_nro].grade.value)
    print()
    print(f'Subject: {rta.name}')
    for i in range(len(rta.subscriptions)):
      user = self._user_serv.get_by_id(rta.subscriptions[i].user.id)
      print(f'{i} -- {user.username} - Average mark: {rta.subscriptions[i].get_average()}')
    return rta.subscriptions
  
  def update(self):
    go_back = False
    subjects = self.get_all()
    print(f'{len(subjects)} Go back')
    print()
    while True:
      subject_nro = int(input('Which subject you want to edit? \n Choose a number: '))
      if subject_nro < 0 or subject_nro > len(subjects)-1:
        if subject_nro == len(subjects):
          go_back = True
          break
        print('The number must be any of the list')
        print()
        continue
      break
    if go_back:
      print()
      return
    
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
              print("The price can't be minor than 0")
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
  
  def insert(self):
    print()
    print('Insert new subject')
    
    while True:
      subject = Subject()
      
      while True:
        name = str(input('Insert the name: '))
        if name == '' or name.isspace():
          print("The name can't be empty")
          continue
        subject.name = name
        break
      
      while True:
        price = int(input('Insert the price: '))
        if price < 0:
          print("The price can't be minor than 0")
          continue
          
        subject.price = price
        break
      
      while True:
        begining_date = str(input('Insert the begining date (format: yyyy-MM-dd): '))
        if not date_validation(begining_date):
          print("The format is wrong")
          continue
          
        subject.begining_date = begining_date
        break
        
      while True:
        new_final_date = str(input('Insert the final date (format: yyyy-MM-dd): '))
        if not date_validation(new_final_date):
          print("The format is wrong")
          continue
          
        subject.final_date = new_final_date
        break
      
      while True:
        new_grade = int(input('Insert the grade (1 2 3): '))
        if new_grade < 1 or new_grade > 3:
          print("The number is wrong")
          continue
          
        subject.grade = Grade(new_grade)
        break
    
      rta = self._service.insert(subject)
      if rta:
        print()
        break
  
  def delete(self):
    go_back = False
    subjects = self.get_all()
    print(f'{len(subjects)} Go back')
    print()
    while True:
      subject_nro = int(input('Which subject you want to delete? \n Choose a number: '))
      if subject_nro < 0 or subject_nro > len(subjects)-1:
        if subject_nro == len(subjects):
          go_back = True
          break
        print('The number must be any of the list')
        print()
        continue
      break
    if go_back:
      print()
      return
    
    id = subjects[subject_nro].id
    self._service.delete(id)
  
  def manage_marks(self):
    subscriptions = self.get_details()
    print(f'{len(subscriptions)} Go back')
    print()
    
    while True:
      user_nro = int(input('Select the number of the user to edit their marks: '))
      
      if user_nro < 0 or user_nro > len(subscriptions) -1:
        if(user_nro == len(subscriptions)):
          print()
          return
        print('The number is wrong')

      marks = self._mark_controller.get_marks(subscriptions[user_nro].id_subscription)
      
      print()
      
      if not marks:
        while True:
          request = str(input('You want to add a new mark? y/n: ')).lower().strip()
          
          if request != 'y' and request != 'n':
            print('The answer is not correct, try again')
            print()
            continue
          break
        
        if request == 'n':
          break
        
        self._mark_controller.insert(subscriptions[user_nro].id_subscription) 
      else:
        while True:
          for i in range(len(marks)):
            print(f'{i} - {marks[i].date}: {marks[i].mark[0]}')
          print()
        
          request = int(input('What you want to do? \n Add mark (0) \n Edit mark (1) \n Delete mark (2) \n Go back (3) \n'))
          
          if request == 0:
            self._mark_controller.insert(subscriptions[user_nro].id_subscription)
          elif request == 1:
            print()
            while True:
              mark_nro = int(input(f'Which mark do you want to edit? (Go back: {len(marks)}): '))
              
              if mark_nro < 0 or mark_nro > len(marks)-1:
                if len(marks):
                  print()
                  break
                print('The number is wrong')
                print()
                continue
              self._mark_controller.update(marks[mark_nro])
              print()
              break
          elif request == 2:
            mark_nro = int(input(f'Which mark do you want to delete? (Go back: {len(marks)}): '))
              
            if mark_nro < 0 or mark_nro > len(marks)-1:
              if len(marks):
                print()
                break
              print('The number is wrong')
              print()
              continue
            self._mark_controller.delete(marks[mark_nro].id_mark)
            print()
            break
          elif request == 3:
            print()
            break
          else:
            print('The number is wrong, try again')
            print()
          break
      break