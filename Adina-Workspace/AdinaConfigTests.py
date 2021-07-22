from com.adina.mongoDB.MongoDBObject import MongoDBObject
from com.adina.utilities.Utilities import Utilities
from com.adina.config.config import Configuration

"""
adinaConfiguration = Configuration()
print(adinaConfiguration.appPath)
print(adinaConfiguration.logPath)
print(type(adinaConfiguration.getLoggingNames))
print(adinaConfiguration.getLoggingNames)
print(adinaConfiguration.getLogger("MongoDB"))
mongoLogger = adinaConfiguration.getLogger("MongoDB")
mongoLogger.logger.debug("Debug - Mensaje de Mongo")
mongoLogger.logger.info("Info - Mensaje de Mongo")
mongoLogger.logger.warn("Warn - Mensaje de Mongo")
mongoLogger.logger.error("Error - Mensaje de Mongo")
mongoLogger.logger.fatal("Fatal - Mensaje de Mongo")
"""

#"""
# "mongodb+srv://AdinaAdm:SpulBly5BuiSKD0m@cluster0.0squg.gcp.mongodb.net"
mongoServerOne = MongoDBObject("MongoServerOne")
print(type(mongoServerOne))
print(mongoServerOne.mongoClient().list_database_names())
print(mongoServerOne.connectToDatabase("Adina2021"))
print(mongoServerOne.connectedDataBase().name)
print(mongoServerOne.showCollections())
mongoServerOne.mongoDBlogger.debug("Linea de Debug")
mongoServerOne.mongoDBlogger.info("Linea de Info")
mongoServerOne.mongoDBlogger.warn("Linea de Warn")
mongoServerOne.mongoDBlogger.error("Linea de Error")
mongoServerOne.mongoDBlogger.fatal("Linea de Fatal")
#"""

#"""
utilities = Utilities()
print(utilities.rootPath)
utilities.debug("Debug message")
utilities.info("Info message")
utilities.warn("Warn message")
utilities.error("Error message")
utilities.fatal("Fatal message")
#"""