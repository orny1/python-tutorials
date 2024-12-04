
import psycopg2
 
DB_NAME = "testing"
DB_USER = "posgres"
DB_PASS = "TsapiOrny02"
DB_HOST = "localhost"
DB_PORT = "5432"
 
try:
    conn = psycopg2.connect(database=DB_NAME,
                            user=DB_USER,
                            password=DB_PASS,
                            host=DB_HOST,
                            port=DB_PORT)
    print("Database connected successfully")
except:
    print("Database not connected successfully")