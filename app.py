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


@app.route("/garden-planner", methods=["GET"])
def garden_planner():
  try:
    db_connection = db.connect_db()  # Open our database connection

    # Create and execute our queries
    # In query1, we use a JOIN clause to display the names of the homeworlds,
    #       instead of just ID values
    query1 = "SELECT Plant.plant_id, Plant.species, Plant.plant_category, \
        Plant.water_requirements, Plant.sunlight, Plant.season, Plant.cycle, Plant.edible \
        FROM Plant;"
    plants = db.query(db_connection, query1).fetchall()

    # Render the plant.j2 file, and also send the renderer
    # a couple objects that contains bsg_people and bsg_homeworld information
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



# ########################################
# ########## LISTENER

if __name__ == "__main__":
  app.run(
    port=PORT, debug=True
  )
