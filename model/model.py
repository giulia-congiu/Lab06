from database.DAO import DAO

class Model:
    def __init__(self):
        pass

    def getAnno(self):
        return DAO.getAnno()

    def getBrand(self):
        brand = DAO.getBrand()
        brand.sort()
        return brand

    def getRetailer(self):
        retailers =  DAO.getRetailer()
        retailers.sort(key=lambda r: r.Retailer_name)
        return retailers

    def getSales(self, anno, brand, retailer):
        sales= DAO.getSales(anno, brand, retailer)
        sales.sort(key=lambda s: s.ricavo, reverse=True)
        return sales[:5] #restituisco solo le prime 5

    def getSalestot(self, anno, brand, retailer):
        sales = DAO.getSales(anno, brand, retailer)
        sales.sort(key=lambda s: s.ricavo, reverse=True)
        return sales