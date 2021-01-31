import requests
import random
import hashlib
from timeit import default_timer

class regionCountry:

    def __init__(self):
        
        self.headers = {
            'x-rapidapi-key': "80d4ed17c2msh66ebb8cd037c572p11e422jsna3e2d005ae38",
            'x-rapidapi-host': "restcountries-v1.p.rapidapi.com"
            }

    def petition(self, url):
        response = requests.request("GET", url, headers=self.headers)
        return response.json()

    def regions(self):
        
        self.timeStart = default_timer()
        #res = self.petition("https://restcountries-v1.p.rapidapi.com/all")
        res = self.petition("https://restcountries.eu/rest/v2/all?fields=region")    

        regions = []
        
        for i in res:
            if (i['region'] not in regions) and (i['region'] not in '') :
                regions.append(i['region'])

        self.timeFinal = default_timer()
        self.generalTime = self.timeFinal-self.timeStart
        return regions        

    def hash(self,msj):
        return hashlib.sha1(msj.encode('utf-8')).hexdigest()

    def countrys(self,regions):
        countrys = []
        
        for i in regions:
            self.timeStart = default_timer() 
            res = self.petition("https://restcountries.eu/rest/v2/region/"+str(i)+"?fields=name;languages")
            city = random.randint(0,(len(res)-1))
            self.timeFinal = default_timer()
            timeIndependent = self.timeFinal-self.timeStart
            time = self.generalTime+timeIndependent
            limit_time = float("%.5f" %time)
            country = {'region': i, 'country': res[city]['name'], 'language': self.hash(str(res[city]['languages'][0]['name'])), 'time':limit_time}
            countrys.append(country)
        return countrys
        