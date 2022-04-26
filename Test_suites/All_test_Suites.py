import unittest
from Package_1.TC_login_test import LoginTest
from Package_1.TC_signup_test import SignupTest

from Package_2.TC_payment_test import PaymentTest
from Package_2.TC_paymentReturns_test import PaymentReturnTest

# Get all test cases from LoginTest, SignUpTest, PaymentTest and PaymentReturnTest

tc1 = unittest.TestLoader().loadTestsFromTestCase(LoginTest)
tc2 = unittest.TestLoader().loadTestsFromTestCase(SignupTest)
tc3 = unittest.TestLoader().loadTestsFromTestCase(PaymentTest)
tc4 = unittest.TestLoader().loadTestsFromTestCase(PaymentReturnTest)

# Creatin Test Suites

sanityTestSuite = unittest.TestSuite([tc1, tc2])
functionalTestSuite = unittest.TestSuite([tc3, tc4])
masterTestSuite = unittest.TestSuite([tc1, tc2, tc3, tc4])

'''unittest.TextTestRunner().run(functionalTestSuite)
unittest.TextTestRunner().run(sanityTestSuite)
unittest.TextTestRunner().run(masterTestSuite)'''

unittest.TextTestRunner(verbosity=2).run(masterTestSuite)       # gives details