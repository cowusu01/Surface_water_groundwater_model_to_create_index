#function to connect to Url and download data
import json
import requests
import pandas as pd


columnsTitles = ["dig_ticket_",
                 "permit_",
                 "requestdate",
                 "emergency",
                 "stnofrom",
                 "stnoto",
                 "direction",
                 "stname",
                 "suffix",
                 "placement",
                 "digdate",
                 "expirationdate",
                 "primarycontactlast",
                 "latitude",
                 "longitude"]


def getRequestData(): 
    """Method to get dig tickets from Chicago data portal api. Response is is converted to csv.
    args:None.
    Return: None
    """
    outputFileName = "digticketreport.csv"  # Ouput csv file name.
    # Url to api.
    digticketurl = "https://data.cityofchicago.org/resource/gptz-y9ub.json?$limit=620000&$offset=0"
    digticketresponse = requests.request(
        "GET", digticketurl,  verify=False) ## no need to verify ssl certificate##
    if digticketresponse.status_code == 200: ### if response is successful
        parsedResponse = json.loads(digticketresponse.text)
        #print(parsedResponse)
        df = pd.DataFrame(parsedResponse)
        digticketReport = df.reindex(columns=columnsTitles) ### rearrange the columns
        digticketReport.to_csv(outputFileName, sep=',', index=False)


if __name__ == '__main__':
    getRequestData()
