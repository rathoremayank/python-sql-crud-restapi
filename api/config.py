from app import app
from flaskext.mysql import MySQL

mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'Welcome01'
app.config['MYSQL_DATABASE_DB'] = 'phoenix-db'
app.config['MYSQL_DATABASE_HOST'] = '172.17.0.2'
mysql.init_app(app)
