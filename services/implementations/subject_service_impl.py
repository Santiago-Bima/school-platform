from school_platform.services.subject_service import SubjectService
from school_platform.repositories.subject_repository import SubjectRepository
from school_platform.models.subject import Subject
from school_platform.models.grade import Grade
from school_platform.repositories.subscription_repository import SubscriptionRepository
from school_platform.models.subscription import Subscription
from school_platform.models.user import User
from school_platform.repositories.mark_repository import MarkRepository
from school_platform.models.mark import Mark

class SubjectServiceImpl(SubjectService):
  def __init__(self):
    self._repository = SubjectRepository()
    self._subscription_repo = SubscriptionRepository()
    self._mark_repo = MarkRepository()
  
  def get_all(self):
    subjects = [ 
      Subject(id=i[0], name=i[1], price=i[2], begining_date=i[3], final_date=i[4], grade=Grade(i[5]))
      for i in self._repository.get_all()
    ]
    return subjects
  
  def get_by_name_and_grade(self, name, grade):
    subject_data = self._repository.get_by_name_and_grade(name, grade)
    if not subject_data:
      return None

    subscriptions_data = self._subscription_repo.get_by_subject(subject_data[0])
    subscriptions = [
      Subscription(
        id_subscription=sub_data[0],
        subject=subject_data,
        user=User(id=sub_data[2]),
        marks=[
          Mark(id_subscription=mark[3], mark=mark[1], id_mark=mark[0], date=mark[2])
          for mark in self._mark_repo.get_by_subscription(sub_data[0])
        ]
      )
      for sub_data in subscriptions_data
    ]

    return Subject(
      id=subject_data[0], name=subject_data[1], price=subject_data[2],
      begining_date=subject_data[3], final_date=subject_data[4],
      grade=Grade(subject_data[5]), subscriptions=subscriptions
    )
    
  def update(self, subject, id):
    subject.name = subject.name.lower().strip()
    
    existing_subject = self._repository.get_by_name_and_grade(subject.name, subject.grade.value)
    if existing_subject and existing_subject[0] != id:
      print('There is already a subject with the same name and grade. Please choose another one.')
      print()
      return False
    
    result = self._repository.update(subject, id)
    if result:
      print(f'The subject: {subject.name} {subject.grade.name} has been updated.')
    
    return result
  
  def insert(self, subject):
    subject.name = subject.name.lower().strip()
    
    existing_subject = self._repository.get_by_name_and_grade(subject.name, subject.grade.value)
    if existing_subject and existing_subject[0] != id:
      print('There is already a subject with the same name and grade. Please choose another one.')
      print()
      return False
    
    result = self._repository.insert(subject)
    if result:
      print(f'The subject: {subject.name} {subject.grade.name} has been inserted.')
    
    return result
  
  def delete(self, id):
    if self._repository.delete(id):
      print('The subject has been deleted')
    print()
  
  