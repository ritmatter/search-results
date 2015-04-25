from pymongo import MongoClient
import loader

# Creates interactive command line search for search history
# Sets up search results database if it does not exist already

print "Connecting to database..."
client = MongoClient();
db = client.search_results;
if (db.results.count() == 0):
    print "Empty database found. Configuring database..."
    loader.write_db()

while True:
    var = raw_input("\nEnter query text: ")
    query = ".*" +  var + ".*"
    results = db.results.find({ "text": { "$regex": query }})
    for i in results:
      print str(i["date"]) + ", " + i["text"]
