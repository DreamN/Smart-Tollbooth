#############################################################################
##              Local Setting for the Smart Tollbooth Project              ##
#############################################################################

import psycopg2

#+-----------------------------------------------------+#
#|                  DATABASE SETTING                   +#
#+-----------------------------------------------------+#

DATABASE_NAME = 'smarttb'
DATABASE_USER = 'pjuser'
DATABASE_HOST = 'localhost'
DATABASE_PASSWORD = 'random'
DATABASE_STRING_FORM = "postgresql://{}:{}@{}:5432/{}"
DATABASE_STRING = DATABASE_STRING_FORM.format(DATABASE_USER, DATABASE_PASSWORD,
                                              DATABASE_HOST, DATABASE_NAME)

def getDatabaseString():
    return DATABASE_STRING
