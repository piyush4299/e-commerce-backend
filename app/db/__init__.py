from .mongodb import connect_to_database, close_database_connection

# Exporting the functions to be accessible from outside the package
__all__ = ["connect_to_database", "close_database_connection"]