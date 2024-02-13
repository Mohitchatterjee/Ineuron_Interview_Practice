from urllib.request import urlopen 
import json
import pandas as pd 

class Pokemon:
    def read_URL(self, URL):
        # store the response of URL 
        response = urlopen(url) 
  
        # storing the JSON response from url in data 
        self.data_json = json.loads(response.read()) 
        self.storeJsonToExcel()
    
    def storeJsonToExcel(self):  
        # Normalize json with key pokemon
        df = pd.json_normalize(self.data_json['pokemon'])
        
        fileName = 'Pokemon.xlsx'

        # Save df into excel format
        df.to_excel(fileName)

if __name__ == '__main__':
    url = "https://raw.githubusercontent.com/Biuni/PokemonGO-Pokedex/master/pokedex.json"
    cls_obj = Pokemon()
    cls_obj.read_URL(url)
  

