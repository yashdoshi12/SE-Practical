from datetime import date
import Medium as M
import mysql.connector
import os

#It is version2
#Because I've created database on cloud.

today = date.today() # To get Today's Date. 
db=mysql.connector.connect(host="sql6.freesqldatabase.com",user="sql6582218",passwd="KNAZUQReNL",database="sql6582218")
cursor=db.cursor()
print('........................................Birthday Service and Festival..............................')

def showData():
    cursor.execute('SELECT * FROM Data')
    data = cursor.fetchall()
    for d in data:
        print(d)
    #cursor.execute('SELECT * FROM Festivals')
    #data = cursor.fetchall()
    #for d in data: 
        # print(d)

def getData():
    global Email_ID
    global Month
    global Name
    global Number
    global Holiday
    global Date

    Holiday,Date = [],[]
    Email_ID,Month,Name,Number = [],[],[],[]
    #for getting Birthday's table data/info
    cursor.execute('SELECT * FROM Data')
    data = cursor.fetchall()
    for d in data:
        Email_ID += [d[1]]
        Month+=[(str(d[3])).split('-')]
        Name += [d[0]]
        Number += [d[2]]
        #print(d)
    
    #For getting Festival's table data
    cursor.execute('SELECT * FROM Festivals')
    data = cursor.fetchall()
    for d in data:
        Holiday += [d[0]]
        Date += [(str(d[1])).split('-')]
    
    
def checkBirthdayToday():
    getData()
    for i in range(len(Month)):
        for j in range(len(Month[i])):
            if Month[i][j]==str(today.month) and Month[i][j-1]==str(today.day):
                print("Listout the name of Person's who have birthday today!")
                print(Name[i])
                M.sendMail(Name[i],Email_ID[i]) #It will send Mail to the person
                M.sendWTPM(Name[i][j],Number[i]) #It will send Whatsapp Message to the person
            
def checkFestivalToday():
    getData()
    for i in range(len(Date)):
        for j in range(len(Date[i])):
            if str(today.month) == Date[i][j] and str(today.day) == Date[i][j-1]:
                for filename in os.listdir('.'):
                    if filename.startswith(Holiday[i]):
                        Text = open(Holiday[i]+".txt")
                        Text = Text.read() #Read or stored content of Holiday[i] toText variable. 
                        Photo = open(Holiday[i]+".png")
                        # This for loop will send emails to all present in table of Data. 
                        for mail in Email_ID:
                            M.sendFM(Text,Photo.name,mail)
                        
                        # This for loop will send Whatsapp Message to all present in table of Data.
                        for Number in Number:
                            M.sendFMWT(Number,Photo.name,Text)
                            Photo.close() # Closed opened file
                            
checkFestivalToday() # Festival Function Called
checkBirthdayToday() # Birthday Function Called



from email.message import EmailMessage # This will provides creating or modifying structured messages.
import imghdr # imghdr module-determines the type of image
import os
from PIL import Image #(PIL)-Python Image Library
import pywhatkit
import smtplib
import urllib.request # request module defines functions and classes which helpinopening URLs

msg = EmailMessage()
Sender_Mail = "xyz516332@gmail.com" 
password = "ktzvzolvtabzdoya" 

def sendMail(Name,Reciver_Mail):
    server = smtplib.SMTP('smtp.gmail.com',587) #Created gmail's server, and connected to gmail API
    # Adding transfer layered security  
    server.starttls()
    server.login(Sender_Mail,password) # Email, App password are inserted. 
    msg['Subject'] = 'Testing of HAPPY BIRTHDAY Service!' 
    msg['From'] = Sender_Mail
    msg['To'] = Reciver_Mail
    msg.set_content(f'Happiest Birthday {Name}!\nI Enjoy a Lot......!')
    urllib.request.urlretrieve('https://thumbs.dreamstime.com/b/colorful-happy- birthday-cupcakes-candles-spelling-148323072.jpg',"HBD.jpg")
    with open('HBD.jpg','rb') as f:
        file_data = f.read()
        file_type = imghdr.what(f.name)
        file_name = f.name
    msg.add_attachment(file_data,maintype='image',subtype=file_type,filename=file_name)
    server.send_message(msg)
    server.quit()

def sendWTPM(Name,Number):
    img = 'B1.jpg' 
    body = f'Many Many Returns of the Day {Name}!\nI hope all your birthday wishes and dreams come true.' 
    pywhatkit.sendwhats_image(Number,img,body,15,False,3)
    #FM: Festival Message

def sendFM(Text,Photo,Reciver_Mail):
    server = smtplib.SMTP('smtp.gmail.com',587) #Created gmail's server, and connected to gmail API
    # Adding transfer layered security
    server.starttls()
    server.login(Sender_Mail,password) # Email, App password are inserted. 
    msg['Subject'] = 'Testing of Festival Service!' 
    msg['From'] = Sender_Mail
    msg['To'] = Reciver_Mail
    msg.set_content(f'{Text}')
    with open(Photo,'rb') as f:
        file_data = f.read()
        file_type = imghdr.what(f.name)
        file_name = f.name
        msg.add_attachment(file_data,maintype='image',subtype=file_type,filename=file_name)
    
    server.send_message(msg)
    server.quit()

def sendFMWT(Number,Photo,Text):
    body = f'{Text}' 
    pywhatkit.sendwhats_image(Number,Photo,body,15,False,3)
    