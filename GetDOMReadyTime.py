from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re, os, datetime

class CreateContainer(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.set_window_size(1366, 768)
        self.driver.implicitly_wait(30)

        self.base_url = "http://smdp.com/"
        self.urlNames = ["","category/news", "category/business", "category/opinion", "category/sports", "category/life", "horoscopes", "category/notices", "about-us", "advertise", "pdf-reprints?pdfyear=14&pdfmonth=01", "category/news/obit", "category/news/city-council", "in-contention", "tv-tattle", "channels/realitytv", "category/sports/thesnideworldofsports"]#, "the-fien-print/fox-pushed-american-idol-back-an-hour-shifts-rake-to-fridays", "starr-raving/sex-sent-me-to-the-er-gets-a-jumbo-sized-order-from-tlc"]
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_GetDOMReadyTime(self):

        directory = "smdp.com Performance " + str(datetime.datetime.now()).replace(":", "-")
        if not os.path.exists(directory):
            os.makedirs(directory)
        os.chdir(directory)

        driver = self.driver
        for pageName in self.urlNames:
            if pageName == "":
                performanceFile = open("Home page performance", 'w')
            else:
                performanceFile = open(str(pageName.replace("/", "_") + str(" Performance")),'w')
            for i in range(4):
                driver.get(self.base_url + pageName)
                time.sleep(8)

                domComplete = driver.execute_script("return window.performance.timing.domComplete")
                responseStart = driver.execute_script("return window.performance.timing.responseStart")
                frontendPerformance = domComplete - responseStart

                performanceFile.write("Front-end performance of " + self.base_url + pageName + "   \n " + str(frontendPerformance) + " ms" + "\n End \n \n \n \n")

            performanceFile.close()

    def tearDown(self):
        self.driver.quit()
        print self.verificationErrors
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()