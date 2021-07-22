import pymongo
import certifi
from pprint import pprint

CONNECTION_STRING = "mongodb+srv://AdinaAdm:SpulBly5BuiSKD0m@cluster0.0squg.gcp.mongodb.net/Adina2021"
# "mongodb+srv://AdinaAdm:SpulBly5BuiSKD0m@cluster0.0squg.gcp.mongodb.net/Adina2021?retryWrites=true&w=majority"

client = pymongo.MongoClient(CONNECTION_STRING, tlsCAFile=certifi.where())
print(type(client))
print(client.list_database_names())
db=client.Adina2021
#serverStatusResult=db.command("serverStatus")
#pprint(serverStatusResult)




