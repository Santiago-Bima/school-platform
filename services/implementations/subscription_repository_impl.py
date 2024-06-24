from school_platform.services.subscription_service import SubscriptionService
from school_platform.repositories.subscription_repository import SubscriptionRepository
from school_platform.repositories.user_repository import UserRepository
from school_platform.repositories.subject_repository import SubjectRepository
from school_platform.repositories.mark_repository import MarkRepository
from school_platform.models.subscription import Subscription
from school_platform.models.user import User
from school_platform.models.subject import Subject
from school_platform.models.grade import Grade
from school_platform.models.mark import Mark

class SubscriptionServiceImpl(SubscriptionService):
  def __init__(self):
    self._repository = SubscriptionRepository()
    self._subject_repository = SubjectRepository()
    self._user_repository = UserRepository()
    self._mark_repository = MarkRepository()
  
  def get_by_user(self, username):
    user = self._user_repository.get_user_by_name(username)
    user_id = user[0]
    
    subscriptions = self._repository.get_by_user(user_id)
    
    if not subscriptions:
      print('There are no subscriptions to any subject for this user')
      return False
    
    subscriptions_obj = []
    for i in subscriptions:
      subject = self._subject_repository.get_by_id(i[1])
      subject_obj = Subject(id=subject[0] ,name=subject[1], grade=Grade(subject[5]), price=subject[2])
      marks = self._mark_repository.get_by_subscription(i[0])
      marks_obj = []
      for j in marks:
        mark = Mark(mark=j[1],date=j[3])
        marks_obj.append(mark)
      subscription = Subscription(subject=subject_obj, inscription_date=i[3], marks=marks_obj, id_subscription=i[0])
      subscriptions_obj.append(subscription)
      
    return subscriptions_obj

  def subscribe(self, subscription):
    rta = self._repository.insert(subscription)
    
    if rta:
      print('You have been subscribed correctly')
  
  def desubscribe(self, id):
    if self._repository.delete(id):
      print('The subscription has been deleted')
    print()