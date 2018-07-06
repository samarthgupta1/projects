from Tkinter import *
import requests
import datetime
import re
import sys

def data_output(data):
    m_symbol = '\xb0' + 'C'
    '''print('---------------------------------------')
    print"city",json_data.get('city').get('name')
    print('---------------------------------------')
    print"country",json_data.get('city').get('country')
    print('---------------------------------------')
    print"temp",data.get('main').get('temp')
    print('---------------------------------------')
    print"temp max",data.get('main').get('temp_max')
    print('---------------------------------------')
    print"temp min",data.get('main').get('temp_min')
    print('---------------------------------------')
    print"humidity",data.get('main').get('humidity')
    print('---------------------------------------')
    print"pressure",data.get('main').get('pressure')
    print('---------------------------------------')
    print"sky",data['weather'][0]['main']
    print('---------------------------------------')
    print"wind",data.get('wind').get('speed')
    print('---------------------------------------')
    print"wind speed ",data.get('deg')
    print('---------------------------------------')
    print"cloudiness",data.get('clouds').get('all')
    print('---------------------------------------')
    print"date",data['dt_txt']
    print('---------------------------------------')'''

    city_lab = Label(m, text="City:")
    city_lab.grid(row=5, column=0)
    city_data.config(text=json_data['city']['name'])
    city_data.grid(row=5, column=1)
    city_ab = Label(m, text="Country:")
    city_ab.grid(row=5, column=2)
    country_data.config(text=json_data['city']['country'])
    country_data.grid(row=5, column=3)
    city_ab = Label(m, text="max temp")
    city_ab.grid(row=6, column=0)
    temp_max.config(text=str(data['main']['temp_max']) + m_symbol)
    temp_max.grid(row=6, column=1)
    city_ab = Label(m, text="mim temp:")
    city_ab.grid(row=6, column=2)
    temp_min.config(text=str(data['main']['temp_min']) + m_symbol)
    temp_min.grid(row=6, column=3)
    city_ab = Label(m, text="humidity:")
    city_ab.grid(row=7, column=0)
    humidity.config(text=data['main']['humidity'])
    humidity.grid(row=7, column=1)
    city_ab = Label(m, text="pressure:")
    city_ab.grid(row=7, column=2)
    pressure.config(text=data['main']['pressure'])
    pressure.grid(row=7, column=3)
    city_ab = Label(m, text="wind speed:")
    city_ab.grid(row=8, column=0)
    wind.config(text=data['wind']['speed'])
    wind.grid(row=8, column=1)
    city_ab = Label(m, text="clouds:")
    city_ab.grid(row=8, column=2)
    cloud.config(text=data['clouds']['all'])
    cloud.grid(row=8, column=3)
    city_ab = Label(m, text="weather:")
    city_ab.grid(row=9, column=0)
    weather.config(text= data['weather'][0]['main'])
    weather.grid(row=9, column=1)
    city_ab = Label(m, text="date:")
    city_ab.grid(row=9, column=2)
    date.config(text=data['dt_txt'])
    date.grid(row=9,column=3)


#global counter
counter1=0
counter2=0

def nex():
    global counter1
    counter1 += 1
    entry()


def pre():
    global counter2
    counter2 -= 1
    entry()

def entry():

    #print "next",counter1
    #global counter2
    #counter2 -= 1
    #print "previous",counter2

    now = datetime.datetime.now()
    #print(now)
    today= now.day
    r=today +counter1+counter2
    #print r
    y='0'+str(r)
    #print y
    t=city_entry.get()
    #t= raw_input("enter the city")
    r = requests.get(url='http://api.openweathermap.org/data/2.5/forecast?q='+ t +'&appid=354e6f3729c970f2810cf814c749f6ea')
    global json_data
    json_data = r.json()
    #print(json_data)
    list_items =json_data['list']
    #return list_items
    #print list_items
    #print json_data.get('name')
    #data_output(json_data)
    #print r
    list_indices = []
    for items in list_items:
        matchObj = re.match(r"(\d+)-(\d+)-(\d+)",items['dt_txt'], re.M | re.I)
        #print(matchObj.group(3))
        list_indices.append(matchObj.group(3))
    #print(list_indices)
    #print(list_indices[0])
    #list.index(item)
    #print(today)
    #print r,y
    for items in list_indices:
        #print items
        if items == r or items == y:
            #print("yay")
            #print(items)
            #print r
            index=list_indices.index(items)
            #print(index)
            break
    #print(index)
    #print "X",(list_items[index])
    data_output(list_items[index])
def fetch_data():
    entry()

m = Tk(className='Weather Forecast')

city_label = Label(m, text="Enter a city: ")
city_label.grid(row=0, column=0)
city_entry= Entry(m)
city_entry.grid(row=0, column=1)
show = Button(m, text="Show",command=fetch_data)

show.grid(row=1, column=1)
city_data = Label(m)
country_data = Label(m)
temp_max = Label(m)
temp_min = Label(m)
humidity = Label(m)
pressure = Label(m)
wind = Label(m)
cloud = Label(m)
weather = Label(m)
date=Label(m)

next=Button(m,text=">",width=2,height=2,textvariable=counter1,command=nex)
next.grid(row=10,column=2)
previous=Button(m,text="<",width=2,height=2,textvariable=counter2,command=pre)
previous.grid(row=10,column=1)
m.mainloop()

