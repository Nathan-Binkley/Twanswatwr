import mysql.connector
import keys

mydb = mysql.connector.connect(
  host="localhost",
  user=keys.DB_User,
  passwd=keys.DB_Pass
)

mycursor = mydb.cursor()

try:
    mycursor.execute("CREATE DATABASE mydatabase") #DATABASES "mydatabase" "tweets"
except:
    mycursor.execute("SHOW DATABASES")


