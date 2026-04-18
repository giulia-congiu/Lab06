from database.DB_connect import DBConnect
from model.retailer import Retailer
from model.sales import Sales


class DAO():
    def __init__(self):
        pass

    @staticmethod
    def getAnno():
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """SELECT distinct YEAR(date) as anno
                    FROM go_daily_sales;"""
        cursor.execute(query)

        res = []
        for row in cursor:
            res.append(row["anno"])

        cursor.close()
        cnx.close()
        return res

    @staticmethod
    def getBrand():
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """SELECT distinct Product_brand as brand
                        FROM go_products;"""
        cursor.execute(query)

        res = []
        for row in cursor:
            res.append(row["brand"])

        cursor.close()
        cnx.close()
        return res

    @staticmethod
    def getRetailer():
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """SELECT * FROM go_retailers;"""
        cursor.execute(query)

        res = []
        for row in cursor:
            res.append(Retailer(**row))

        cursor.close()
        cnx.close()
        return res

    @staticmethod
    def getSales(anno, brand, retailer):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """SELECT s.Retailer_code , s.Product_number , s.Date, s.Quantity , s.Unit_sale_price 
                    FROM go_daily_sales s, go_products p
                    where s.Product_number = p.Product_number 
                    AND YEAR(s.Date) = COALESCE(%s, YEAR(s.Date))
                    AND p.Product_brand = COALESCE(%s, p.Product_brand)
                    AND s.Retailer_code = COALESCE(%s, s.Retailer_code)"""
        cursor.execute(query, (anno, brand, retailer)) #I %s nella query sono dei segnaposto
        # cursor.execute li sostituisce nell'ordine con i valori della tupla (anno, brand, retailer_code)

        res = []
        for row in cursor:
            res.append(Sales(**row))

        cursor.close()
        cnx.close()
        return res