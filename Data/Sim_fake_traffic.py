from time import sleep
from io import  BytesIO
import pycurl


### Simulator for the changes to congestion ###

##### 15 intervals

waitTime = 2   # 15 * waittime = simulation time

##values###
cpcURL = 'http://10.18.0.132:2999/api/current_priority_congestion='
ncpcURL = 'http://10.18.0.132:2999/api/current_non_priority_congestion='


#------------------------------------------#
sleep(waitTime) #1st

c = pycurl.Curl()
storage =  BytesIO()
c = pycurl.Curl()
c.setopt(c.URL, ncpcURL+'10')
c.setopt(c.WRITEFUNCTION, storage.write)
c.perform()
c.close()


c = pycurl.Curl()
storage =  BytesIO()
c = pycurl.Curl()
c.setopt(c.URL, cpcURL+'5')
c.setopt(c.WRITEFUNCTION, storage.write)
c.perform()
c.close()

#------------------------------------------#
sleep(waitTime) #2nd

c = pycurl.Curl()
storage =  BytesIO()
c = pycurl.Curl()
c.setopt(c.URL, ncpcURL+'15')
c.setopt(c.WRITEFUNCTION, storage.write)
c.perform()
c.close()


c = pycurl.Curl()
storage =  BytesIO()
c = pycurl.Curl()
c.setopt(c.URL, cpcURL+'7')
c.setopt(c.WRITEFUNCTION, storage.write)
c.perform()
c.close()

#------------------------------------------#
sleep(waitTime) #3rd

c = pycurl.Curl()
storage =  BytesIO()
c = pycurl.Curl()
c.setopt(c.URL, ncpcURL+'20')
c.setopt(c.WRITEFUNCTION, storage.write)
c.perform()
c.close()


c = pycurl.Curl()
storage =  BytesIO()
c = pycurl.Curl()
c.setopt(c.URL, cpcURL+'7')
c.setopt(c.WRITEFUNCTION, storage.write)
c.perform()
c.close()

#------------------------------------------#
sleep(waitTime) #4th

c = pycurl.Curl()
storage =  BytesIO()
c = pycurl.Curl()
c.setopt(c.URL, ncpcURL+'20')
c.setopt(c.WRITEFUNCTION, storage.write)
c.perform()
c.close()


c = pycurl.Curl()
storage =  BytesIO()
c = pycurl.Curl()
c.setopt(c.URL, cpcURL+'7')
c.setopt(c.WRITEFUNCTION, storage.write)
c.perform()
c.close()


#------------------------------------------#
sleep(waitTime) #5th

c = pycurl.Curl()
storage =  BytesIO()
c = pycurl.Curl()
c.setopt(c.URL, ncpcURL+'30')
c.setopt(c.WRITEFUNCTION, storage.write)
c.perform()
c.close()


c = pycurl.Curl()
storage =  BytesIO()
c = pycurl.Curl()
c.setopt(c.URL, cpcURL+'7')
c.setopt(c.WRITEFUNCTION, storage.write)
c.perform()
c.close()

#------------------------------------------#
sleep(waitTime) #6th

c = pycurl.Curl()
storage =  BytesIO()
c = pycurl.Curl()
c.setopt(c.URL, ncpcURL+'35')
c.setopt(c.WRITEFUNCTION, storage.write)
c.perform()
c.close()


c = pycurl.Curl()
storage =  BytesIO()
c = pycurl.Curl()
c.setopt(c.URL, cpcURL+'7')
c.setopt(c.WRITEFUNCTION, storage.write)
c.perform()
c.close()

#------------------------------------------#
sleep(waitTime) #7th

c = pycurl.Curl()
storage =  BytesIO()
c = pycurl.Curl()
c.setopt(c.URL, ncpcURL+'40')
c.setopt(c.WRITEFUNCTION, storage.write)
c.perform()
c.close()


c = pycurl.Curl()
storage =  BytesIO()
c = pycurl.Curl()
c.setopt(c.URL, cpcURL+'7')
c.setopt(c.WRITEFUNCTION, storage.write)
c.perform()
c.close()

#------------------------------------------#
sleep(waitTime) #8th

