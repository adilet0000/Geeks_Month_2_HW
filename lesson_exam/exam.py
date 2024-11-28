import sqlite3

def create_connection(db_name):
   try:
      connection = sqlite3.connect(db_name)
      return connection
   except sqlite3.Error as e:
      print(f"Error connecting to database: {e}")
      return None

def fetch_stores(connection):
   sql = "SELECT store_id, title FROM store"
   cursor = connection.cursor()
   cursor.execute(sql)
   return cursor.fetchall()

def fetch_products_by_store(connection, store_id):
   sql = '''
   SELECT p.title, c.title AS category, p.unit_price, p.stock_quantity
   FROM products p
   JOIN categories c ON p.category_code = c.code
   WHERE p.store_id = ?
   '''
   cursor = connection.cursor()
   cursor.execute(sql, (store_id,))
   return cursor.fetchall()

def main():
   db_name = "exam.db"
   connection = create_connection(db_name)

   if not connection:
      print("Не удалось подключиться к базе данных.")
      return

   while True:
      print("\nВы можете отобразить список продуктов по выбранному id магазина из перечня магазинов ниже, для выхода из программы введите цифру 0:")
      stores = fetch_stores(connection)
      for store in stores:
         print(f"{store[0]}. {store[1]}")

      try:
         user_input = int(input("\nВведите id магазина: "))
      except ValueError:
         print("Пожалуйста, введите число.")
         continue

      if user_input == 0:
         print("Выход из программы.")
         break

      store_ids = [store[0] for store in stores]
      if user_input not in store_ids:
         print("Магазина с таким id не существует. Попробуйте снова.")
         continue

      products = fetch_products_by_store(connection, user_input)
      if products:
         print("\nПродукты в выбранном магазине:")
         for product in products:
            print(f"Название продукта: {product[0]}")
            print(f"Категория: {product[1]}")
            print(f"Цена: {product[2]}")
            print(f"Количество на складе: {product[3]}")
            print("-" * 40)
      else:
         print("В данном магазине нет продуктов.")

   connection.close()

if __name__ == "__main__":
   main()
