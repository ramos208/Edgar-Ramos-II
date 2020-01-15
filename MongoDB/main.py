import pymongo
from pymongo import MongoClient

# cluster = MongoClient ("mongodb+srv://edgar208:ramos208@cluster0-vyw5y.mongodb.net/test?retryWrites=true&w=majority")
cluster = MongoClient ("localhost:27017")
db = cluster["test"]
collection = db["test"]


post = {"name": "edgar", "score": 2}
post2 = {"_id": 2, "name": "edgar", "score": 5}
"""=================== Insert Item ================= """
""" insert Once """
# collection.insert_one(post)
""" insert Many """
# collection.insert_many([post,post2])

""" Query """

# """ print all data by like a dictionary """
# results_all = collection.find({})
# print(results_all)
#
# for x in results_all:
#     print(x)

# """     print one data     """
# results = collection.find_one({"name":"edgar"})
# print(results)

# results2 = collection.find({"name":"edgar"})
# print(results2)
#
# """ convert to String   """
# for result in results2:
#
#     print(result)
#     """ Result """
#     # {'_id': 0, 'name': 'edgar', 'score': 5}
#
#     """ By Column """
#     print(result["_id"])
#     """ Result """
#     # 0

""" Delete item """

""" delete one """
# delete = collection.delete_one({"score": 2})
"""  find and delete """
# delete = collection.find_one_and_delete({"_id": 2})
"""  delete many """
# delete = collection.delete_many({"score": 2})
""" delete all """
# delete = collection.delete_many({})

""" Update """
# update = collection.update_one({"score": 10},{"$set":{"score": 2}})
""" upadate and add new field """
# update = collection.update_many({"score": 10},{"$set":{"new field": 20}})

# """ Count item """
# count = collection.count_documents({"score":10})
# """ count all """
# count = collection.count_documents({})
# print(count)



