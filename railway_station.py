import pickle,os
print "-------------------------------------------------------WELCOME USER--------------------------------------------------------\n",
print ""
print "This is an Railway Reservtion Computer Program where you as a customer can view the trains available and can even book or cancel train and as an Authorised person can alter the database and much more..."
print "___"*88
print ""
print " choose any of the following options:-"
def takeUserInput():
    global choice
    try:
        choice=int(raw_input("enter your choice"))
    except ValueError:
        print "invalid input\n"
def takeSUserInput():
    global Schoice
    try:
        Schoice=int(raw_input("enter your schoice"))
    except ValueError:
        print "invalid input\n"
def ACDetails():
    print "details"

class Train:
    def __init__(self):
        self.From=raw_input("enter the boarding location:")
        self.to=raw_input("enter the destination location:")
        self.railways=raw_input("enter the train name :")
        self.id=raw_input("enter the train number:")
        self.sstation=raw_input("enter starting station")
        self.dstation=raw_input("enter destination station")
        self.dtime=raw_input("enter the departure time::")
        self.atime=raw_input("enter the arrival time:")
        self.seats=input("enter the number seats:")
        self.seatDict={}
        self.c_id=0
    def book_seat(self):
        self.seats-=1
        self.c_id+=1
while True:
    print "\n\n----***MAIN MENU***---"
    print 'Enter "1"to display train data'
    print 'Enter "2"to change database(authorised person only)'
    print 'Enter "3"to book train'
    print 'Enter "4"to cancel train'
    print 'Enter "5"to quit program'
    takeUserInput()
    if choice==1:
        fr=open('traindetails.dat','rb')
        try:
            while 1:
                a1=pickle.load(fr)
                print
                print"--x--"*25
                print "TRAIN NAME:",a1.railways
                print "DESTINATION LOCATION:",a1.to
                print "BOARDING LOCATION:",a1.From
                print "TRAIN ID:",a1.id
                print "STARTING SATATION:",a1.sstation
                print "DESTINATION STATION :",a1.dstation
                print "DEPARTURE TIME:",a1.dtime
                print  "ARRIVAL TIME:",a1.atime
                print "NO OF SEATS AVAILABLE:",a1.seats
                print "--x--"*25
        except EOFError:
            fr.close()
    elif choice==2:
        password=raw_input("enter the password:")
        fr=open('pass.txt','r')
        s=fr.read()
        if password==s:
            print "\n__________________Access granted__________________"
            while 1:
                print "\nAs an authorised person you can choose any of the following options"
                print '\n\nEnter "1" to change password'
                print 'Enter "2" to add new train'
                print 'Enter "3" to delete old train'
                print 'Enter "4" to get passanger details'
                print 'Enter "5" to Quit'
                takeSUserInput()
                if Schoice==1:
                    oldpass=raw_input("enter old password:")
                    newpass=raw_input("enter new password:")
                    if oldpass==newpass:
                        print "password not changed"
                    else:
                        s=raw_input('enter newpassword again:')
                        if s==newpass:
                            fr=open('pass.txt','w')
                            fr.write(s)
                            fr.close()
                            print '\n____password changed____'
                        else:
                            print '\n***wrong password***'
            
                elif Schoice==2:
                    fw=open('traindetails.dat','ab+')
                    a=Train()
                    found=1
                    try:
                        while 1:
                            ac=pickle.load(fw)
                            if ac.railways==a.railways and ac.id==a.id:
                                found=0
                    except EOFError:
                        fw.close()
                        fw=open('traindetails.dat','ab+')
                        if found==1:
                            pickle.dump(a,fw)
                            print "\n**Train added**"
                        elif found==0:
                            print "\n train already exist"
                        fw.close()
                elif Schoice==3:
                    arlns=raw_input("enter the name of train to be deleted :")
                    del_id=raw_input("enter the id of train to be deleted:")
                    fw=open('temp.dat','wb')
                    fr=open('traindetails.dat','rb')
                    f=0
                    try:
                        while 1:
                            train=pickle.load(fr)
                            if train.railways==arlns and train.id==del_id:
                                f=1
                            else:
                                pickle.dump(train,fw)
                    except EOFError:
                        fr.close()
                        fw.close()
                    if f==0:
                        print "\n train does not exist"
                    if f==1:
                        print "\n train deleted"
                    import os
                    os.remove('traindetails.dat')
                    os.rename('temp.dat','traindetails.dat')
                elif Schoice==4:
                    railwaysN=raw_input("enter train name:")
                    trainN=raw_input("enter the train id:")
                    fr=open("traindetails.dat",'rb')
                    found=0
                    try:
                        while True:
                            ac2=pickle.load(fr)
                            if ac2.railways==railwaysN and ac2.id==trainN:
                                found=1
                                print "\nList of passangers:"
                                for i in ac2.seatDict.values():
                                    print "=*="*36
                                    print 'NAME:',i[0]     
                                    print 'AGE:',i[1]
                                    print 'DAY:',i[3]
                                    print 'DATE:',i[2]
                                    print 'TICKET PRICE:',i[4]
                                    print  "=*="*36
                    except EOFError:
                        fr.close()
                    if found==0:
                        print "enter correct data"      
                elif Schoice==5:
                    print "program ends"
                    break
                else:
                    print "\n invalid input\n"
                    
    elif choice==3:
        book_From=raw_input("enter your boarding location:")
        book_to=raw_input("enter your destination:")
        fr=open('traindetails.dat','rb')
        flfound=0
        try:
            while 1:
                ac=pickle.load(fr)
                if ac.From==book_From and ac.to==book_to:
                    print "=="*88
                    print"TRAIN NAME:",ac.railways
                    print"BOARDING LOCATION",ac.From
                    print"DESTINATION LOCATION",ac.to
                    print "TRAIN ID",ac.id
                    print "STARTING SATATION:",ac.sstation
                    print "DESTINATION STATION :",ac.dstation
                    print "DEPARTURE TIME:",ac.dtime
                    print  "ARRIVAL TIME:",ac.atime
                    print "NO OF SEATS AVAILABLE:",ac.seats
                    print "=="*88
                    flfound=1
        except EOFError:
            fr.close()
        if flfound==1:
            try:
                book_railways=raw_input("enter your train name from which you want to travel:")
                book_acid=raw_input("enter your train id from which you are traveling:")
                name=raw_input("enter your full name:")
                age=input("enter your age:")
                day= raw_input("enter the day you want to tarvel")
                date= raw_input("enter the date you want to tarvel")
                if age<18:
                    category='C'
                    z=raw_input("enter type of boagi sleeper ,ac, 2c::")
                    if z=='sleeper'or z=='Sleeper':
                        price=496
                    elif z=='ac' or z=='AC':
                        price =690
                    if z=='2c'or z=="2C":
                        price= 1004
                elif 18<=age<60:
                    category='A'
                    z=raw_input("enter type of boagi sleeper ,ac, 2c::")
                    if z=='sleeper'or z=='Sleeper':
                        price=395
                    elif z=='ac' or z=='AC':
                        price =540
                    if z=='2c'or z=="2C":
                        price =990
                elif age>=60:
                    category='SC'
                    z=raw_input("enter type of boagi sleeper ,ac, 2c::")
                    if z=='sleeper'or z=='Sleeper':
                        price=295
                    elif z=='ac' or z=='AC':
                        price =400
                    if z=='2c'or z=="2C":
                        price =800
            except SyntaxError:
                print "\n invalid information"
            fr=open('traindetails.dat','rb')
            fw=open('temp.dat','ab')
            f=0
            try:
                while True:
                    ac=pickle.load(fr)
                    if ac.railways==book_railways and ac.id==book_acid and ac.seats>0:
                        ac.book_seat()
                        cust_id= "T"+str(ac.id)+ category  +"P"+str(ac.c_id)
                        ac.seatDict.update({cust_id:[name,age,date,day,price]})
                        f+=1
                        pickle.dump(ac,fw)
                    elif ac.seats==0:
                        print "no seats available"
                    else:
                        pickle.dump(ac,fw)
            except EOFError:
                fr.close()
                fw.close()
            import os
            os.remove('traindetails.dat')
            os.rename('temp.dat','traindetails.dat')
            if f==0:
                print "train not available"
            try:
                print "^*^"*36
                print"your booking id id",cust_id
                print "^*^"*36
                print"your ticket price is ",price
            except:
                pass
    elif choice==4:
         train_to_del=raw_input("enter your book train name:")
         trainid_to_del=raw_input('enter your train id:')
         id_to_del=raw_input("enter your booking id:")
         fr1=open('traindetails.dat','rb')
         fw1=open('temp.dat','wb')
         bnf=0
         try:
             while 1:
                 ac1=pickle.load(fr1)
                 if ac1.railways==train_to_del and ac1.id==trainid_to_del:
                     try:
                         ac1.seatDict.pop(id_to_del)
                         print "\n booking cancelled"
                         bnf=1
                     except:
                         print "\n booking id not found"
                     pickle.dump(ac1,fw1)
         except EOFError:
             fr1.close()
             fw1.close()
         if bnf==0:
             print "give correct information"
         import os
         os.remove('traindetails.dat')
         os.rename('temp.dat','traindetails.dat')
    elif choice==5:
        import sys
        print "program ends"
        sys.exit()
    else:
        print "invalid choice"
                            

s1=Train()
s1.book_seat()
