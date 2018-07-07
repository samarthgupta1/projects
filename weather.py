# -*- coding: utf-8 -*-
from Tkinter import *
import requests
import datetime
import re
import sys
from io import BytesIO
import urllib  # not urllib.request
from PIL import Image, ImageTk

o=0
def data_output(data):
    m_symbol =u'\u2103'
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

    #print "weather id",data['weather'][0]['id']
    #global o
    #o=data['weather'][0]['id']
    #city_lab = Label(m, text="City:",bg='#8ee5ee')
    #city_lab.grid(row=5, column=0)
    city_data.config(text=json_data['city']['name'])
    city_data.grid(row=5, column=1)
    #city_ab = Label(m, text="Country:",bg='#8ee5ee')
    #city_ab.grid(row=5, column=2)
    country_data.config(text=json_data['city']['country'])
    country_data.grid(row=5, column=3)
    city_ab = Label(m, text="max temp",bg='#8ee5ee',font=("Helvetica",10),fg='#ee7600')
    city_ab.grid(row=6, column=0)
    temp_max.config(text=str(data['main']['temp_max']) + m_symbol)
    temp_max.grid(row=6, column=1)
    city_ab = Label(m, text="mim temp:",bg='#8ee5ee',font=("Helvetica",10),fg='#ee7600')
    city_ab.grid(row=6, column=2)
    temp_min.config(text=str(data['main']['temp_min']) + m_symbol)
    temp_min.grid(row=6, column=3)
    city_ab = Label(m, text="humidity:",bg='#8ee5ee',font=("Helvetica",10),fg='#ee7600')
    city_ab.grid(row=7, column=0)
    humidity.config(text=data['main']['humidity'])
    humidity.grid(row=7, column=1)
    city_ab = Label(m, text="pressure:",bg='#8ee5ee',font=("Helvetica",10),fg='#ee7600')
    city_ab.grid(row=7, column=2)
    pressure.config(text=data['main']['pressure'])
    pressure.grid(row=7, column=3)
    city_ab = Label(m, text="wind speed:",bg='#8ee5ee',font=("Helvetica",10),fg='#ee7600')
    city_ab.grid(row=8, column=0)
    wind.config(text=data['wind']['speed'])
    wind.grid(row=8, column=1)
    city_ab = Label(m, text="clouds:",bg='#8ee5ee',font=("Helvetica",10),fg='#ee7600')
    city_ab.grid(row=8, column=2)
    cloud.config(text=data['clouds']['all'])
    cloud.grid(row=8, column=3)
    city_ab = Label(m, text="weather:",bg='#8ee5ee',font=("Helvetica",10),fg='#ee7600')
    city_ab.grid(row=9, column=2)
    weather.config(text= data['weather'][0]['main'])
    weather.grid(row=9, column=3)
    city_ab = Label(m, text="date:",bg='#8ee5ee',font=("Helvetica",10),fg='#ee7600')
    city_ab.grid(row=9, column=0)
    #a=re.match(r"(\d+)-(\d+)-(\d+)",data['dt_txt'])
    s=re.match(r"(\d+)-(\d+)-(\d+)",data['dt_txt'])
    a=s.group()
    date.config(text=a)
    date.grid(row=9,column=1)




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
    r = requests.get(url='http://api.openweathermap.org/data/2.5/forecast?q='+ t +'&mode=json&units=metric&&appid=354e6f3729c970f2810cf814c749f6ea')
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
    global o
    o=list_items[index]['weather'][0]['id']
    print o
    if(o==800):
        url = "http://openweathermap.org/img/w/01d.png"

        u = urllib.urlopen(url)
        raw_data = u.read()
        u.close()

        im = Image.open(BytesIO(raw_data))
        image = ImageTk.PhotoImage(im)
        label = Label(m,image=image,bg='#8ee5ee')
        label.place(x=370,y=220)
        mainloop()
    elif(o==801):
        url = "http://openweathermap.org/img/w/02d.png"

        u = urllib.urlopen(url)
        raw_data = u.read()
        u.close()

        im = Image.open(BytesIO(raw_data))
        image = ImageTk.PhotoImage(im)
        label = Label(m, image=image, bg='#8ee5ee')
        label.place(x=370, y=220)
        mainloop()
    elif (o==802):
        url = "http://openweathermap.org/img/w/03d.png"

        u = urllib.urlopen(url)
        raw_data = u.read()
        u.close()

        im = Image.open(BytesIO(raw_data))
        image = ImageTk.PhotoImage(im)
        label = Label(m, image=image, bg='#8ee5ee')
        label.place(x=370, y=220)
        mainloop()
    elif (o==803 or 0==804):
        url = "http://openweathermap.org/img/w/04d.png"

        u = urllib.urlopen(url)
        raw_data = u.read()
        u.close()

        im = Image.open(BytesIO(raw_data))
        image = ImageTk.PhotoImage(im)
        label = Label(m, image=image, bg='#8ee5ee')
        label.place(x=370, y=220)
        mainloop()
    elif (o==300 or o==301 or o==302 or o==310 or o==311 or o==312 or o==313 or o==314 or o==321 or o==520 or o==521 or o==522 or o==531):
        url = "http://openweathermap.org/img/w/09d.png"

        u = urllib.urlopen(url)
        raw_data = u.read()
        u.close()

        im = Image.open(BytesIO(raw_data))
        image = ImageTk.PhotoImage(im)
        label = Label(m, image=image, bg='#8ee5ee')
        label.place(x=370, y=220)
        mainloop()
    elif (o==500 or o==501 or o==502 or o==503 or o==504):
        url = "http://openweathermap.org/img/w/10d.png"

        u = urllib.urlopen(url)
        raw_data = u.read()
        u.close()

        im = Image.open(BytesIO(raw_data))
        image = ImageTk.PhotoImage(im)
        label = Label(m, image=image, bg='#8ee5ee')
        label.place(x=370, y=220)
        mainloop()
    elif (o==200 or o==201 or o==202 or o==210 or o==211 or o==212 or o==221 or o==230 or o==231 or o==232):
        url = "http://openweathermap.org/img/w/11d.png"

        u = urllib.urlopen(url)
        raw_data = u.read()
        u.close()

        im = Image.open(BytesIO(raw_data))
        image = ImageTk.PhotoImage(im)
        label = Label(m, image=image, bg='#8ee5ee')
        label.place(x=370, y=220)
        mainloop()
    elif (o==511 or o==600 or o==601 or o==602 or o==611 or o==612 or o==615 or o==616 or o==620 or o==621 or o==622):
        url = "http://openweathermap.org/img/w/13d.png"

        u = urllib.urlopen(url)
        raw_data = u.read()
        u.close()

        im = Image.open(BytesIO(raw_data))
        image = ImageTk.PhotoImage(im)
        label = Label(m, image=image, bg='#8ee5ee')
        label.place(x=370, y=220)
        mainloop()
    elif (o==701 or o==711 or o==721 or o==731 or o==741 or o==751 or o==761 or o==762 or o==771 or o==781):
        url = "http://openweathermap.org/img/w/50d.png"

        u = urllib.urlopen(url)
        raw_data = u.read()
        u.close()

        im = Image.open(BytesIO(raw_data))
        image = ImageTk.PhotoImage(im)
        label = Label(m, image=image, bg='#8ee5ee')
        label.place(x=370, y=220)
        mainloop()
    else:
        print "no image"


