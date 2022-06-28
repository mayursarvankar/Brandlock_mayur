import requests
from linkedin import linkedin
#pip install --upgrade https://github.com/ozgur/python-linkedin/tarball/master


#https://www.linkedin.com/oauth/v2/authorization?response_type=code&client_id=*&scope=*&state=*&redirect_uri=*
CLINETiD="770438fkjov8by"
CLIENTSECRED="EBeQf9AsJ7U31k6e"
url="https%3A%2F%2Fapi-brandlock.io"
#https://www.linkedin.com/oauth/v2/authorization?response_type=code&client_id=8642sxa4tfrvt3&scope=r_liteprofile&state=987654321&redirect_uri=https%3A%2F%2Fapi-brandlock.io
#https://www.linkedin.com/oauth/v2/authorization?response_type=code&client_id=770438fkjov8by&scope=r_liteprofile&state=987654321&redirect_uri=https%3A%2F%2Fapi-brandlock.io
acees_toke="AQUGMkn7n7Av08IvP_tTnbmXukUhzlD1mXoq4lhxdPCYNs_6sfK3TEnX874vtrCL2izjoR2QBbLcvRwKqo_glAqlvwil3r-qcMS6eUHvMbNshlq-1A77aAh0UPKgbDwa8QZQQUWeN41XbDsoqU6sb3UxiNxeBnhdPhQpqRIZKW4WGkJVVAj8J1w78g_6gXuvcY05REPN0e9w1dG06C9w5X67Yvu7pbN1pdfeTMRxmOXz66CqXL_JPTKwCu785FUH3iLsw0ArO4dXaLDvHNaisoQRWAG7b0M6O8c0_6a2TZWJhc0CPfr3m-_gWbUcXEprN4wJYau4fLM3fdUxkdbgQluoaG1x3A"

r="https://www.linkedin.com/developers/tools/oauth/redirect"
id="19a30018b"
# id="me"
r2=f'https://api.linkedin.com/v2/{id} -H "Authorization: Bearer {acees_toke}"'
# base_url="https://api.linkedin.com/v2/me"
base_url=f"https://api.linkedin.com/v2/people/(id:{id})"
req=requests.get(base_url,headers={"Authorization":f"Bearer {acees_toke}"}).json()

print(req)

