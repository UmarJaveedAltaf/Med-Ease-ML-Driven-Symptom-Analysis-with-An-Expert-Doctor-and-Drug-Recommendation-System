import mysql.connector

class DBConnection:
    @staticmethod
    def getConnection():
        try:
            database = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="root",  # or "" if you left it blank
                db='disease_prediction'
            )
            print("✅ MySQL connection successful!")
            return database
        except mysql.connector.Error as err:
            print(f"❌ Error: {err}")
            return None

if __name__ == "__main__":
    db = DBConnection.getConnection()
    if db:
        print("✅ Connection object:", db)
    else:
        print("❌ Connection failed.")
