import psycopg2
import pandas as pd


class load_postgr_data():
    def __init__(self):
        pass

    def connection_db(self):
        conn_var = psycopg2.connect(
            host="localhost",
            database="demo_db",
            user="postgres",
            password="mayur@123")
        cursor_var =conn_var.cursor()
        return conn_var ,cursor_var

    def create_table(self,table_name):

        conn, cursor = self.connection_db()



        try:
            creating_querry=f"CREATE TABLE MTD_Screenshot_{table_name}( user_id VARCHAR ( 50 )," \
                            f" Screenshot_path VARCHAR ," \
                            f" adware_path VARCHAR ," \
                            f" Screenshot_method VARCHAR ( 50 ) ," \
                            f"Date_capture VARCHAR ( 50)  ) "

            cursor.execute(creating_querry)
            conn.commit()
            conn.close()
            print(f'Sql_table : MTD_Screenshot_{table_name} created !')
        except psycopg2.Error  as e:
            # print(repr(e))
            print(f'Sql_table : MTD_Screenshot_{table_name} already created !')


    def load_table(self,id,adware_ss_path,ss_path,ss_meth,date,table_name):


        conn,cursor=self.connection_db()

        # cursor.execute("select * from currentbody_tb2 order by client_name ASC ")
        inserting_querry=f"insert into  MTD_Screenshot_{table_name} (user_id,adware_path,Screenshot_path,Screenshot_method,Date_capture) values ( '{id}','{adware_ss_path}','{ss_path}','{ss_meth}','{date}')"
        # print(inserting_querry)
        cursor.execute(inserting_querry)
        conn.commit()
        conn.close()
        # GGB_query = cursor.fetchall()
        # print(GGB_query)





# xv= load_postgr_data().create_table("MTD_Screenshot_2")
# xv2=load_postgr_data().load_table("111","C:\\Users\\Admin\\PycharmProjects\\db_conection_screenshot\\seclectors_present_images\\123.png","ali_present","2020-03-123","may_2")
