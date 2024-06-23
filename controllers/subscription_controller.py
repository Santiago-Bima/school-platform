from school_platform.services.implementations.subscription_repository_impl import SubscriptionServiceImpl
from school_platform.services.implementations.mark_service_impl import MarkServiceImpl
from school_platform.services.implementations.subject_service_impl import SubjectServiceImpl
from school_platform.services.implementations.user_service_impl import UserServiceImpl
from school_platform.models.subscription import Subscription

class SubscriptionController:
  def __init__(self):
    self._service = SubscriptionServiceImpl()
    self._marks_service = MarkServiceImpl()
    self._subjects_service = SubjectServiceImpl()
    self._user_service = UserServiceImpl()
    
  def get_all(self, username):
    subscriptions = self._service.get_by_user(username)
    
    if not subscriptions:
      pass
    
    for i in range(len(subscriptions)):
      print(f'{i} {subscriptions[i].__str__()}')
      marks = self._marks_service.get_by_subscription(subscriptions[i].id_subscription)
      if marks:
        for j in marks:
          print(f' -- {j.__str__()}')
    
    return subscriptions
  
  def subscribe(self, username):
    subjects = self._subjects_service.get_all()
    remaining_subjects = []
    subscriptions = self._service.get_by_user(username)

    cont = -1
    for i in subjects:
      equal = False
      for j in subscriptions:
        if i.id == j.subject.id:
          equal = True
          break
      if equal:
        continue
      remaining_subjects.append(i)
      cont += 1
      print(f'{cont} {i.__str__()}')
    cont += 1
    print(f'{cont} Go back')
    print()
    
    while True:
      request = int(input('Which subject you want to subscribe?: '))
      if request < 0 or request > cont:
        print('The number is wrong')
        print()
        continue
      
      if request == cont:
        return
      
      user = self._user_service.get_by_username(username)
      new_subscription = Subscription(subject=remaining_subjects[request], user=user)
      
      self._service.subscribe(new_subscription)
      print()
      return
  
  def desubscribe(self, username):
    subscriptions = self.get_all(username)
    print(f'{len(subscriptions)} Go back')
    print()
    
    while True:
      request = int(input('Which subject you want to desubscribe?: '))
      if request < 0 or request > len(subscriptions):
        print('The number is wrong')
        print()
        continue
      
      if request == len(subscriptions):
        return
      
      self._service.desubscribe(subscriptions[request].id_subscription)
      print()
      return