import pymongo

from pymongo import Connection
connection = Connection()

db = connection.test_database
print db

person = {"name":"Sam", "Age":24}

people = db.people
people.insert(person)

print "! " + str(people.find_one({"name":"Sam"}))
