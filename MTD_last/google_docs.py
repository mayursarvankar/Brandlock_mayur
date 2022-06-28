import gspread
import pandas as pd
import os

def GoogleSheetData(Sheeturl,sheetName):
    main_path="C:/Users/Admin/PycharmProjects/Brandlock/MTD_last"

    gc=gspread.service_account(filename=main_path +"/"+"inputData/creds.json")

    sh = gc.open_by_url(Sheeturl)
    ws=sh.worksheet(sheetName)
    df = pd.DataFrame(ws.get_all_records())
    df.columns= [ "Web_id","Company_Website"]
    # df["Company_Website"] = "https://www."+ df["Company_Website"]

    # print(df.head())

    return df

# xy=GoogleSheetData("https://docs.google.com/spreadsheets/d/1mgnooTFb5WSAF_IrMxYp5unqqdfna3Oe5Ouu0bflhkA/edit#gid=1669480742","for mayur")
# print(xy)