#############################################################################
##              Local Setting for the Smart Tollbooth Project              ##
#############################################################################

import psycopg2

#+-----------------------------------------------------+#
#|                  DATABASE SETTING                   +#
#+-----------------------------------------------------+#

DATABASE_NAME = 'dbu2gkqs7vvmg4'
DATABASE_USER = 'yoiihmyyafmsxa'
DATABASE_HOST = 'ec2-107-21-248-129.compute-1.amazonaws.com'
DATABASE_PASSWORD = '7ca3dfd7f799afdafd8ccd7b1f63c6e76ef43899be7cb7c09f48d25e9ec97489'
DATABASE_STRING_FORM = "postgresql://{}:{}@{}:5432/{}"
DATABASE_STRING = DATABASE_STRING_FORM.format(DATABASE_USER, DATABASE_PASSWORD,
                                              DATABASE_HOST, DATABASE_NAME)

def getDatabaseString():
    return DATABASE_STRING
