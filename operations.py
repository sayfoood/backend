import pandas as pd
from sqlalchemy import JSON
from models import comp,sp


#class binding functions related to mess incharge operations 
class MessOps(comp,sp):

    def disp_db(self):#displaying 
        df = pd.read_csv('./database/st_db.csv',index_col=['RollNo'])
        try:
            df = df.drop('Unnamed: 0',axis=1)
        except:
            return df
        else:
            return df

    def add_stu(self,roll_no,name,creds):#addition of data of newly enrolled student to "st_db.csv" 
        st_db = self.disp_db()
        st_db = st_db.reset_index()
        st_db = st_db.append(pd.DataFrame([[roll_no,name,creds]],columns=st_db.columns))
        st_db.to_csv('./database/st_db.csv')
        st_db = st_db.set_index('RollNo')
        return st_db

    def remove_stu(self, roll_no):#widthdrawl for admission and deletion of student data from "st_db.csv"
        st_db = self.disp_db()
        st_db = st_db.drop(roll_no)
        st_db.to_csv('./database/st_db.csv')
        return st_db


    def creds(self, roll_no,amt):#creds are equivalent to actual money in digital form , this funtion adds creds to student data 
        df = self.disp_db()
        curr_val = int(df.loc[roll_no]['creds'])
        df.at[roll_no,'creds']=curr_val+amt
        df.to_csv('./database/st_db.csv')
        return df


    def stu_order_history(self, roll_no):#history of orders made by student till date along with date and time of ordering 
        try:
            df = self.view_order_db()
            df.reset_index()
            df = df.set_index('Reg. No.')
            return df.loc[roll_no]
        except:
            print("Oops!! No order Found")

    def view_order_db(self):
        df = pd.read_csv('./database/orderdb.csv',index_col=['Order No.'])
        try:
            df = df.drop('Unnamed: 0',axis=1)
        except:
            return df
        else:
            return df


#class for binding function definations for student operations 
class studOps(comp):

    def view_order_db(self):
        df = pd.read_csv('./database/orderdb.csv',index_col=['Order No.'])
        try:
            df = df.drop('Unnamed: 0',axis=1)
        except:
            return df
        else:
            return df

    def disp_db(self):
        df = pd.read_csv('./database/st_db.csv',index_col=['RollNo'])
        try:
            df = df.drop('Unnamed: 0',axis=1)
        except:
            return df
        else:
            return df
    def view_order_db(self):
        df = pd.read_csv('./database/orderdb.csv',index_col=['Order No.'])
        try:
            df = df.drop('Unnamed: 0',axis=1)
        except:
            return df
        else:
            return df


    def view_menu_db(self) -> JSON:
        menu_db = pd.read_csv('./database/menu_db.csv',index_col=['Id'])
        return menu_db

    def order_amt(self, order_id):
        menu_db = self.view_menu_db()
        return float(menu_db.loc[order_id]['Price'])

    def debit(self, roll_no,amt):
        df = self.disp_db()
        curr_val = int(df.loc[roll_no]['creds'])
        if(curr_val>100):
            df.at[roll_no,'creds'] = (curr_val-amt)
        else:
            print("Sorry, Insufficient Credit Balance")
        df.to_csv('./database/st_db.csv')
        return df

    def stu_det(self, roll_no):
        df = self.disp_db()
        return df.loc[roll_no]

    def add_order(self, order_no,time,roll_no,order,amt):
        df = self.view_order_db()
        df = df.reset_index()
        df = df.append(pd.DataFrame([[order_no,time,roll_no,order,amt]],columns=df.columns))
        df.to_csv('./database/orderdb.csv')
        df = df.set_index('Order No.')
        return df