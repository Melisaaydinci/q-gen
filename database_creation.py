create_table_query = '''
    CREATE TABLE  IF NOT EXISTS coaches(
        id SERIAL PRIMARY KEY,
        name VARCHAR(100),
        surname VARCHAR(100),
        mail VARCHAR(100),
        password VARCHAR(10),
        telephone VARCHAR(11),
        student_list integer[] 
       
    );
    CREATE TABLE IF NOT EXISTS students (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100),
        surname VARCHAR(100),
        mail VARCHAR(100),
        password VARCHAR(10),
        telephone VARCHAR(11),
        programs JSON
       
    );
    CREATE TABLE IF NOT EXISTS videos(
        id SERIAL PRIMARY KEY,
        class VARCHAR(100),
        subclass VARCHAR(100),
        videos_id integer[]  
       
    );
'''
