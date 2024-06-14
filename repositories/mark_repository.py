from utils.db import Database

class MarkRepository:
  def get_by_subscription(self, id_subscription):
    connection = Database.get_connection()
    if connection:
      cursor = connection.cursor()
      try:
        cursor.execute(f"SELECT * FROM marks where id_subscription = %s ORDER BY date ASC", (id_subscription,))
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
  
  def get_by_date(self, date):
    connection = Database.get_connection()
    if connection:
      cursor = connection.cursor()
      try:
        cursor.execute(f"SELECT * FROM marks where date = %s", (date,))
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
  
  def insert(self, mark):
    connection = Database.get_connection()
    if connection:
      cursor = connection.cursor()
      try:
        cursor.execute(f"insert into marks SET mark=%s,id_subscription=%s, date=%s", (mark.mark, mark.id_subscription, mark.date))
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