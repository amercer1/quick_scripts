import json

serialized = """{ "title" : "My Book",
                  "author" : "me",
                  "publicationYear" : 2015,
                  "topics" : [ "data", "sports", "Andre"] } """

deserialized = json.loads(serialized)
if "data" in deserialized["topics"]:
    print(deserialized)
