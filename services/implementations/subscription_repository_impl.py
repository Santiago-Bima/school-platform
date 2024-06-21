from school_platform.services.subscription_service import SubscriptionService
from school_platform.repositories.subscription_repository import SubscriptionRepository
from school_platform.repositories.user_repository import UserRepository
from school_platform.models.subscription import Subscription
from school_platform.models.user import User

class SubscriptionServiceImpl(SubscriptionService):
  def __init__(self):
    self._repository = SubscriptionRepository()
    self._user_repository = UserRepository()
  
  def get_by_user(self, username):
    user = self._user_repository.get_user_by_name(username)
    user_id = user[3]
    
    subscriptions = self._repository.get_by_username(user_id)
    
    if not subscriptions:
      print('There are no subscriptions to any subject for this user')
      return False
    
    print (subscriptions)