from urllib.request import urlopen 
import json
import pandas as pd 

class Nasa:
    def read_URL(self, URL):
        # store the response of URL 
        response = urlopen(url) 
  
        # storing the JSON response from url in data 
        self.data_json = json.loads(response.read()) 
        print(self.data_json)
        self.storeJsonToExcel()
    
    def storeJsonToExcel(self):  
        # Normalize json with key pokemon
        df = pd.json_normalize(self.data_json)
        
        fileName = './Nasa.csv'

        # Save df into excel format
        df.to_csv(fileName, sep='-')

if __name__ == '__main__':
    url = "https://data.nasa.gov/resource/y77d-th95.json"
    cls_obj = Nasa()
    cls_obj.read_URL(url)
  

