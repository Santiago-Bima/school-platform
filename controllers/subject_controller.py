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
    if not subjects:
      print("No subjects found.")
      return []
          
    for i in range(len(subjects)):
      print(str(i) + ' ' + subjects[i].__str__())
    
    return subjects
  
  def get_details(self):
    subjects = self.get_all()

    print(f"{len(subjects)} - Go back")
    while True:
      try:
        subject_index = int(input("Choose a subject number to view details: "))
        if subject_index < 0 or subject_index >= len(subjects):
          if subject_index == len(subjects):
            print("Going back.")
            print()
            return []
          print("Invalid number. Please choose from the list.")
          continue

        subject = subjects[subject_index]
        break
      except ValueError:
        print("Invalid input. Please enter a valid number.")
    
    rta = self._service.get_by_name_and_grade(subjects[subject_index].name, subjects[subject_index].grade.value)
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
      try:
        subject_nro = int(input('Which subject you want to edit? \n Choose a number: '))
        if subject_nro < 0 or subject_nro > len(subjects)-1:
          if subject_nro == len(subjects):
            print("Going back.")
            print()
            return []
          print('The number must be any of the list')
          print()
          continue
        break
      except ValueError:
        print("Invalid input. Please enter a valid number.")
    
    old_subject = self._service.get_by_name_and_grade(subjects[subject_nro].name, subjects[subject_nro].grade.value)
    
    print()
    print(f'Editing {old_subject.name} {old_subject.grade.name}')
    
    subject_updated = Subject(name=old_subject.name, price=old_subject.price, begining_date=old_subject.begining_date, final_date=old_subject.final_date, grade=old_subject.grade)
    
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
          try:
            new_price = int(input('Insert the price: '))
            if new_price < 0:
              print("The price can't be minor than 0")
              continue
              
            subject_updated.price = new_price
            break
          except ValueError:
            print("Invalid input. Please enter a valid number.")
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
          try:
            new_grade = int(input('Insert the grade (1 2 3): '))
            if new_grade < 1 or new_grade > 3:
              print("The number is wrong")
              continue
              
            subject_updated.grade = Grade(new_grade)
            break
          except ValueError:
            print("Invalid input. Please enter a valid number.")
      break
  
    self._service.update(subject_updated, old_subject.id)
    print()
  
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
        try:
          price = int(input('Insert the price: '))
          if price < 0:
            print("The price can't be minor than 0")
            continue
          
          subject.price = price
          break
        except ValueError:
          print("Invalid input. Please enter a valid number.")
      
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
        try:
          new_grade = int(input('Insert the grade (1 2 3): '))
          if new_grade < 1 or new_grade > 3:
            print("The number is wrong")
            continue
            
          subject.grade = Grade(new_grade)
          break
        except ValueError:
          print("Invalid input. Please enter a valid number.")
    
      rta = self._service.insert(subject)
      if rta:
        print()
        break
  
  def delete(self):
    subjects = self.get_all()
    print(f'{len(subjects)} Go back')
    print()
    while True:
      try:
        subject_nro = int(input('Which subject you want to delete? \n Choose a number: '))
        if subject_nro < 0 or subject_nro > len(subjects)-1:
          if subject_nro == len(subjects):
            print('Going back')
            print()
            return []
          print('The number must be any of the list')
          print()
          continue
        break
      except ValueError:
        print("Invalid input. Please enter a valid number.")
    
    id = subjects[subject_nro].id
    self._service.delete(id)
  
  def manage_marks(self):
    subscriptions = self.get_details()
    print(f'{len(subscriptions)} Go back')
    print()
    
    while True:
      try:
        user_nro = int(input('Select the number of the user to edit their marks: '))
      
        if user_nro < 0 or user_nro > len(subscriptions) -1:
          if(user_nro == len(subscriptions)):
            print('Going back')
            print()
            return []
          print('The number is wrong')
      
      except ValueError:
        print("Invalid input. Please enter a valid number.")

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
            print(f'{i} - {marks[i].date}: {marks[i].mark}')
          print()
        
          request = int(input('What you want to do? \n Add mark (0) \n Edit mark (1) \n Delete mark (2) \n Go back (3) \n'))
          
          if request == 0:
            self._mark_controller.insert(subscriptions[user_nro].id_subscription)
          elif request == 1:
            print()
            while True:
              try:
                mark_nro = int(input(f'Which mark do you want to edit? (Go back: {len(marks)}): '))
                
                if mark_nro < 0 or mark_nro > len(marks)-1:
                  if len(marks):
                    print('Going back')
                    print()
                    return []
                  print('The number is wrong')
                  print()
                  continue
                self._mark_controller.update(marks[mark_nro])
                print()
                break
              except ValueError:
                print("Invalid input. Please enter a valid number.")
          elif request == 2:
            try:
              mark_nro = int(input(f'Which mark do you want to delete? (Go back: {len(marks)}): '))
                
              if mark_nro < 0 or mark_nro > len(marks)-1:
                if len(marks):
                  print('Going back')
                  print()
                  return []
                print('The number is wrong')
                print()
                continue
              self._mark_controller.delete(marks[mark_nro].id_mark)
              print()
              break
            except ValueError:
              print("Invalid input. Please enter a valid number.")
          elif request == 3:
            print()
            break
          else:
            print('The number is wrong, try again')
            print()
          break
      break