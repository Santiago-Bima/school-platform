from school_platform.services.implementations.subject_service_impl import SubjectServiceImpl
from school_platform.services.implementations.user_service_impl import UserServiceImpl

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