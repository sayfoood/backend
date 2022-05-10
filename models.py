import pandas as pd


#class binding functions related to cook, viz. issueing materials,issueing graduate,complain etc.
class cooking:

    def add_cook(self, Cook_id,Name,Item,Quantity):#adding cook data to database
        cook_db = self.view_cookdb()
        cook_db = cook_db.reset_index()
        cook_db = cook_db.append(pd.DataFrame([[Cook_id,Name,Item,Quantity]],columns=cook_db.columns))
        cook_db.to_csv('cook_db.csv')
        cook_db = cook_db.set_index('Cook_id')
        return cook_db

    def view_cookdb(self):#display data stored in csv
        df = pd.read_csv('./database/cook_db.csv',index_col=['Cook_id'])
        try:
            df = df.drop('Unnamed: 0',axis=1)
        except:
            return df
        else:
            return df

    def view_cooks_item(self):#history df material issues to cook 
        cook_db1 = pd.read_csv('./database/cook_db.csv',index_col=['Cook_id'])
        return cook_db1


#funtions related to material ordered for mess 
class sp:
    def __init_supplydb(self):
        sp_db = pd.DataFrame(columns=['Item_id','Name','delivered','Quantity'])
        sp_db.to_csv('./database/sp_db.csv')

    def view_spdb(self):
        df = pd.read_csv('./database/sp_db.csv',index_col=['Item_id'])
        try:
            df = df.drop('Unnamed: 0',axis=1)
        except:
            return df
        else:
            return df

    def view_indb(self):#displaying data stored in in_db.csv
        df = pd.read_csv('./database/inventorydb.csv',index_col=['Item_id'])
        try:
            df = df.drop('Unnamed: 0',axis=1)
        except:
            return df
        else:
            return df

    def __init_inventory(self):#for the first order recieved ever , this funtion creates the inventorydb.csv
        in_db = pd.DataFrame(columns=['Item_id','Name','Quantity'])
        in_db.to_csv('./database/inventorydb.csv')

    def delFromInventory(self,Item_id, quantity_ass):#once the material is issued to the cook and nothing is left then the data is deleted from the inventory database
        indb = self.view_indb()
        saved = indb.loc[Item_id]['Quantity']
        indb.loc[Item_id ,'Quantity'] =saved - quantity_ass

    def addToInventory(self, Item_id,name,quantity):
        in_db = self.view_indb()
        if  in_db.empty:
            print("[INFO] Not Found Adding One")
            in_db = in_db.reset_index()
            in_db = in_db.append(pd.DataFrame([[Item_id,name,quantity]],columns=in_db.columns))
        elif(Item_id not in in_db.index.values):
            in_db = in_db.reset_index()
            in_db = in_db.append(pd.DataFrame([[Item_id,name,quantity]],columns=in_db.columns))
        else:
            print("[INFO] Found Existing One")
            crr_qty = in_db.loc[Item_id]['Quantity']
            in_db.loc[Item_id,'Quantity'] = quantity + crr_qty
        in_db.to_csv('./database/inventorydb.csv')
        return in_db

    def add_items(self, item_id,name,quantity,status):#ordering items from market by the mess incharge and adding the material to supply database i.e. "sp_db.csv"
        sp_db = self.view_spdb()
        sp_db = sp_db.reset_index()
        sp_db = sp_db.append(pd.DataFrame([[item_id,name,status,quantity]],columns=sp_db.columns))
        sp_db.to_csv('./database/sp_db.csv')
        return sp_db

    def change_status(self, item_id, status):#once the order of raw material from the market is recieved , the status can be changed from not 
                                            #delivered "ND" to "delivered" and the order data is deleted from sp_db.csv and added to 
                                            #inventory "inventorydb.csv"
        df = self.view_spdb()
        print("NAME : ",df.loc[item_id]['Name'] )
        data = df.loc[item_id]['Quantity']
        name = df.loc[item_id]['Name']
        print(data)
        if status == "yes":
            self.addToInventory(item_id,name,data)
            df = df.drop(item_id)
            df.to_csv('./database/sp_db.csv')
        else:
            print("[INFO] Nothing Changed ")



#class binding functions related to regiteration of complains from both incharge and students 
class comp(cooking):

    def complain(self, Cook_id,complaint):
        complain_db = self.view_complaindb()
        complain_db = complain_db.reset_index()
        complain_db = complain_db.append(pd.DataFrame([[Cook_id,complaint]],columns=complain_db.columns))
        complain_db.to_csv('./database/complain_db.csv')
        complain_db = complain_db.set_index('Cook_id')

    def view_complain(self):
        complain_db1 = pd.read_csv('./database/complain_db.csv',index_col=['Cook_id'])
        return complain_db1

    def view_complaindb(self):
        df = pd.read_csv('./database/complain_db.csv',index_col=['Cook_id'])
        try:
            df = df.drop('Unnamed: 0',axis=1)
        except:
            return df
        else:
            return df



