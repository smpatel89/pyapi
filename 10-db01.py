#!/usr/bin/python3

import sqlite3

conn = sqlite3.connect('data/test.db')
print('Opened db successfully')

try:
    conn.execute(\
            ''' CREATE TABLE company            ''' \
            '''   (id INT PRIMARY KEY NOT NULL, ''' \
            '''   name TEXT NOT NULL,           ''' \
            '''   age INT NOT NULL,             ''' \
            '''   address CHAR(50),             ''' \
            '''   salary REAL);                 '''
            )
except Exception as e:
    print(f'Table creation error - {e}')
else:
    print('Table created successfully')

conn.execute(\
        ''' INSERT INTO company                             ''' \
        '''   (id, name, age, address, salary)              ''' \
        ''' VALUES(1, "Paul", 32, "California", 200000.00); '''
        )
conn.commit()
conn.close()
