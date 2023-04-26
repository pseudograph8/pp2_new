import psycopg2

# changing phone number by first name
def update_phonebook(id, phone_number):
    """ update vendor name based on the vendor id """
    sql = """ UPDATE phonebook
                SET phone_number = %s
                WHERE id = %s"""
    conn = None

    try:
        conn = psycopg2.connect(host="localhost", dbname="postgres", user="postgres", password="seidazym", port = 5432)

        cur = conn.cursor()

        #create a table
        cur.execute("""CREATE TABLE IF NOT EXISTS phoneBook (
            id INT PRIMARY KEY,
            first_name VARCHAR(255),
            phone_number VARCHAR(255)
            );
        """)

        cur.execute("""INSERT INTO phonebook (id, first_name, phone_number) VALUES
        (1, 'Aruzhan', '+7475637615'),
        (2, 'Firuza', '+77084236847'),
        (3, 'Aknur', '+77082995405'),
        (4, 'Aina', '+77012995405'),
        (5, 'James', '+75005412698');
        """)

        

        # print user with the id = 1
        # cur.execute("""SELECT * FROM phonebook WHERE id = 1;""")
        # print(cur.fetchone())

        # sql = cur.mogrify("""SELECT * FROM phonebook WHERE starts_with(first_name, %s)""", ("A"))
        # print(sql)
        # cur.execute(sql)
        # print(cur.fetchall())

        # execute the UPDATE  statement
        cur.execute(sql, (id, phone_number))

        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()


    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

if __name__ == '__main__':
    # Update id 
    update_phonebook('+75854785624', 5)