from flask import Flask, render_template, request
import database_creation
import database_functions
import psycopg2

# Veritabanı bağlantısı için gerekli bilgileri belirtin
db_host = 'localhost'
db_port = '5432'
db_name = 'q-gen'
db_user = 'postgres'
db_password = 'melisa33'

# PostgreSQL veritabanına bağlantı kurun
conn = psycopg2.connect(
    host=db_host,
    port=db_port,
    dbname=db_name,
    user=db_user,
    password=db_password
)

# Bağlantı üzerinden bir imleç (cursor) oluşturun
cursor = conn.cursor()

cursor.execute(database_creation.create_table_query)
conn.commit()
    

app = Flask(__name__)
@app.route('/')
def index():
    cursor.execute('SELECT * FROM coaches')
    users = cursor.fetchall()
    cursor.execute('SELECT * FROM students')
    users2=cursor.fetchall()
    return render_template('index.html', users=users,users2=users2)


# Bağlantıyı ve imleci kapatın
#cursor.close()
#conn.close()


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)