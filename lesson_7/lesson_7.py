import sqlite3

products_list = [
   ('Twix', 50, 20),
   ('KitKat', 55, 25),
   ('Oreo', 65, 30),
   ('Alpen Gold', 80, 12),
   ('Ferrero Rocher', 180, 8),
   ('Lindt', 145, 10),
   ('Kinder Bueno', 70, 15),
   ('Ritter Sport', 90, 12),
   ('Snickers', 60, 18),
   ('Mars', 55, 22),
   ('Milka', 100, 20),
   ('Hershey\'s', 85, 10),
   ('Toblerone', 110, 8),
   ('Bounty', 45, 25),
   ('Milky Way', 40, 30)
]

def create_connection(db_name):
   try:
      connection = sqlite3.connect(db_name)
      print('Connection established')
      return connection
   except sqlite3.Error as e:
      print(e)
      return None

def create_table(connection):
   sql = '''
   CREATE TABLE IF NOT EXISTS products (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      product_title TEXT NOT NULL CHECK(length(product_title) <= 200),
      price REAL NOT NULL DEFAULT 0.0,
      quantity INTEGER NOT NULL DEFAULT 0
    )
    '''
   try:
      cursor = connection.cursor()
      cursor.execute(sql)
      connection.commit()
      print("Table 'products' created or already exists.")
   except sqlite3.Error as e:
      print(e)

def insert_multiple_products(connection, products):
   sql = '''INSERT INTO products (product_title, price, quantity) VALUES (?, ?, ?)'''
   try:
      cursor = connection.cursor()
      cursor.executemany(sql, products)
      connection.commit()
      print(f"{len(products)} products were successfully added to the database.")
   except sqlite3.Error as e:
      print(e)

def search_products_by_name(connection, search_term):
   sql = '''SELECT * FROM products WHERE product_title LIKE ?'''
   try:
      cursor = connection.cursor()
      cursor.execute(sql, (f"%{search_term}%",))
      rows = cursor.fetchall()
      print(f"Products matching '{search_term}':")
      if rows:
         for row in rows:
             print(row)
      else:
         print("No matching products found.")
   except sqlite3.Error as e:
      print(e)

def update_product(connection, product_id, updated_values):
   sql = '''UPDATE products SET product_title = ?, price = ?, quantity = ? WHERE id = ?'''
   try:
      cursor = connection.cursor()
      cursor.execute(sql, (*updated_values, product_id))
      connection.commit()
      print(f"Product with ID {product_id} updated successfully.")
   except sqlite3.Error as e:
      print(e)

def delete_product(connection, product_id):
   sql = '''DELETE FROM products WHERE id = ?'''
   try:
      cursor = connection.cursor()
      cursor.execute(sql, (product_id,))
      connection.commit()
      print(f"Product with ID {product_id} deleted successfully.")
   except sqlite3.Error as e:
      print(e)

def fetch_all_products(connection):
   sql = '''SELECT * FROM products'''
   try:
      cursor = connection.cursor()
      cursor.execute(sql)
      rows = cursor.fetchall()
      print("Products in the database:")
      for row in rows:
         print(row)
   except sqlite3.Error as e:
      print(e)

def update_quantity_by_id(connection, product_id, quantity):
   sql = '''UPDATE products SET quantity = ? WHERE id = ?'''
   try:
      cursor = connection.cursor()
      cursor.execute(sql, (quantity, product_id))
      connection.commit()
      print(f"Quantity of product with ID {product_id} updated to {quantity}.")
   except sqlite3.Error as e:
      print(e)

def update_price_by_id(connection, product_id, price):
   sql = '''UPDATE products SET price = ? WHERE id = ?'''
   try:
      cursor = connection.cursor()
      cursor.execute(sql, (price, product_id))
      connection.commit()
      print(f"Price of product with ID {product_id} updated to {price}.")
   except sqlite3.Error as e:
      print(e)

def fetch_products_by_criteria(connection, price_limit, quantity_limit):
   sql = '''SELECT * FROM products WHERE price < ? AND quantity > ?'''
   try:
      cursor = connection.cursor()
      cursor.execute(sql, (price_limit, quantity_limit))
      rows = cursor.fetchall()
      print(f"Products cheaper than {price_limit} and with quantity more than {quantity_limit}:")
      for row in rows:
         print(row)
   except sqlite3.Error as e:
      print(e)

if __name__ == "__main__":
   db_name = 'hw.db'
   connection = create_connection(db_name)

   if connection:
      create_table(connection)
      insert_multiple_products(connection, products_list)
      update_product(connection, 1, ('Updated Twix', 60, 35))
      update_quantity_by_id(connection, 3, 50)
      update_price_by_id(connection, 4, 75.5)
      fetch_products_by_criteria(connection, 100, 10)
      search_products_by_name(connection, 'Snickers')
      delete_product(connection, 2)
      fetch_all_products(connection)
      connection.close()
