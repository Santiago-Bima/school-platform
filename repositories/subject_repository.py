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
  
  