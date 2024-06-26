from utils.db import Database

class SubjectRepository:
  def get_all(self):
    connection = Database.get_connection()
    if connection:
      cursor = connection.cursor()
      try:
        cursor.execute("SELECT * FROM subjects")
        rta = cursor.fetchall()
        return rta
      except Exception as e:
        print(f"Error executing query: {e}")
        return []
      finally:
        cursor.close()
        Database.close_connection(connection)
    else:
      return []
  
  def get_by_name_and_grade(self, name, grade):
    connection = Database.get_connection()
    if connection:
      cursor = connection.cursor()
      try:
        cursor.execute("SELECT * FROM subjects where name LIKE %s AND grade = %s", (name, grade))
        rta = cursor.fetchone()
        return rta
      except Exception as e:
        print(f"Error executing query: {e}")
        return None
      finally:
        cursor.close()
        Database.close_connection(connection)
    else:
      return None
  
  def update(self, subject, id):
    connection = Database.get_connection()
    if connection:
      cursor = connection.cursor()
      try:
        cursor.execute("UPDATE subjects SET name=%s,price=%s,begining_date=%s, final_date=%s, grade=%s WHERE id=%s", (subject.name, subject.price, subject.begining_date, subject.final_date, subject.grade.value ,id))
        connection.commit()
        return True
      except Exception as e:
        print(f"Error executing query: {e}")
        return False
      finally:
        cursor.close()
        Database.close_connection(connection)
    else:
      return False
  
  def insert(self, subject):
    connection = Database.get_connection()
    if connection:
      cursor = connection.cursor()
      try:
        cursor.execute("insert into subjects SET name=%s,price=%s,begining_date=%s, final_date=%s, grade=%s", (subject.name, subject.price, subject.begining_date, subject.final_date, subject.grade.value))
        connection.commit()
        return True
      except Exception as e:
        print(f"Error executing query: {e}")
        return False
      finally:
        cursor.close()
        Database.close_connection(connection)
    else:
      return False
  
  def delete(self, id):
    connection = Database.get_connection()
    if connection:
      cursor = connection.cursor()
      try:
        cursor.execute("DELETE FROM subjects WHERE id=%s", (id,))
        connection.commit()
        return True
      except Exception as e:
        print(f"Error executing query: {e}")
        return False
      finally:
        cursor.close()
        Database.close_connection(connection)
    else:
      return False
  
  def get_by_id(self, id):
    connection = Database.get_connection()
    if connection:
      cursor = connection.cursor()
      try:
        cursor.execute("SELECT * FROM subjects where id = %s", (id,))
        rta = cursor.fetchone()
        return rta
      except Exception as e:
        print(f"Error executing query: {e}")
        return None
      finally:
        cursor.close()
        Database.close_connection(connection)
    else:
      return None