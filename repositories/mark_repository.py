from utils.db import Database

class MarkRepository:
  def get_by_subscription(self, id_subscription):
    connection = Database.get_connection()
    if connection:
      cursor = connection.cursor()
      try:
        cursor.execute(f"SELECT * FROM marks where id_subscription = %s", (id_subscription,))
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