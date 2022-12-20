import unittest
import smtplib
import genratorOTP as O

class BetweenAssertMixin(object):
    def assertBetween(self, x, low, hi):
        if not (low <= x <= hi):
            raise AssertionError('Length of OTP is %r should be in between %r and %r' % (x, low, hi))

class OTP(unittest.TestCase,BetweenAssertMixin):
    def testcase1(self):
        #Checking Email
        Name = "Suyog"
        Email = "suyogpardhi1820@gmail.com"
        self.assertIn("@",Email)
        self.assertIn(".",Email)
        self.assertIn("com",Email)
        True_Str1 = "gmail" in Email
        if True_Str1 or True_Str2:
            print("No Error Found in Email!")
        else:
            self.assertTrue(True_Str1)

        #Checking OTP
        otp = O.genrateOtp()
        self.assertBetween(len(otp),4,8)

        #Calling Sendmail Function
        O.sendMail(Name,Email,otp)
        print()

    def testcase2(self):
        #Checking Email 
        Name = "Suyog"
        Email = "suyogpardhi1820@gmail.com"
        self.assertIn("@",Email)
        self.assertIn(".",Email)
        self.assertIn("com",Email)
        True_Str1 = "gmail" in Email
        if True_Str1:
            print("No Error Found in Email!")
        else:
            self.assertTrue(True_Str1)

        #Checking OTP
        otp = O.genrateOtp()
        self.assertBetween(len(otp),4,8)
        
        #Calling Sendmail Function
        O.sendMail(Name,Email,otp)
        print()

    def testcase3(self):
        #Checking Email
        Name = "Suyog"
        Email = "suyogpardhi1820@gmail.com"
        self.assertIn("@",Email)
        self.assertIn(".",Email)
        self.assertIn("com",Email)
        True_Str1 = "gmail" in Email
        if True_Str1 or True_Str2:
            print("No Error Found in Email!")
        else:
            self.assertTrue(True_Str1)

        #Checking OTP
        # Here i will Enter invalid otp length
        otp = O.genrateOtp()
        self.assertBetween(len(otp),4,8)

        #Calling Sendmail Function
        O.sendMail(Name,Email,otp)

unittest.main()