#############################################################################
##              Local Setting for the Smart Tollbooth Project              ##
#############################################################################

import psycopg2

#+-----------------------------------------------------+#
#|                  DATABASE SETTING                   +#
#+-----------------------------------------------------+#

DATABASE_NAME = 'YOUR DATABASE NAME'
DATABASE_USER = 'YOUR DATABASE USER'
DATABASE_HOST = 'YOUR DATABASE HOST'
DATABASE_PASSWORD = 'YOUR DATABASE PASSWORD'
DATABASE_STRING_FORM = "postgresql://{}:{}@{}:5432/{}"
DATABASE_STRING = DATABASE_STRING_FORM.format(DATABASE_USER, DATABASE_PASSWORD,
                                              DATABASE_HOST, DATABASE_NAME)

def getDatabaseString():
    return DATABASE_STRING
