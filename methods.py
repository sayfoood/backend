from os import path
from time import ctime
from flask import jsonify
import pandas as pd
from sqlalchemy import JSON
from models import comp, cooking
from operations import MessOps,studOps

def disp_db():
    df = pd.read_csv('./database/st_db.csv',index_col=['RollNo'])
    try:
        df = df.drop('Unnamed: 0',axis=1)
    except:
        return df
    else:
        return df

def __initial_cookdb():
    cook_db = pd.DataFrame(columns=['Cook_id','Name','Item','Quantity'])
    cook_db.to_csv('./database/cook_db.csv')

def __initial_cook():
    cook = cooking()
    cook.add_cook('MS19901','Chintu Kumar','Ogra','1kg')
    cook.add_cook('MS19902','Sampath Singh','Potato','2kg')
    cook.add_cook('MS19903','Surya Dev','Onion','2kg')
    cook.add_cook('MS19904','Ganesh Shah','Tomato','2kg')


def view_cookdb():
    df = pd.read_csv('./database/cook_db.csv',index_col=['Cook_id'])
    try:
        df = df.drop('Unnamed: 0',axis=1)
    except:
        return df
    else:
        return df

def __initial_compdb():
    complain_db = pd.DataFrame(columns=['Cook_id','Complain'])
    complain_db.to_csv('./database/complain_db.csv')

def initial_comp():
    comp_obj = comp()
    comp_obj.complain('MS19901',"Chappatis were cold")
    comp_obj.complain('MS19902',"Potato Looks Old")
    comp_obj.complain('MS19902',"Onion Was Not Of Good Quality")

def init():
    if path.exists("./database/st_db.csv"):
        pass
    else:
        st_db = pd.DataFrame(columns=['RollNo','Name','creds'])
        st_db.to_csv('./database/st_db.csv')

def init_db():
    m1 = MessOps()
    df = disp_db()
    if df.empty:
        m1.add_stu('2013412','Piyush',5000)
        m1.add_stu('2013394','Nahar',5000)
        m1.add_stu('2013294','Kanishk',5000)
        m1.add_stu('2013407','Paritosh',5000)
    else:
        pass
def gen_oid(self, curr_oid):
    curr_oid = curr_oid+1
    return curr_oid

def init_order_db():
    order_db = pd.DataFrame(columns=['Order No.','Time','Reg. No.','Order','Amount'])
    order_db.to_csv('orderdb.csv')

def df_to_json(df : pd.DataFrame) :
    return (df.to_json(orient="split"))

def takeorder(orders : list,roll_no):
    total_amount = 0.00
    ord_detail = stud.view_order_db()
    prev_oid = ord_detail.index.values.tolist()
    items = []
    try:
        prev_oid = prev_oid[-1]
    except:
        prev_oid = 0
    df = stud.view_menu_db()    
    for order in orders:
        items.append(df.loc[order]['Item'])
        total_amount = total_amount + stud.order_amt(order)
                
    stud.debit(roll_no,total_amount)
    stud.add_order((prev_oid+1),ctime(),roll_no,items,total_amount)
    return items   


stud = studOps()
mess = MessOps()