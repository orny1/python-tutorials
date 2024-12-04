import psycopg2
from decouple import config
import logging

logger = logging.getLogger(__name__)


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
        print("Database not connected successfully")
    return conn

def create_car_table(conn):
    query = """
    create table if not exists cars (
    id SERIAL PRIMARY KEY,
    make VARCHAR(50),
    model VARCHAR(50)
    );
    """
    try:
        cur = conn.cursor()
        cur.execute(query)

    except Exception as e:
        print(f"Could not create car table, {e}")
        return 
    conn.commit()
    print("Car table created successfully.")

def insert_car(conn, make, model):
    query = """
    INSERT INTO cars (make, model) values
    (%s, %s);
    """
    try:
        cur = conn.cursor()
        cur.execute(query, (make, model))
        conn.commit()

    except Exception as e:
        print(f"Could not add car: {e}")
        return
    print("Car added successfully")

def list_cars(conn):
    query = """
    SELECT * FROM cars;
    """
    cur = conn.cursor()
    cur.execute(query)
    rows = cur.fetchall()
    print("-"*49)
    print(f"\tID\t|\tMODEL\t|\tMAKE\t|")
    print("-"*49)
    for car in rows:
        print(f"\t{car[0]}\t| \t{car[1]}\t| \t{car[2]}\t|")
        print("-"*49)

def get_car_info(conn, car_id):
    query = """
    SELECT * FROM cars WHERE id=%s;
    """
    cur = conn.cursor()
    cur.execute(query, (car_id, ))
    car = cur.fetchone()
    
    if car:
        print("-"*49)
        print(f"\tID\t|\tMODEL\t|\tMAKE\t|")
        print("-"*49)
        print(f"\t{car[0]}\t| \t{car[1]}\t| \t{car[2]}\t|")
        print("-"*49)
    else:
        print("No car with given ID, status=404")

def update_make(conn, make, car_id):
    query = """
    UPDATE cars SET make=%s where id=%s;
    """
    try:
        cur = conn.cursor()
        cur.execute(query, (make, car_id))
        conn.commit()

    except Exception as e:
        print(f"Something went wrong while updating car information: {e}")
        conn.rollback()
        return
    print(f"Make of car-{car_id} has been updated successfully")



def update_model(conn, model, car_id):
    query = """
    UPDATE cars SET model=%s where id=%s;
    """
    try:
        cur = conn.cursor()
        cur.execute(query, (model, car_id))
        conn.commit()

    except Exception as e:
        print(f"Something went wrong while updating car information: {e}")
        conn.rollback()
        return
    print(f"Model of car-{car_id} has been updated successfully")

def delete_car(conn, car_id):
    query = """
    DELETE FROM cars WHERE cars.id = %s;
    """
    try:
        cur = conn.cursor() 
        cur.execute(query, (car_id,))
    except Exception as e:
        print(f"Could not delete car with id={car_id}")
        return
    conn.commit()
    print(f"Car with id={car_id} deleted successfully, status=204")
    list_cars(conn)
    
def main():
    # connect to the database
    conn = connect_db()
    if conn:
        pass
    else:
        print('database not connected.')
        return 
    welcome_message = "=========== WELCOME TO BLIX CAR INVENTORY ============"
    options_string = """
    SELECT AN OPTIONS: ADD [1],\t LIST CARS [2],\t SEE CAR INFO [3],\t UPDATE CAR [4], DELETE CAR [5]
    """
    print(welcome_message)
    while True:
        # ask user for the option
        print(options_string)
        try:
            option = int(input("Enter an option from above: "))
        except:
            print("invalid options")
            continue

        if option == 1:
            # user wants to add a car
            make = input("Enter make of the car: ")
            model = input("Enter car model: ")
            insert_car(conn, make, model)
        
        if option == 2:
            # user wants to list cars
            list_cars(conn)

        if option == 3:
            try:
                carID = int(input("enter car id: "))
            except:
                print("Invalid input")
                continue
            get_car_info(conn, carID)
        
        if option == 4:
            update_options = """UPDATE CAR INFORMATION: MAKE [1],\t MODEL [2]"""
            print(update_options)
            try:
                update_option = int(input("Enter option of interest to be updated as seen above: "))
            except:
                print("invalid input")
                continue
            if update_option == 1:
                # user wants to update the make of the car
                make = input("Enter new Make: ")
                try:
                    carID = int(input("Enter carID: "))
                except:
                    print('invalid input for car id, must be integer')
                if carID:
                    update_make(conn, make, carID)
            if update_option == 2:
                # user wants to update the model of the car
                model = input("Enter new model: ")
                try:
                    carID = int(input("Enter carID: "))
                except:
                    print('invalid input for car id, must be integer')
                if carID:
                    update_model(conn, model, carID)

        if option == 5:
            try:
                carID = int(input("Enter car ID: "))
            except:
                print("Invalid input")
                continue
            delete_car(conn, carID)


        if option == -1:
            break


if __name__ == "__main__":
    main()

