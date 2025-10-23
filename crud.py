import psycopg2
hostname = 'localhost'
database = 'demo_db'
username = 'postgres'
pwd = 'Naman2003'
port_id = 5432
conn = None
cur = None
try:
    conn = psycopg2.connect(
        host = hostname,
        dbname = database,
        user = username,
        password = pwd,
        port = port_id
    )
    cur = conn.cursor()

    cur.execute('DROP TABLE IF EXISTS sales')

    create_script = ''' CREATE TABLE IF NOT EXISTS sales (
    sale_id SERIAL PRIMARY KEY,
    customer_name VARCHAR(50),
    product_name VARCHAR(50),
    quantity INT,
    price_per_unit DECIMAL(10, 2),
    sale_date DATE)  '''

    cur.execute(create_script)

    insert_script = 'INSERT INTO sales (customer_name, product_name, quantity, price_per_unit, sale_date) VALUES (%s, %s, %s, %s, %s)'
    insert_values = [('Rahul Sharma', 'Laptop', 2, 55000.00, '2025-10-20'),
                    ('Priya Verma', 'Smartphone', 1, 32000.00, '2025-10-19'),
                    ('Amit Kumar', 'Headphones', 3, 2500.00, '2025-10-18'),
                    ('Sneha Gupta', 'Monitor', 1, 12000.00, '2025-10-17'),
                    ('Vikas Mehta', 'Keyboard', 5, 900.00, '2025-10-16'),
                    ('Ankur', 'Refrigerator', 1, 45000.00, '2025-08-01')]
    
    for record in insert_values:
        cur.execute(insert_script,record)

    update_script = 'UPDATE sales SET price_per_unit = price_per_unit + (price_per_unit * 0.5)'
    cur.execute(update_script)

    delete_script = 'DELETE FROM sales where customer_name = %s'
    delete_record = ('Rahul Sharma',)
    cur.execute(delete_script,delete_record)

    cur.execute('SELECT * FROM SALES')
    for record in cur.fetchall():
        print(record)
    conn.commit()




except Exception as error:
    print(error)
finally:
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()
