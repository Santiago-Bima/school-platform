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
    self._suscription_repo = SubscriptionRepository()
    self._mark_repo = MarkRepository()
  
  def get_all(self):
    rta = self._repository.get_all()
    subjects = []
    for i in rta:
      subject = Subject(name=i[1], price=i[2], begining_date=i[3], final_date=i[4], grade=Grade(i[5]))
      subjects.append(subject)
    return subjects
  
  def get_by_name_and_grade(self, name, grade):
    rta = self._repository.get_by_name_and_grade(name, grade)
    subscriptions = self._suscription_repo.get_by_subject(rta[0])
    subscriptions_objects = []
    for i in subscriptions:
      marks = self._mark_repo.get_by_subscription(i[2])
      marks_objects = []
      for j in marks:
        mark = Mark(id_subscription=j[0], mark=j[1], id_mark=j[2], date=j[3])
        marks_objects.append(mark)
      subscription = Subscription(id_suscription=i[2], subject=rta, user=User(id=i[3]), marks=marks_objects)
      subscriptions_objects.append(subscription)
    rta = Subject(id=rta[0], name=rta[1], price=rta[2], begining_date=rta[3], final_date=rta[4], grade=Grade(rta[5]), subscriptions=subscriptions_objects)
    return rta
    
  def update(self, subject, id):
    subject.name = subject.name.lower().strip()
    
    existing_subject = self._repository.get_by_name_and_grade(subject.name, subject.grade.value)
    if existing_subject is not None and existing_subject[0] != id:
      print('There is already a subject with the same name and grade. Please choose another one.')
      print()
      return False
    
    result = self._repository.update(subject, id)
    if result:
      print(f'The subject: {subject.name} {subject.grade.name} has been updated.')
      return result
    else:
      return False
  
  def insert(self, subject):
    subject.name = subject.name.lower().strip()
    
    existing_subject = self._repository.get_by_name_and_grade(subject.name, subject.grade.value)
    if existing_subject is not None and existing_subject[0] != id:
      print('There is already a subject with the same name and grade. Please choose another one.')
      print()
      return False
    
    result = self._repository.insert(subject)
    if result:
      print(f'The subject: {subject.name} {subject.grade.name} has been inserted.')
      return result
    else:
      return False
  
  