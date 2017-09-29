from pymongo import MongoClient
client=MongoClient('localhost', 27017)
db=client.jmdatabase
collection=db.dyskografia

d1={"_id": "plyta1","nazwa":"Room for Squares", "rok": "5 lipca 2001", "wytwornia": "Aware, Columbia"}
d2={"_id": "plyta2", "nazwa": "Heavier Things", "rok": "9 luty 2003", "wytwornia":"Aware, Columbia"}
d3={"_id": "plyta3", "nazwa": "Continuum", "rok":"4 listopad 2006", "wytwornia":"Aware, Columbia"}
d4={"_id": "plyta4", "nazwa":"Battle Studies", "rok":"17 listopad 2009", "wytwornia": "Columbia"}
d5={"_id": "plyta5", "nazwa":"Born and raised", "rok":"22 maj 2012", "wytwornia":"Columbia"}
d6={"_id": "plyta6", "nazwa":"Paradise Valley", "rok":"19 czerwiec 2013", "wytwornia":"Columbia"}

dane=[d1,d2,d3,d4,d5,d6]

for x in dane:
	collection.insert_one(x)
