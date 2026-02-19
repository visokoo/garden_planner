# ########################################
# ########## SETUP

# All code is based on the CS340 starter code, with the exception of the actual queries
# used for querying the DB or otherwise noted.

from flask import Flask, render_template, request, redirect, url_for
import database.db_connector as db

PORT = 8000

app = Flask(__name__)

# ########################################
# ########## ROUTE HANDLERS

#   _    _  ____  __  __ ______ 
#  | |  | |/ __ \|  \/  |  ____|
#  | |__| | |  | | \  / | |__   
#  |  __  | |  | | |\/| |  __|  
#  | |  | | |__| | |  | | |____ 
#  |_|  |_|\____/|_|  |_|______|                             

# READ ROUTES
@app.route("/", methods=["GET"])
def home():
  try:
    return render_template("home.j2")

  except Exception as e:
    print(f"Error rendering page: {e}")
    return "An error occurred while rendering the page.", 500

#   _____  _               _   _ _______ 
#  |  __ \| |        /\   | \ | |__   __|
#  | |__) | |       /  \  |  \| |  | |   
#  |  ___/| |      / /\ \ | . ` |  | |   
#  | |    | |____ / ____ \| |\  |  | |   
#  |_|    |______/_/    \_\_| \_|  |_|             

@app.route("/plants", methods=["GET", "POST"])
def plants():
  try:
    db_connection = db.connect_db()  # Open our database connection
    query1 = "SELECT Plant.plant_id AS id, Plant.species, Plant.plant_category AS 'plant category', Plant.water_requirements AS 'water requirements', \
              Plant.sunlight, Plant.season, Plant.cycle, Plant.edible FROM Plant;"

    if request.method == "POST":
      species = request.form.get('create_plant_species')
      plant_category = request.form.get('create_plant_category')
      water_requirements = request.form.get('create_water_requirements')
      sunlight = request.form.get('create_sunlight')
      season = request.form.get('create_season')
      cycle = request.form.get('create_cycle')
      edible = request.form.get('edible')
      cursor = db_connection.cursor()
      cursor.callproc('sp_insert_into_plant', [species, plant_category, water_requirements, sunlight, season, cycle, edible, 0]) # 0 is a placeholder for the returned id
      db_connection.commit()
      return redirect(url_for("plants"))

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

#    _____          _____  _____  ______ _   _ 
#   / ____|   /\   |  __ \|  __ \|  ____| \ | |
#  | |  __   /  \  | |__) | |  | | |__  |  \| |
#  | | |_ | / /\ \ |  _  /| |  | |  __| | . ` |
#  | |__| |/ ____ \| | \ \| |__| | |____| |\  |
#   \_____/_/    \_\_|  \_\_____/|______|_| \_|
                                                                         
@app.route("/gardens", methods=["GET", "POST"])
def gardens():
  try:
    db_connection = db.connect_db()  # Open our database connection
    query1 = "SELECT Garden.garden_id AS id, Garden.description, Garden.location, \
             CONCAT(User.first_name, ' ', User.last_name) AS owner \
             FROM Garden JOIN User on Garden.user_id = User.user_id;"
    query2 = "SELECT User.user_id, CONCAT(User.first_name, ' ', User.last_name) AS owner FROM User;"

    if request.method == "POST":
      description = request.form.get('create_garden_description')
      location = request.form.get('create_garden_location')
      user_name = request.form.get('create_garden_owner')
      cursor = db_connection.cursor()
      cursor.callproc('sp_insert_into_garden', [description, location, user_name, 0]) # 0 is a placeholder for the returned id
      db_connection.commit()
      return redirect(url_for("gardens"))

    gardens = db.query(db_connection, query1).fetchall()
    users = db.query(db_connection, query2).fetchall()

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

#   ____  ______ _____  
#  |  _ \|  ____|  __ \ 
#  | |_) | |__  | |  | |
#  |  _ <|  __| | |  | |
#  | |_) | |____| |__| |
#  |____/|______|_____/ 
                                
@app.route("/beds", methods=["GET", "POST"])
def beds():
  try:
    db_connection = db.connect_db()  # Open our database connection
    query1 = "SELECT Bed.bed_id AS id, Bed.label, Bed.length AS 'length (inches)', Bed.width AS 'width (inches)', Bed.garden_id AS garden FROM Bed;"
    query2 = "SELECT garden_id, location FROM Garden ORDER BY location;"

    if request.method == "POST":
      label = request.form.get('create_bed_label')
      length = request.form.get('create_bed_length')
      width = request.form.get('create_bed_width')
      garden_id = request.form.get('create_bed_garden')
      cursor = db_connection.cursor()
      cursor.callproc('sp_insert_into_bed', [label, length, width, garden_id, 0]) # 0 is a placeholder for the returned id
      db_connection.commit()
      return redirect(url_for("beds"))

    beds = db.query(db_connection, query1).fetchall()
    gardens_dropdown = db.query(db_connection, query2).fetchall()

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

#   _____  _               _   _ _______   _____ _   _   ____  ______ _____  
#  |  __ \| |        /\   | \ | |__   __| |_   _| \ | | |  _ \|  ____|  __ \ 
#  | |__) | |       /  \  |  \| |  | |      | | |  \| | | |_) | |__  | |  | |
#  |  ___/| |      / /\ \ | . ` |  | |      | | | . ` | |  _ <|  __| | |  | |
#  | |    | |____ / ____ \| |\  |  | |     _| |_| |\  | | |_) | |____| |__| |
#  |_|    |______/_/    \_\_| \_|  |_|    |_____|_| \_| |____/|______|_____/ 

