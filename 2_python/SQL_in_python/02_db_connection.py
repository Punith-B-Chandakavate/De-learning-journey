import psycopg2 as ps
from contextlib import contextmanager


# =========================================================
# DATABASE CONNECTION
# =========================================================

@contextmanager
def connect_to_db(commit=False):
    """
    Creates database connection and cursor.

    commit=True  -> saves INSERT/UPDATE/DELETE changes
    commit=False -> only for SELECT queries
    ----------------------------------------------
        This line creates a cursor object that allows us
        to execute SQL commands and fetch results as
        dictionaries instead of tuples.

        Each row returned from the database will be
        represented as a dictionary where:

            - keys   -> column names
            - values -> corresponding row values
        from psycopg2.extras import RealDictCursor
        cursor = connection.cursor(
            cursor_factory=RealDictCursor
        )
    ----------------------------------------------
    
    """

    connection = None
    cursor = None

    try:
        # Create database connection
        connection = ps.connect(
            host="localhost",
            database="movie_db",
            user="postgres",
            password="1234",
            port=5432
        )

        # Create cursor object
        cursor = connection.cursor()

        # Give cursor to the function using 'with'
        yield cursor

        # Save changes if needed
        if commit:
            connection.commit()

    except Exception as e:
        print("Database connection failed")
        print("Error:", e)

    finally:
        # Close cursor and connection safely
        if cursor:
            cursor.close()

        if connection:
            connection.close()


# =========================================================
# FETCH ALL MOVIES
# =========================================================

def fetch_all_movies():

    with connect_to_db() as cursor:

        query = "SELECT * FROM movies"

        cursor.execute(query)

        records = cursor.fetchall()

        print("\nAll Movies:\n")

        for row in records:
            print(row)


# =========================================================
# FETCH MOVIES BY RELEASE YEAR
# =========================================================

def fetch_movies_by_release_year(release_year):

    with connect_to_db() as cursor:

        query = """
            SELECT *
            FROM movies
            WHERE release_year = %s
        """

        cursor.execute(query, (release_year,))

        records = cursor.fetchall()

        print(f"\nMovies Released in {release_year}:\n")

        for row in records:
            print(row)


# =========================================================
# INSERT SINGLE MOVIE
# =========================================================

def insert_movie(
    title,
    release_year,
    imdb_rating,
    language_id,
    industry,
    studio
):

    with connect_to_db(commit=True) as cursor:

        query = """
            INSERT INTO movies
            (
                title,
                release_year,
                imdb_rating,
                language_id,
                industry,
                studio
            )

            VALUES (%s, %s, %s, %s, %s, %s)
        """

        values = (
            title,
            release_year,
            imdb_rating,
            language_id,
            industry,
            studio
        )

        cursor.execute(query, values)

        print("\nMovie inserted successfully")


# =========================================================
# INSERT MULTIPLE MOVIES
# =========================================================

def insert_multiple_movies():

    with connect_to_db(commit=True) as cursor:

        query = """
            INSERT INTO movies
            (
                title,
                release_year,
                imdb_rating,
                language_id,
                industry,
                studio
            )

            VALUES (%s, %s, %s, %s, %s, %s)
        """

        movie_list = [

            (
                "The Matrix",
                1999,
                8.7,
                1,
                "Hollywood",
                "Warner Bros"
            ),

            (
                "Inception",
                2010,
                8.8,
                1,
                "Hollywood",
                "Warner Bros"
            ),

            (
                "Interstellar",
                2014,
                8.6,
                1,
                "Hollywood",
                "Warner Bros"
            )
        ]

        cursor.executemany(query, movie_list)

        print("\nMultiple movies inserted successfully")


# =========================================================
# GET TABLE COLUMN NAMES
# =========================================================

def get_table_columns(table_name):

    with connect_to_db() as cursor:

        query = """
            SELECT column_name
            FROM information_schema.columns
            WHERE table_name = %s
        """

        cursor.execute(query, (table_name,))

        columns = cursor.fetchall()

        column_names = [col[0] for col in columns]

        print(f"\nColumns in '{table_name}' table:\n")

        print(column_names)


# =========================================================
# DELETE MOVIE
# =========================================================

def delete_movie(movie_id):

    with connect_to_db(commit=True) as cursor:

        query = """
            DELETE FROM movies
            WHERE movie_id = %s
        """

        cursor.execute(query, (movie_id,))

        print(f"\nMovie with ID {movie_id} deleted")


# =========================================================
# UPDATE MOVIE RATING
# =========================================================

def update_movie_rating(movie_id, new_rating):

    with connect_to_db(commit=True) as cursor:

        query = """
            UPDATE movies
            SET imdb_rating = %s
            WHERE movie_id = %s
        """

        values = (new_rating, movie_id)

        cursor.execute(query, values)

        print(f"\nMovie rating updated successfully")


# =========================================================
# MAIN PROGRAM
# =========================================================

if __name__ == "__main__":

    # Fetch all movies
    fetch_all_movies()

    # Fetch table columns
    get_table_columns("movies")

    # Fetch movies by release year
    fetch_movies_by_release_year(2022)

    # Insert one movie
    insert_movie(
        "Avatar",
        2009,
        7.8,
        1,
        "Hollywood",
        "20th Century Fox"
    )

    # Insert multiple movies
    insert_multiple_movies()

    # Delete movie
    delete_movie(101)

    # Update movie rating
    update_movie_rating(102, 9.0)