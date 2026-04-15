from database.DB_connect import DBConnect
from model.retailer import Retailer


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