# Citation for use of AI Tools:
# Date: 2/19/2026
# Prompts used to generate flask routes:
# I need help refactoring the Insert route to utilize cursor.nextset() to consume result sets from MySQL stored procedures in Python.
# AI Source URL: https://gemini.google.com/                                                                                                                                                   
@app.route("/plants-in-beds", methods=["GET", "POST"])
def plants_in_beds():
  try:
    db_connection = db.connect_db()  # Open our database connection
    query1 = "SELECT Plant_in_Bed.id AS id, Plant.species, Plant.plant_category AS 'plant category', \
        Plant_in_Bed.date_planted AS 'date planted', Plant_in_Bed.plant_quantity AS 'plant quantity', Bed.label AS bed \
        FROM Plant_in_Bed \
        INNER JOIN Plant ON Plant_in_Bed.plant_id = Plant.plant_id \
        INNER JOIN Bed ON Plant_in_Bed.bed_id = Bed.bed_id \
        ORDER BY id;"
    query2 = "SELECT bed_id, label FROM Bed ORDER BY label;"
    query3 = "SELECT plant_id, species FROM Plant ORDER BY species;"

    if request.method == "POST":
      plant = request.form.get('create_plant_species')
      bed = request.form.get('create_plant_bed')
      date_planted = request.form.get('create_date_planted')
      plant_quantity = request.form.get('create_plant_quantity')
        
      cursor = db_connection.cursor()
        
      # 1. Call the procedure
      # Note: Ensure the list matches the number of IN parameters in your SQL
      cursor.callproc('sp_insert_into_plant_in_bed', [plant, bed, date_planted, plant_quantity, 0])
        
      # 2. Consume results to prevent "Commands out of sync"
      while cursor.nextset():
            pass
            
      # 3. Commit the transaction
      db_connection.commit()
        
      # 4. Close cursor to be tidy
      cursor.close()  
      return redirect(url_for("plants_in_beds"))
    
    my_plants = db.query(db_connection, query1).fetchall()
    beds_dropdown = db.query(db_connection, query2).fetchall()
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
        return "Error updating plant data.", 500
    finally:
        if db_connection:
            db_connection.close()

# Citation for use of AI Tools:
# Date: 2/19/2026
# Prompts used to generate flask routes:
# 1. Help me write a flask app route to delete a plant from plant_in_bed using a stored procedure.
# 2. I need help writing a delete route for the plant-in-bed object (refactoring existing table and route code).
# 3. I need help troubleshooting MySQL Error 1305 (Procedure does not exist) and Error 2014 (Commands out of sync).
# AI Source URL: https://gemini.google.com/
@app.route("/delete-plant-in-bed/<int:id>", methods=["POST"])
def delete_plant_in_bed(id):
    db_connection = None
    try:
        db_connection = db.connect_db()
        cursor = db_connection.cursor()

        # 1. Call the procedure
        cursor.callproc('sp_delete_plant_in_bed', [id])
        
        # 2. CONSUME the results (This fixes the 'out of sync' error)
        # This loops through any SELECT statements inside your procedure
        while cursor.nextset():
            pass

        # 3. Commit after clearing results
        db_connection.commit()

        # 4. Close cursor to be tidy
        cursor.close()  
        
        return redirect("/plants-in-beds")

    except Exception as e:
        print(f"Error: {e}")
        return f"Error deleting plant with ID {id}.", 500
    finally:
        if db_connection:
            db_connection.close()

#   _    _  _____ ______ _____  
#  | |  | |/ ____|  ____|  __ \ 
#  | |  | | (___ | |__  | |__) |
#  | |  | |\___ \|  __| |  _  / 
#  | |__| |____) | |____| | \ \ 
#   \____/|_____/|______|_|  \_\
                                         
@app.route("/users", methods=["GET", "POST"])
def users():
  try:
    db_connection = db.connect_db()  # Open our database connection
    query = "SELECT User.user_id as id, User.first_name AS 'first name', User.last_name AS 'last name' FROM User"

    if request.method == "POST":
      first_name = request.form.get('create_user_first_name')
      last_name = request.form.get('create_user_last_name')
      cursor = db_connection.cursor()
      cursor.callproc('sp_insert_into_user', [first_name, last_name, 0]) # 0 is a placeholder for the returned id
      db_connection.commit()

    users = db.query(db_connection, query).fetchall()

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
        return "Error fetching user data.", 500
    finally:
        if db_connection:
            db_connection.close()

#   _____  ______  _____ ______ _______ 
#  |  __ \|  ____|/ ____|  ____|__   __|
#  | |__) | |__  | (___ | |__     | |   
#  |  _  /|  __|  \___ \|  __|    | |   
#  | | \ \| |____ ____) | |____   | |   
#  |_|  \_\______|_____/|______|  |_|   
                                                                    
@app.route("/reset", methods=["GET"])
def reset():
    db_connection = None
    try:
        db_connection = db.connect_db()

        query = "CALL sp_load_garden_planner_db();"
        
        db.query(db_connection, query)
        return redirect("/")

    except Exception as e:
        print(f"Error: {e}")
        return "Error resetting DB.", 500
    finally:
        if db_connection:
            db_connection.close()

# ########################################
# ########## LISTENER

if __name__ == "__main__":
  app.run(
    port=PORT, debug=True
  )
