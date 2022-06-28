import psycopg2
import pandas as pd


class load_postgr_data():
    def __init__(self):
        pass

    def connectionDb(self):
        conn_var = psycopg2.connect(
            host="brandlock-analytics.cml96yw8vdxq.us-west-2.rds.amazonaws.com",
            database="marketing",
            user="mayur",
            password="Fse#4Hntfgj#$vs")
        cursor_var =conn_var.cursor()
        return conn_var ,cursor_var


    def loadTable(self,tableName):


        conn,cursor=self.connectionDb()

        # cursor.execute("select * from currentbody_tb2 order by client_name ASC ")
        selectingQuerry= f"SELECT * FROM {tableName}"
        print(selectingQuerry)
        cursor.execute(selectingQuerry)
    #     conn.commit()
    #     conn.close()
        queryResult = cursor.fetchall()
        columnNames = [i[0] for i in cursor.description]
        # print(queryResult)
        # print(columnNames)

        df = pd.DataFrame(queryResult, columns=columnNames)
        print(df)







xv=load_postgr_data().loadTable(tableName="campaign")
print(xv)







# host: 'brandlock-analytics.cml96yw8vdxq.us-west-2.rds.amazonaws.com',
#         port: 5432,
#         user: 'mayur',
#         password: 'Fse#4Hntfgj#$vs',
#         database: 'marketing',
#         timezone: 'ist'