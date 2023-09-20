import pandas as pand
import requests

# Define the URL of the API
urlOfbinanceApidata = 'https://data.binance.com/api/v3/ticker/24hr'
try:
    responseofURL = requests.get(urlOfbinanceApidata,timeout=3)
    responseofURL.raise_for_status()
  #to convert it into JSON Format after succesfull checks
    data=responseofURL.json()
  #convert into dataFrame
    dataFrame = pand.DataFrame(data)
  #now to save the data frame into CSV(comma seperated values) we use
    dataFrame.to_csv('binance_csv_api_data.csv', index=False)
except requests.exceptions.HTTPError as errh:
    print ("Http Error:",errh)
except requests.exceptions.ConnectionError as errc:
    print ("Error Connecting:",errc)
except requests.exceptions.Timeout as errt:
    print ("Timeout Error:",errt)
except requests.exceptions.RequestException as err:
    print ("OOps: Something Else",err)
finally:
  print("Converted succesfully , Task 1 Completed")
