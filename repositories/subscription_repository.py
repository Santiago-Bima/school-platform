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
