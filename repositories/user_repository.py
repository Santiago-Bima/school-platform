from utils.db import Database

class UserRepository:
  def get_all(self):
    connection = Database.get_connection()
    if connection:
      cursor = connection.cursor()
      try:
        cursor.execute("SELECT * FROM users order by id_type desc")
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
  
  def delete(self, id):
    connection = Database.get_connection()
    if connection:
      cursor = connection.cursor()
      try:
        cursor.execute(f"DELETE FROM users where id=%s", (id,))
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
  
  def update(self, user, id):
    connection = Database.get_connection()
    if connection:
      cursor = connection.cursor()
      try:
        cursor.execute(f"UPDATE users SET username=%s,password=%s,id_type=%s WHERE id=%s", (user.username, user.password, user.user_type.value, id))
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
  
  def insert(self, user):
    connection = Database.get_connection()
    if connection:
      cursor = connection.cursor()
      try:
        cursor.execute(f"INSERT INTO users (`username`, `password`, `id_type`) VALUES (%s, %s, %s) ", (user.username, user.password, user.user_type.value))
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
    
  def get_user_by_name(self, username):
    connection = Database.get_connection()
    if connection:
      cursor = connection.cursor()
      try:
        cursor.execute(f"SELECT * FROM users where username=%s", (username,))
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