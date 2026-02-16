# ########################################
# ########## SETUP

# All code is based on the CS340 starter code, with the exception of the actual queries
# used for querying the DB or otherwise noted.

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

# -------------- [ PLANT ] -------------- #

@app.route("/plants", methods=["GET"])
def plants():
  try:
    db_connection = db.connect_db()  # Open our database connection

    query1 = "SELECT Plant.plant_id AS id, Plant.species, Plant.plant_category AS 'plant category', Plant.water_requirements AS 'water requirements', \
              Plant.sunlight, Plant.season, Plant.cycle, Plant.edible FROM Plant;"
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

# -------------- [ GARDEN ] -------------- #
@app.route("/gardens", methods=["GET"])
def gardens():
  try:
    db_connection = db.connect_db()  # Open our database connection

    query1 = "SELECT Garden.garden_id AS id, Garden.description, Garden.location, \
              CONCAT(User.first_name, ' ', User.last_name) AS owner \
              FROM Garden JOIN User on Garden.user_id = User.user_id;"
    gardens = db.query(db_connection, query1).fetchall()

    query2 = "SELECT User.user_id, CONCAT(User.first_name, ' ', User.last_name) AS owner FROM User;"
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

# -------------- [ BED ] -------------- #
@app.route("/beds", methods=["GET"])
def beds():
  try:
    db_connection = db.connect_db()  # Open our database connection

    # Create and execute our queries
    
    # Query 1: Get all identifying information to populate the "View All Beds" table
    query1 = "SELECT Bed.bed_id AS id, Bed.label, Bed.length AS 'length (inches)', Bed.width AS 'width (inches)', Bed.garden_id AS garden FROM Bed;"
    beds = db.query(db_connection, query1).fetchall()

    # Query 2: Get all garden_id and location to populate the Garden dropdown
    query2 = "SELECT garden_id, location FROM Garden ORDER BY location;"
    gardens_dropdown = db.query(db_connection, query2).fetchall()

    # Render the file, and also send the renderer
    # a couple objects that contains information
    return render_template(
      "bed.j2", beds=beds, gardens_dropdown=gardens_dropdown
    )

  except Exception as e:
    print(f"Error executing queries: {e}")
    return(f"An error occurred while executing the database queries.", 500)

  finally:
    # Close the DB connection, if it exists
    if "db_connection" in locals() and db_connection:
        db_connection.close()

# -------------- [ PLANT IN BED ] -------------- #
@app.route("/plants-in-beds", methods=["GET"])
def plants_in_beds():
  try:
    db_connection = db.connect_db()  # Open our database connection

    # Create and execute our queries
    
    # Query 1: Get all identifying information to populate the "View All Of My Plants" table
    query1 = "SELECT Plant_in_Bed.plant_id AS id, Plant.species, Plant.plant_category AS 'plant category', \
        Plant_in_Bed.date_planted AS 'date planted', Plant_in_Bed.plant_quantity AS 'plant quantity', Bed.label AS bed \
        FROM Plant_in_Bed \
        INNER JOIN Plant ON Plant_in_Bed.plant_id = Plant.plant_id \
        INNER JOIN Bed ON Plant_in_Bed.bed_id = Bed.bed_id \
        ORDER BY id;"
    my_plants = db.query(db_connection, query1).fetchall()

    # Query 2: Get all bed_id and label to populate the Bed dropdown
    query2 = "SELECT bed_id, label FROM Bed ORDER BY label;"
    beds_dropdown = db.query(db_connection, query2).fetchall()

    # Query 3: Get all plant_id and species to populate the Plant dropdown
    query3 = "SELECT plant_id, species FROM Plant ORDER BY species;"
    plants_dropdown = db.query(db_connection, query3).fetchall()

    # Render the file, and also send the renderer
    # a couple objects that contains information
    return render_template(
      "plant_in_bed.j2", my_plants=my_plants, beds_dropdown=beds_dropdown, plants_dropdown=plants_dropdown
    )

  except Exception as e:
    print(f"Error executing queries: {e}")
    return(f"An error occurred while executing the database queries.", 500)

  finally:
    # Close the DB connection, if it exists
    if "db_connection" in locals() and db_connection:
        db_connection.close()

# Citation for use of AI Tools:
# Date: 2/09/2026
# Prompts used to generate flask routes
# Could you help me translate this into the flask routes:
# -- populate target plant's current data into Update Plant Form
# AI Source URL: https://gemini.google.com/
@app.route("/edit-plant-in-bed/<int:id>", methods=["GET"])
def edit_plant_in_bed(id):
    db_connection = None
    try:
        db_connection = db.connect_db()

        # The query uses %s as a placeholder for the ID
        query = "SELECT plant_id, bed_id, date_planted, plant_quantity \
                 FROM Plant_in_Bed \
                 WHERE id = %s;"
        
        # We pass the 'id' from the URL into the query execution
        # Note: (id,) is a tuple, which the database connector requires
        cursor = db.query(db_connection, query, (id,))
        plant_data = cursor.fetchone() # Use fetchone() since we only want one row

        # We also likely need these for the dropdowns in the update form
        query2 = "SELECT plant_id, species FROM Plant;"
        plants_dropdown = db.query(db_connection, query2).fetchall()

        query3 = "SELECT bed_id, label FROM Bed;"
        beds_dropdown = db.query(db_connection, query3).fetchall()

        return render_template(
            "update_plant_in_bed.j2", 
            plant_data = plant_data, 
            plants_dropdown=plants_dropdown, 
            beds_dropdown=beds_dropdown
        )

    except Exception as e:
        print(f"Error: {e}")
        return "Error fetching plant data.", 500
    finally:
        if db_connection:
            db_connection.close()

# -------------- [ USER ] -------------- #
@app.route("/users", methods=["GET"])
def users():
  try:
    db_connection = db.connect_db()  # Open our database connection

    # Create and execute our queries
    
    # Query 1: Get all identifying information to populate the "View All Of My Plants" table
    query = "SELECT User.user_id as id, User.first_name AS 'first name', User.last_name AS 'last name' FROM User"
    users = db.query(db_connection, query).fetchall()


    # Render the file, and also send the renderer
    # a couple objects that contains information
    return render_template(
      "user.j2", users=users
    )

  except Exception as e:
    print(f"Error executing queries: {e}")
    return(f"An error occurred while executing the database queries.", 500)

  finally:
    # Close the DB connection, if it exists
    if "db_connection" in locals() and db_connection:
        db_connection.close()

@app.route("/edit-user/<int:id>", methods=["GET"])
def edit_user(id):
    db_connection = None
    try:
        db_connection = db.connect_db()

        # The query uses %s as a placeholder for the ID
        query = "SELECT * \
                 FROM User \
                 WHERE user_id = %s;"
        
        # We pass the 'id' from the URL into the query execution
        # Note: (id,) is a tuple, which the database connector requires
        cursor = db.query(db_connection, query, (id,))
        user_data = cursor.fetchone() # Use fetchone() since we only want one row


        return render_template(
            "update_user.j2", 
            user_data = user_data, 
        )

    except Exception as e:
        print(f"Error: {e}")
        return "Error fetching plant data.", 500
    finally:
        if db_connection:
            db_connection.close()

# ########################################
# ########## LISTENER

if __name__ == "__main__":
  app.run(
    port=PORT, debug=True
  )
