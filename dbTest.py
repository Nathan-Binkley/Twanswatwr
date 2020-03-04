import mysql.connector
import keys

mydb = mysql.connector.connect(
  host="tweets.sql",
  user=keys.DB_User,
  passwd=keys.DB_Pass
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE mydatabase")