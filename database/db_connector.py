import MySQLdb

# Database credentials
# host = 'classmysql.engr.oregonstate.edu'
host = 'localhost'
# user = 'cs340_tavi'
user = 'root'
# passwd = '5jHQlf5bdzQX'
passwd = ''
db = 'cs340_tavi'

def connect_db(host=host, user=user, passwd=passwd, db=db):
  '''
  connects to a database and returns a database object
  '''
  db_connection = MySQLdb.connect(host, user, passwd, db)
  return db_connection

def query(db_connection=None, query=None, query_params=()):
  '''
  executes a given SQL query on the given db connection and returns a Cursor object
  db_connection: a MySQLdb connection object created by connectDB()
  query: string containing SQL query
  returns: A Cursor object as specified at https://www.python.org/dev/peps/pep-0249/#cursor-objects.
  You need to run .fetchall() or .fetchone() on that object to actually acccess the results.
  '''

  if db_connection is None:
    print("No connection to the database found! Have you called connect_db() first?")
    return None

  if query is None or len(query.strip()) == 0:
    print("query is empty! Please pass a SQL query in query")
    return None

  print("Executing %s with %s" % (query, query_params));
  # Create a cursor to execute query. Why? Because apparently they optimize execution by retaining a reference according to PEP0249
  cursor = db_connection.cursor(MySQLdb.cursors.DictCursor)

  # Sanitize the query before executing it.
  cursor.execute(query, query_params)
  
  # Commit any changes to the database.
  db_connection.commit()
  
  return cursor