c = pycurl.Curl()
storage =  BytesIO()
c = pycurl.Curl()
c.setopt(c.URL, ncpcURL+'40')
c.setopt(c.WRITEFUNCTION, storage.write)
c.perform()
c.close()


c = pycurl.Curl()
storage =  BytesIO()
c = pycurl.Curl()
c.setopt(c.URL, cpcURL+'10')
c.setopt(c.WRITEFUNCTION, storage.write)
c.perform()
c.close()

#------------------------------------------#
sleep(waitTime) #9th

c = pycurl.Curl()
storage =  BytesIO()
c = pycurl.Curl()
c.setopt(c.URL, ncpcURL+'40')
c.setopt(c.WRITEFUNCTION, storage.write)
c.perform()
c.close()


c = pycurl.Curl()
storage =  BytesIO()
c = pycurl.Curl()
c.setopt(c.URL, cpcURL+'14')
c.setopt(c.WRITEFUNCTION, storage.write)
c.perform()
c.close()

#------------------------------------------#
sleep(waitTime) #10th

c = pycurl.Curl()
storage =  BytesIO()
c = pycurl.Curl()
c.setopt(c.URL, ncpcURL+'40')
c.setopt(c.WRITEFUNCTION, storage.write)
c.perform()
c.close()


c = pycurl.Curl()
storage =  BytesIO()
c = pycurl.Curl()
c.setopt(c.URL, cpcURL+'20')
c.setopt(c.WRITEFUNCTION, storage.write)
c.perform()
c.close()

#------------------------------------------#
sleep(waitTime) #11th

c = pycurl.Curl()
storage =  BytesIO()
c = pycurl.Curl()
c.setopt(c.URL, ncpcURL+'40')
c.setopt(c.WRITEFUNCTION, storage.write)
c.perform()
c.close()


c = pycurl.Curl()
storage =  BytesIO()
c = pycurl.Curl()
c.setopt(c.URL, cpcURL+'20')
c.setopt(c.WRITEFUNCTION, storage.write)
c.perform()
c.close()

#------------------------------------------#
sleep(waitTime) #12th

c = pycurl.Curl()
storage =  BytesIO()
c = pycurl.Curl()
c.setopt(c.URL, ncpcURL+'35')
c.setopt(c.WRITEFUNCTION, storage.write)
c.perform()
c.close()


c = pycurl.Curl()
storage =  BytesIO()
c = pycurl.Curl()
c.setopt(c.URL, cpcURL+'15')
c.setopt(c.WRITEFUNCTION, storage.write)
c.perform()
c.close()

#------------------------------------------#
sleep(waitTime) #13th

c = pycurl.Curl()
storage =  BytesIO()
c = pycurl.Curl()
c.setopt(c.URL, ncpcURL+'30')
c.setopt(c.WRITEFUNCTION, storage.write)
c.perform()
c.close()


c = pycurl.Curl()
storage =  BytesIO()
c = pycurl.Curl()
c.setopt(c.URL, cpcURL+'10')
c.setopt(c.WRITEFUNCTION, storage.write)
c.perform()
c.close()

#------------------------------------------#
sleep(waitTime) #14th

c = pycurl.Curl()
storage =  BytesIO()
c = pycurl.Curl()
c.setopt(c.URL, ncpcURL+'20')
c.setopt(c.WRITEFUNCTION, storage.write)
c.perform()
c.close()


c = pycurl.Curl()
storage =  BytesIO()
c = pycurl.Curl()
c.setopt(c.URL, cpcURL+'5')
c.setopt(c.WRITEFUNCTION, storage.write)
c.perform()
c.close()

#------------------------------------------#
sleep(waitTime) #15th

c = pycurl.Curl()
storage =  BytesIO()
c = pycurl.Curl()
c.setopt(c.URL, ncpcURL+'10')
c.setopt(c.WRITEFUNCTION, storage.write)
c.perform()
c.close()


c = pycurl.Curl()
storage =  BytesIO()
c = pycurl.Curl()
c.setopt(c.URL, cpcURL+'2')
c.setopt(c.WRITEFUNCTION, storage.write)
c.perform()
c.close()

