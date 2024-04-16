
import mysql.connector
from utilities import basic_math
import unittest

def main():
    # print("reading db")
    # read_db()
    
    a = 7
    even_result = basic_math.check_even(a)    
    print(even_result)

    add_num_result = basic_math.add_numbers(a, 6)
    print(add_num_result)



def read_db():
    user = 'root'
    pwd = 'root'
    database = 'example'
    query = "select * from students where Name = 'joe'"

    example_con = mysql.connector.connect(user = user, 
                                         database = database, 
                                         password = pwd)

    cursor = example_con.cursor()
    try:
        cursor.execute(query)
        if cursor.len() >0:
            print("true")
        else:
            print("false")
            # print(item)
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        example_con.close()
         


if __name__ =='__main__':
    # main()
    unittest.main()
