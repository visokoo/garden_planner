# ########################################
# ########## SETUP

from flask import Flask, render_template, request, redirect
import database.db_connector as db

PORT = 8000

app = Flask(__name__)

# ########################################
# ########## ROUTE HANDLERS

# READ ROUTES
@app.route("/", methods=["GET"])
def home():
  try:
    return render_template("home.j2")

  except Exception as e:
    print(f"Error rendering page: {e}")
    return "An error occurred while rendering the page.", 500


@app.route("/plants", methods=["GET"])
def plants():
  try:
    db_connection = db.connect_db()  # Open our database connection

    query1 = "SELECT * FROM Plant;"
    plants = db.query(db_connection, query1).fetchall()

    # Render the plant.j2 file, and also send the renderer
    return render_template(
      "plant.j2", plants=plants
    )

  except Exception as e:
    print(f"Error executing queries: {e}")
    return(f"An error occurred while executing the database queries.", 500)

  finally:
    # Close the DB connection, if it exists
    if "db_connection" in locals() and db_connection:
        db_connection.close()

@app.route("/gardens", methods=["GET"])
def gardens():
  try:
    db_connection = db.connect_db()  # Open our database connection

    # query1 = "SELECT * FROM Garden;"
    query1 = "SELECT Garden.garden_id, Garden.description, Garden.location, \
              CONCAT(User.first_name, ' ', User.last_name) AS owner \
              FROM Garden JOIN User on Garden.user_id = User.user_id;"
    gardens = db.query(db_connection, query1).fetchall()

    query2 = "SELECT User.user_id, CONCAT(User.first_name, ' ', User.last_name) AS owner FROM USER;"
    users = db.query(db_connection, query2).fetchall()

    # Render the garden.j2 file, and also send the renderer
    return render_template(
      "garden.j2", gardens=gardens, users=users
    )

  except Exception as e:
    print(f"Error executing queries: {e}")
    return(f"An error occurred while executing the database queries.", 500)

  finally:
    # Close the DB connection, if it exists
    if "db_connection" in locals() and db_connection:
        db_connection.close()



# ########################################
# ########## LISTENER

if __name__ == "__main__":
  app.run(
    port=PORT, debug=True
  )