def fetch_data():
    entry()
'''
def image():
    if o==501:
        url = "http://openweathermap.org/img/w/10d.png"
        u = urllib.urlopen(url)
        raw_data = u.read()
        u.close()
        im = Image.open(BytesIO(raw_data))
        image = ImageTk.PhotoImage(im)
        label.config(image=image)
        label.grid(row=13,column=0)
'''
w= Tk(className='Weather Forecast')
m=Frame(w,bg='#8ee5ee')
m.pack()
city_label = Label(m, text="Enter a city: ",bg='#8ee5ee',fg='#ee7600')
city_label.grid(row=0, column=0)
city_entry= Entry(m,bg="#008b8b")
city_entry.grid(row=0, column=1)
show = Button(m, text="Show",command=fetch_data,bg='#ee7600',activeforeground="yellow",activebackground="#008b8b")

show.grid(row=1, column=1)
city_data = Label(m,bg='#8ee5ee',font=("Helvetica",40,'bold'),fg='#ee7600')
country_data = Label(m,bg='#8ee5ee',font=("Helvetica",40,'bold'),fg='#ee7600')
temp_max = Label(m,bg='#8ee5ee',font=("Helvetica",20,'bold'),fg='#ee7600')
temp_min = Label(m,bg='#8ee5ee',font=("Helvetica",20,'bold'),fg='#ee7600')
humidity = Label(m,bg='#8ee5ee',font=("Helvetica",10,'bold'),fg='#ee7600')
pressure = Label(m,bg='#8ee5ee',font=("Helvetica",10,'bold'),fg='#ee7600')
wind = Label(m,bg='#8ee5ee',font=("Helvetica",10,'bold'),fg='#ee7600')
cloud = Label(m,bg='#8ee5ee',font=("Helvetica",10,'bold'),fg='#ee7600')
weather = Label(m,bg='#8ee5ee',font=("Helvetica",15,'bold'),fg='#ee7600')
date=Label(m,bg='#8ee5ee',font=("Helvetica",15),fg='#ee7600')

next=Button(m,text=">",width=2,height=2,textvariable=counter1,command=nex,bg='#ee7600',activeforeground="yellow",activebackground="#008b8b")
next.grid(row=12,column=2)
previous=Button(m,text="<",width=2,height=2,textvariable=counter2,command=pre,bg='#ee7600',activeforeground="yellow",activebackground="#008b8b")
previous.grid(row=12,column=1)
r=Label(m,bg='#8ee5ee',font=("Helvetica",15),fg='#ee7600')
r.grid(row=14,column=4)


'''url = "http://openweathermap.org/img/w/10d.png"

u = urllib.urlopen(url)
raw_data = u.read()
u.close()

im = Image.open(BytesIO(raw_data))
image = ImageTk.PhotoImage(im)
label = tkLabel(image=image)
label.pack()
root.mainloop()'''

m.mainloop()

