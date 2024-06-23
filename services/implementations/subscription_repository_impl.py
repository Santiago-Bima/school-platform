from school_platform.services.subscription_service import SubscriptionService
from school_platform.repositories.subscription_repository import SubscriptionRepository
from school_platform.repositories.user_repository import UserRepository
from school_platform.repositories.subject_repository import SubjectRepository
from school_platform.repositories.mark_repository import MarkRepository
from school_platform.models.subscription import Subscription
from school_platform.models.user import User
from school_platform.models.subject import Subject
from school_platform.models.grade import Grade

class SubscriptionServiceImpl(SubscriptionService):
  def __init__(self):
    self._repository = SubscriptionRepository()
    self._subject_repository = SubjectRepository()
    self._user_repository = UserRepository()
    self._mark_repository = MarkRepository()
  
  def get_by_user(self, username):
    user = self._user_repository.get_user_by_name(username)
    user_id = user[3]
    
    subscriptions = self._repository.get_by_user(user_id)
    
    if not subscriptions:
      print('There are no subscriptions to any subject for this user')
      return False
    
    subscriptions_obj = []
    for i in subscriptions:
      subject = self._subject_repository.get_by_id(i[0])
      subject_obj = Subject(name=subject[1], grade=Grade(subject[5]), price=subject[2])
      marks = self._mark_repository.get_by_subscription(i[0])
      subscription = Subscription(subject=subject_obj, inscription_date=i[1], marks=marks, id_subscription=i[0])
      subscriptions_obj.append(subscription)
      
    return subscriptions_obj