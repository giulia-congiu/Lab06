from database.DAO import DAO

class Model:
    def __init__(self):
        pass

    def getAnno(self):
        return DAO.getAnno()

    def getBrand(self):
        return DAO.getBrand()

    def getRetailer(self):
        return DAO.getRetailer()
