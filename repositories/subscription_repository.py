from utils.db import Database

class SubscriptionRepository:
  def get_by_subject(self, id):
    connection = Database.get_connection()
    if connection:
      cursor = connection.cursor()
      try:
        cursor.execute(f"SELECT * FROM subscriptions where id_subject = %s", (id,))
        rta = cursor.fetchall()
        return rta
      except Exception as e:
        print(f"Error executing query: {e}")
        return None
      finally:
        cursor.close()
        Database.close_connection(connection)
    else:
      return None
  
  def get_by_user(self, id_user):
    connection = Database.get_connection()
    if connection:
      cursor = connection.cursor()
      try:
        cursor.execute("SELECT * FROM subscriptions where id_user = %s", (id_user,))
        rta = cursor.fetchall()
        return rta
      except Exception as e:
        print(f"Error executing query: {e}")
        return None
      finally:
        cursor.close()
        Database.close_connection(connection)
    else:
      return None
  
  def insert(self, subscription):
    connection = Database.get_connection()
    if connection:
      cursor = connection.cursor()
      try:
        cursor.execute("insert into subscriptions SET id_subject=%s, id_user=%s", (subscription.subject.id, subscription.user.id))
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
        cursor.execute("DELETE FROM subscriptions WHERE id_subscription=%s", (id,))
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