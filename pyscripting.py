import requests
import json

url = 'https://api.data.gov/ed/collegescorecard/v1/schools.json'
payload = {
        'api_key': "api_key_string",
        '_fields': ','.join([
            'school.name',
            'school.school_url',
            'school.city',
            'school.state',
            'school.zip',
            '2015.student.size',
        ]),
        'school.operating': '1',
        '2015.academics.program_available.assoc_or_bachelors': 'true',
        '2015.student.size__range': '1..',
        'school.degrees_awarded.predominant__range': '1..3',
        'school.degrees_awarded.highest__range': '2..4',
        'id': '240444',
    }
def main():
    data = requests.get(url, params=payload).json()
   
        
    print(data)
    
    

     
main()
