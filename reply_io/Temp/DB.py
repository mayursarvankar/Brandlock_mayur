import psycopg2
import pandas as pd


class DB():

    def __init__(self):
        #brandlock conn
        # connection = psycopg2.connect(
        # host="brandlock-analytics.cml96yw8vdxq.us-west-2.rds.amazonaws.com",
        # database="marketing",
        # user="mayur",
        # password="Fse#4Hntfgj#$vs")

        #local conn

        self.connection = psycopg2.connect(
            host="localhost",
            database="demo_db",
            user="postgres",
            password="mayur@123")



        self.cursor = self.connection.cursor()

    def fetchAll(self):
        return self.cursor.fetchall()
    def fetchOne(self):
        return  self.cursor.fetchone()

    def executeQuerry(self,querry):
        return self.cursor.execute(querry)

    #     conn.commit()
    #     conn.close()

    def selectTable(self,tableName):

        selectingQuerry = f"SELECT * FROM {tableName}"

        self.executeQuerry(selectingQuerry)

        queryResult = self.fetchAll()

        for row in queryResult:
            print(row)

    def selectTableWhere(self,tableName,columnName,columnValue):

        selectingQuerry = f"SELECT * FROM {tableName} where {columnName} = {columnValue} "

        print(selectingQuerry)

        self.executeQuerry(selectingQuerry)

        queryResult = self.fetchAll()

        for row in queryResult:
            print(row)

    def insertTableRows(self,tableName,insertValueList):
        insertingQuerry= f"INSERT INTO {tableName}  VALUES {insertValueList};"

        self.executeQuerry(insertingQuerry)
        self.connection.commit()
        #     conn.close()



    def updateTableRows(self,tableName,updateColumnName,updateValue,whereColumnName,whereColumnNameValue):
        updatingQuerry = f''' update {tableName}  set {updateColumnName} = '{updateValue}' where {whereColumnName} = '{whereColumnNameValue}' ; '''

        self.executeQuerry(updatingQuerry)
        self.connection.commit()

    def deleteTableRows(self,tableName,deleteColumnName,deleteValue):
        deletingQuerry = f''' DELETE FROM {tableName} WHERE {deleteColumnName} = '{deleteValue}'; '''


        self.executeQuerry(deletingQuerry)
        self.connection.commit()




xy=DB().deleteTableRows(tableName="mtd_screenshot_may_2022",deleteColumnName="user_id",deleteValue="11111")
