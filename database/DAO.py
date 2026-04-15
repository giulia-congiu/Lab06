from database.DB_connect import DBConnect


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
        query = """SELECT distinct YEAR(date) as anno
                        FROM go_daily_sales;"""
        cursor.execute(query)

        res = []
        for row in cursor:
            res.append(row["anno"])

        cursor.close()
        cnx.close()
        return res