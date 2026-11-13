import psycopg2


def get_connection():
    connection = psycopg2.connect('postgresql://admin_ilyas:12345@localhost/demo')
    return connection

