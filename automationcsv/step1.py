import pandas as pd
import numpy as np
import json


def flag_df(df_obj):
    if (df_obj['inhandQty'] <= 10 and df_obj['inhandQty'] > 2):
        return 10
    if (df_obj['inhandQty'] <= 1 and df_obj['inhandQty'] >= 2):
        return 20
    else:
        return 0



def firstStep():


    df=pd.read_csv("B2B_sales.csv")
    sitDf=pd.read_csv("siteMap.csv")




    # ['Period', 'Site', 'Vendor', 'Distro', 'Item', 'Item name', 'Item size',
    #        'Category', 'Unnamed: 8', 'Sub category', 'Sold qty', 'Amount']


    # ========================================================================
    # print(df['Item name'].drop_duplicates)
    # "104688 - Caramel Tobacco (Rich Tobacco With Vanilla Caramel Notes)"
    # "104689 - Strawberry Lime (Sweet Strawberries and Spicy Lime)"
    # "104690 -  Banana ICE (Ripe Banana And Refreshing Icy Mint)"
    # "104691 - Cinnamon Fireball (Sweet Yet Rich Fiery Flavor)"
    # "104692 - Berry Menthol (Fruity Irresistible Berry Blends)"
    # print(df["Item name"])
    df["ItemFinal"]=df["Item"].astype(str) +" - "+ df["Item name"]
    uniqueItem=[]
    for uqItem in df["ItemFinal"].unique():
        uqItemName=str(uqItem).split(" - ")[-1]
        uqItemNo=str(uqItem).split(" - ")[0]
        if uqItemName =="Rich Tobacco With Vanilla Caramel Notes":
            FinaluqName=uqItemNo + " - " + "Caramel Tobacco (" +  uqItemName + ")"
            uniqueItem.append(FinaluqName)
        if uqItemName =="Sweet Strawberries and Spicy Lime":
            FinaluqName=uqItemNo + " - " + "Strawberry Lime (" +  uqItemName + ")"
            uniqueItem.append(FinaluqName)
        if uqItemName =="Ripe Banana And Refreshing Icy Mint":
            FinaluqName=uqItemNo + " - " + "Banana ICE (" +  uqItemName + ")"
            uniqueItem.append(FinaluqName)
        if uqItemName =="Sweet Yet Rich Fiery Flavor":
            FinaluqName=uqItemNo + " - " + "Cinnamon Fireball (" +  uqItemName + ")"
            uniqueItem.append(FinaluqName)
        if uqItemName =="Fruity Irresistible Berry Blends":
            FinaluqName=uqItemNo + " - " + "Berry Menthol (" +  uqItemName + ")"
            uniqueItem.append(FinaluqName)

    # ==================================================================================================================
    lenofuqItem=len(uniqueItem)
    lenofuqSite=len(df['Site'].unique())

    allsite = list(df['Site'].unique()) * lenofuqItem
    allsite.sort()

    allItem = list(uniqueItem) * lenofuqSite
    # allsite.sort()


    site_itemDf=pd.DataFrame({"SiteName":allsite,"ItemName":allItem,"TotalQty":20})

    inQtyList=[]
    siteIDList=[]
    for index, row in site_itemDf.iterrows():

        itemID =int(str(row["ItemName"]).split(" - ")[0])

        filtered_values = np.where((df['Site']==row['SiteName']) & (df['Item'] == itemID))
        try:
            Qty=df["Sold qty"].loc[filtered_values].values[0]
        except:
            Qty=0

        aeNo=str(row['SiteName']).replace("CS","")


        filtered_values2 = np.where(sitDf['AESC number'] == aeNo)
        try:
            SiteID = str(sitDf["Site"].loc[filtered_values2].values[0])
        except:
            SiteID = None


        inQtyList.append(Qty)
        siteIDList.append(SiteID)

        # print(row['SiteName'],row['ItemName'],row['TotalQty'],Qty)

    site_itemDf['intialQty']=inQtyList
    site_itemDf["inhandQty"]= site_itemDf['TotalQty'] - site_itemDf['intialQty']
    site_itemDf['InvoiceQty'] = site_itemDf.apply(flag_df, axis = 1)
    site_itemDf['LastInventory'] = site_itemDf['intialQty'] +  site_itemDf['InvoiceQty']

    site_itemDf['SiteID'] = siteIDList
    site_itemDf.to_csv("Inventory.csv",index=False)

    # +======================================================================
    filtered_values3 = np.where((site_itemDf['InvoiceQty']==10) | (site_itemDf['InvoiceQty'] == 20))
    try:
        validSiteIDs = site_itemDf["SiteID"].loc[filtered_values3].values
    except:
        validSiteIDs = None

    # validSiteID="".join(validSiteID)
    # ['SiteName', 'ItemName', 'TotalQty', 'intialQty', 'inhandQty',
    #        'InvoiceQty', 'SiteID']

    finalData = []
    for validId in validSiteIDs:
        cond_dfItemName=list(site_itemDf[site_itemDf['SiteID']==validId]["ItemName"].values)
        cond_dfInvoiceQty=list(site_itemDf[site_itemDf['SiteID']==validId]["InvoiceQty"].values)
        # appended_data.append(cond_df)


        validData = {
                validId: {"itemNames": cond_dfItemName,"InvoiceQty":cond_dfInvoiceQty}
                }
        finalData.append(validData)


    return finalData


# xy = firstStep()
# print(xy)
# ==============================================================
