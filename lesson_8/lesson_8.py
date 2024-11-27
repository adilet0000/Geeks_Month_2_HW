import sqlite3

def create_connection(db_name):
   try:
      connection = sqlite3.connect(db_name)
      return connection
   except sqlite3.Error as e:
      print(e)
      return None

def fetch_cities(connection):
   try:
      cursor = connection.cursor()
      cursor.execute("SELECT id, title FROM cities")
      return cursor.fetchall()
   except sqlite3.Error as e:
      print(e)
      return []

def fetch_students_by_city(connection, city_id):
   sql = '''
      SELECT 
         s.first_name, 
         s.last_name, 
         c.title AS city_title, 
         co.title AS country_title, 
         c.area
      FROM students s
      JOIN cities c ON s.city_id = c.id
      JOIN countries co ON c.country_id = co.id
      WHERE c.id = ?
    '''
   try:
      cursor = connection.cursor()
      cursor.execute(sql, (city_id,))
      return cursor.fetchall()
   except sqlite3.Error as e:
      print(e)
      return []

def main():
   db_name = "hw.db"
   connection = create_connection(db_name)

   if connection:
      while True:
         print("\nВы можете отобразить список учеников по выбранному id города из перечня городов ниже, для выхода из программы введите 0:")
         
         cities = fetch_cities(connection)
         for city in cities:
            print(f"{city[0]}. {city[1]}")
         try:
               city_id = int(input("\nВведите id города: "))
               if city_id == 0:
                  print("Программа завершена.")
                  break

               students = fetch_students_by_city(connection, city_id)
               if students:
                  print(f"\nУченики, проживающие в выбранном городе:")
                  for student in students:
                     print(f"Имя: {student[0]}, Фамилия: {student[1]}, Страна: {student[3]}, Город: {student[2]}, Площадь города: {student[4]} км²")
               else:
                  print("В этом городе нет учеников.")
         except ValueError:
            print("Пожалуйста, введите корректный id.")

      connection.close()

if __name__ == "__main__":
   main()
