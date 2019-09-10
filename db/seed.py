import pandas as pd
import sqlite3

conn = sqlite3.connect('jane.db')
c = conn.cursor()

c.execute('''
    drop table if exists products
''')
c.execute('''
    create table products (
         id int primary key,
         amount text,
         brand text,
         lineage text,
         name text not null,
         product_type text,
         product_subtype text,
         url text
    )
''')
df = pd.read_csv('products.csv')
df.to_sql('products', conn, if_exists='append', index=False)

conn.commit()
conn.close()
