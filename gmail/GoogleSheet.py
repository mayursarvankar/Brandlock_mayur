import gspread
import pandas as pd

gc=gspread.service_account(filename="creds.json")

sh = gc.open_by_url('https://docs.google.com/spreadsheets/d/1mgnooTFb5WSAF_IrMxYp5unqqdfna3Oe5Ouu0bflhkA/edit#gid=1669480742')
ws=sh.worksheet('for mayur')
df = pd.DataFrame(ws.get_all_records())
df["web_url"] = "https://www."+ df["web_url"]
print(df.head())