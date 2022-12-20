#Implementetion of OTP assignment as per OOP design.
import random
import senders_data as Get
import smtplib
import unittest

class generate_otp(unittest.TestCase):

    #Fetching Login credentials from the senderdata file
    Sender_Mail = Get.email
    PassWord = Get.password

    def _init_(self,receivers_name,receivers_email,n):
        self.receivers_name=receivers_name
        self.receivers_email=receivers_email
        self.n=n
        OTP=self.create_otp(self.n)
        

        #Testing length of OTP.
        self.assertBetween(self.n,4,8)

        #Validation of the Email ID
        self.validation()

        self.send_email(OTP)
    
    def create_otp(self,n):
        self.n=n
        OTP=""
        for i in range(self.n):
            OTP+=str(random.randint(0,9))
        return (OTP)    

    
    def str(self) :
        return ('{} has {} as an email'.format(self.receivers_name,self.receivers_email))

    
    def assertBetween(self, n, low, hi):
        if not (low <= n <= hi):
            raise AssertionError('Length of OTP is %r must be in between %r and %r' % (n, low, hi))
        print("**************************************************************************************")
    
    def validation(self):
        email="suyogpardhi1820@gmail.com"
        check_email =("@" and "gmail" and "."and "com") in email #self.receivers_email
        if check_email:
            print("No error in email")
        else:
            self.assertTrue(check_email)

    def send_email(self,OTP):
        server=smtplib.SMTP('smtp.gmail.com',587)
        server.starttls()
        server.login(self.Sender_Mail,self.PassWord)
        
        msg=('Hi {}\n{} is your One Time Password(OTP)'.format(self.receivers_name,OTP))
        print(msg)
        server.sendmail(self.Sender_Mail,self.receivers_email,msg)
        server.quit()
        print("Email sent!")



g=generate_otp('Suyog','suyogpardhi1820@gmail.com',4)