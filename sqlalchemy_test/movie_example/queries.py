# 1 - imports
from datetime import date, datetime, timedelta

from actor import Actor
from base import Session, engine
from contact_details import ContactDetails
from movie import Movie
from sqlalchemy.dialects import mssql, mysql, oracle, postgresql, sqlite
from sqlalchemy.orm import Query

try:
    basestring
except NameError:
    basestring = str

from sqlalchemy.orm import Query


def render_query(statement, db_session):
    """
    Generate an SQL expression string with bound parameters rendered inline
    for the given SQLAlchemy statement.
    WARNING: This method of escaping is insecure, incomplete, and for debugging
    purposes only. Executing SQL statements with inline-rendered user values is
    extremely insecure.
    Based on http://stackoverflow.com/questions/5631078/sqlalchemy-print-the-actual-query
    """
    if isinstance(statement, Query):
        statement = statement.statement
    dialect = db_session.bind.dialect

    class LiteralCompiler(dialect.statement_compiler):
        def visit_bindparam(
            self, bindparam, within_columns_clause=False, literal_binds=False, **kwargs
        ):
            return self.render_literal_value(bindparam.value, bindparam.type)

        def render_array_value(self, val, item_type):
            if isinstance(val, list):
                return "{}".format(
                    ",".join([self.render_array_value(x, item_type) for x in val])
                )
            return self.render_literal_value(val, item_type)

        def render_literal_value(self, value, type_):
            if isinstance(value, int):
                return str(value)
            elif isinstance(value, (str, date, datetime, timedelta)):
                return "'{}'".format(str(value).replace("'", "''"))
            elif isinstance(value, list):
                return "'{{{}}}'".format(
                    ",".join(
                        [self.render_array_value(x, type_.item_type) for x in value]
                    )
                )
            return super(LiteralCompiler, self).render_literal_value(value, type_)

    return LiteralCompiler(dialect, statement).process(statement)


def render_query(statement, db_session):
    """
    Generate an SQL expression string with bound parameters rendered inline
    for the given SQLAlchemy statement.
    WARNING: This method of escaping is insecure, incomplete, and for debugging
    purposes only. Executing SQL statements with inline-rendered user values is
    extremely insecure.
    Based on http://stackoverflow.com/questions/5631078/sqlalchemy-print-the-actual-query
    """
    if isinstance(statement, Query):
        statement = statement.statement
    dialect = db_session.bind.dialect

    class LiteralCompiler(dialect.statement_compiler):
        def visit_bindparam(
            self, bindparam, within_columns_clause=False, literal_binds=False, **kwargs
        ):
            return self.render_literal_value(bindparam.value, bindparam.type)

        def render_array_value(self, val, item_type):
            if isinstance(val, list):
                return "{%s}" % ",".join(
                    [self.render_array_value(x, item_type) for x in val]
                )
            return self.render_literal_value(val, item_type)

        def render_literal_value(self, value, type_):
            if isinstance(value, int):
                return str(value)
            elif isinstance(value, (basestring, date, datetime, timedelta)):
                return "'%s'" % str(value).replace("'", "''")
            elif isinstance(value, list):
                return "'{%s}'" % (
                    ",".join(
                        [self.render_array_value(x, type_.item_type) for x in value]
                    )
                )
            return super(LiteralCompiler, self).render_literal_value(value, type_)

    return LiteralCompiler(dialect, statement).process(statement)


# 2 - extract a session
session = Session()

filter1 = Movie.release_date > date(2015, 1, 1)
query1 = session.query(Movie).filter(Movie.release_date > date(2015, 1, 1)).limit(2)


render_query(query1, session)
render_query(query1, oracle)
render_query(query1, mssql)
render_query(query1, mysql)
render_query(query1, sqlite)
# 3 - extract all movies
movies = session.query(Movie).all()

# 4 - print movies' details
print("\n### All movies:")
for movie in movies:
    print(f"{movie.title} was released on {movie.release_date}")
print("")

# 5 - get movies after 15-01-01
movies = session.query(Movie).filter(Movie.release_date > date(2015, 1, 1)).all()

print("### Recent movies:")
for movie in movies:
    print(f"{movie.title} was released after 2015")
print("")

# 6 - movies that Dwayne Johnson participated
the_rock_movies = (
    session.query(Movie)
    .join(Actor, Movie.actors)
    .filter(Actor.name == "Dwayne Johnson")
    .all()
)

print("### Dwayne Johnson movies:")
for movie in the_rock_movies:
    print(f"The Rock starred in {movie.title}")
print("")

# 7 - get actors that have house in Glendale
glendale_stars = (
    session.query(Actor)
    .join(ContactDetails)
    .filter(ContactDetails.address.ilike("%glendale%"))
    .all()
)

print("### Actors that live in Glendale:")
for actor in glendale_stars:
    print(f"{actor.name} has a house in Glendale")
print("")
