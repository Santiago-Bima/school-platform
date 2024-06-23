from school_platform.services.implementations.subscription_repository_impl import SubscriptionServiceImpl
from school_platform.services.implementations.mark_service_impl import MarkServiceImpl

class SubscriptionController:
  def __init__(self):
    self._service = SubscriptionServiceImpl()
    self._marks_service = MarkServiceImpl()
    
  def get_all(self, username):
    subscriptions = self._service.get_by_user(username)
    
    if not subscriptions:
      pass
    
    for i in subscriptions:
      print(i.__str__() + ' \n')
      marks = self._marks_service.get_by_subscription(i.id_subscription)
      if marks:
        for j in marks:
          print(f'{j.date}: {j.mark}')
      print()