from school_platform.services.subject_service import SubjectService
from school_platform.repositories.subject_repository import SubjectRepository
from school_platform.models.subject import Subject
from school_platform.models.grade import Grade

class SubjectServiceImpl(SubjectService):
  def __init__(self):
    self._repository = SubjectRepository()
  
  def get_all(self):
    rta = self._repository.get_all()
    print(rta)
    subjects = []
    for i in rta:
      subject = Subject(name=i[1], price=i[2], begining_date=i[3], final_date=i[4], grade=Grade(i[5]))
      subjects.append(subject)
    return subjects
    
