from decouple import config
import psycopg2
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# logger.debug("This is a debug message")
# logger.info("This is a info message")
# logger.warning("This is a warning message")
# logger.error("This is a error message")
# logger.critical("This is a critical message")

def connect_db():
    conn = None
    try:
        conn = psycopg2.connect(database=config("DB_NAME"),
                                user=config("DB_USER"),
                                password=config("DB_PASS"),
                                host=config("DB_HOST"),
                                port=config("DB_PORT"))
        print("Database connected successfully")
    except:
        logger.error("Error accessing database")


connect_db()