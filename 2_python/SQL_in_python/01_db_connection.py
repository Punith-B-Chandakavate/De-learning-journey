import psycopg2 as ps
from psycopg2.extras import RealDictCursor


# =========================================================
# DATABASE CONNECTION
# =========================================================

def connect_to_db():
    """
    Creates and returns a database cursor.

    RealDictCursor returns query results as dictionaries
    instead of tuples.

    Example:
        {
            'movie_id': 1,
            'title': 'Interstellar'
        }
    """

    try:

        # Create PostgreSQL connection
        connection = ps.connect(
            host="localhost",
            database="movie_db",
            user="postgres",
            password="1234",
            port=5432
        )

        # Create cursor object
        cursor = connection.cursor(
            cursor_factory=RealDictCursor
        )

        print("Connected to database successfully")

        return connection, cursor

    except Exception as e:

        print("Database connection failed")
        print("Error:", e)

        return None, None


# =========================================================
# FETCH ALL MOVIES
# =========================================================

def fetch_all_movies():

    connection, cursor = connect_to_db()

    if not cursor:
        return

    try:

        query = "SELECT * FROM movies"

        cursor.execute(query)

        records = cursor.fetchall()

        print("\nAll Movies:\n")

        for row in records:
            print(row)

    except Exception as e:

        print("Error fetching movies")
        print(e)

    finally:

        cursor.close()
        connection.close()


# =========================================================
# FETCH MOVIES BY RELEASE YEAR
# =========================================================

def fetch_movies_by_release_year(release_year):

    connection, cursor = connect_to_db()

    if not cursor:
        return

    try:

        query = """
            SELECT *
            FROM movies
            WHERE release_year = %s
        """

        cursor.execute(query, (release_year,))

        records = cursor.fetchall()

        print(f"\nMovies released in {release_year}:\n")

        for row in records:
            print(row)

    except Exception as e:

        print("Error fetching movies")
        print(e)

    finally:

        cursor.close()
        connection.close()


# =========================================================
# MAIN PROGRAM
# =========================================================

if __name__ == "__main__":

    # Fetch all movies
    fetch_all_movies()

    # Fetch movies by release year
    fetch_movies_by_release_year(2022)