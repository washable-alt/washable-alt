Day 38

Exercise Tracking with Python and Google Sheets

Nutritionix API - Helps to parse the exercises the user has completed into a json dictionary

`headers`: `x-app-id`, `x-app-key`

`parameters`: `query`, `gender`, `weight_kg`, `height_cm`, `age`

`query`: Input the exercises the user has completed (i.e. ran 1km) [Refer to https://dspace.mit.edu/handle/1721.1/100640 for more information]

Sheety API - Helps to serve user's spreadsheet as an API
Sheet names act as API endpoints

`URL Structure`

https://api.sheety.co/username/projectName/sheetName


First step for SHEETY API is to prepare spreadsheet: 
1. Make the first row of the spreadsheet as the header
2. Tabs within the spreadsheet will be used as the API endpoint name
3. For example, sheet1, sheet2, etc
4. Include the `GOOGLE_SHEET_NAME`, so that the json dictionary can be crafted

Second step is to do a post request, which requires an `url`, `json` and `headers`

`Authentication Methods`
1. No Auth -Anyone can edit the google sheet if someone does a post request 
2. Basic Auth - value set to the username and password encoded as base64
   headers = f"Authorisation: Basic {basic_auth}"
3. Bearer Auth - Uses a token or secret of my choosing
   headers = f"Authorisation: Bearer {token}"