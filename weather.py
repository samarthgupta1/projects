
import requests
w=raw_input("enter the city")
r = requests.get(url='http://api.openweathermap.org/data/2.5/weather?q='+w+'&appid=354e6f3729c970f2810cf814c749f6ea')
json_data= r.json()
print(json_data)
print json_data.get('name')


def data_output(data):
    m_symbol = '\xb0' + 'C'
    print('---------------------------------------')
    print"city",json_data.get('name')
    print('---------------------------------------')
    print"country",json_data.get('sys').get('country')
    print('---------------------------------------')
    print"temp",json_data.get('main').get('temp')
    print('---------------------------------------')
    print"temp max",json_data.get('main').get('temp_max')
    print('---------------------------------------')
    print"temp min",json_data.get('main').get('temp_min')
    print('---------------------------------------')
    print"humidity",json_data.get('main').get('humidity')
    print('---------------------------------------')
    print"pressure",json_data.get('main').get('pressure')
    print('---------------------------------------')
    print"sky",json_data['weather'][0]['main']
    print('---------------------------------------')
    print"wind",json_data.get('wind').get('speed')
    print('---------------------------------------')
    print"wind speed ",json_data.get('deg')
    print('---------------------------------------')
    print"cloudiness",json_data.get('clouds').get('all')
    print('---------------------------------------')

data_output(json_data)