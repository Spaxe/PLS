from time import sleep
from io import  BytesIO
import pycurl


### Simulator for the changes to congestion ###

##### 15 intervals

waitTime = 4   # 10 * waittime = simulation time

##values###
cpcURL = 'http://10.18.0.132:2999/api/current_priority_congestion='
ncpcURL = 'http://10.18.0.132:2999/api/current_non_priority_congestion='

print ('start')

#------------------------------------------#
sleep(waitTime) #1st

c = pycurl.Curl()
storage =  BytesIO()
c = pycurl.Curl()
c.setopt(c.URL, ncpcURL)
c.setopt(pycurl.HTTPHEADER, ['content-type: application/x-www/form-urlencoded'])
c.setopt(pycurl.POST, 1)
c.setopt(pycurl.POSTFIELDS, 'congestion=10')
c.setopt(c.WRITEFUNCTION, storage.write)
c.perform()
c.close()

c = pycurl.Curl()
storage =  BytesIO()
c = pycurl.Curl()
c.setopt(c.URL, cpcURL)
c.setopt(pycurl.HTTPHEADER, ['content-type: application/x-www/form-urlencoded'])
c.setopt(pycurl.POST, 1)
c.setopt(pycurl.POSTFIELDS, 'congestion=5')
c.setopt(c.WRITEFUNCTION, storage.write)
c.perform()
c.close()

print ('*')
#------------------------------------------#
sleep(waitTime) #2

c = pycurl.Curl()
storage =  BytesIO()
c = pycurl.Curl()
c.setopt(c.URL, ncpcURL)
c.setopt(pycurl.HTTPHEADER, ['content-type: application/x-www/form-urlencoded'])
c.setopt(pycurl.POST, 1)
c.setopt(pycurl.POSTFIELDS, 'congestion=15')
c.setopt(c.WRITEFUNCTION, storage.write)
c.perform()
c.close()

c = pycurl.Curl()
storage =  BytesIO()
c = pycurl.Curl()
c.setopt(c.URL, cpcURL)
c.setopt(pycurl.HTTPHEADER, ['content-type: application/x-www/form-urlencoded'])
c.setopt(pycurl.POST, 1)
c.setopt(pycurl.POSTFIELDS, 'congestion=5')
c.setopt(c.WRITEFUNCTION, storage.write)
c.perform()
c.close()
print ('*')
#------------------------------------------#
sleep(waitTime) #2

c = pycurl.Curl()
storage =  BytesIO()
c = pycurl.Curl()
c.setopt(c.URL, ncpcURL)
c.setopt(pycurl.HTTPHEADER, ['content-type: application/x-www/form-urlencoded'])
c.setopt(pycurl.POST, 1)
c.setopt(pycurl.POSTFIELDS, 'congestion=25')
c.setopt(c.WRITEFUNCTION, storage.write)
c.perform()
c.close()

c = pycurl.Curl()
storage =  BytesIO()
c = pycurl.Curl()
c.setopt(c.URL, cpcURL)
c.setopt(pycurl.HTTPHEADER, ['content-type: application/x-www/form-urlencoded'])
c.setopt(pycurl.POST, 1)
c.setopt(pycurl.POSTFIELDS, 'congestion=8')
c.setopt(c.WRITEFUNCTION, storage.write)
c.perform()
c.close()
print ('*')
#------------------------------------------#
sleep(waitTime) #2

c = pycurl.Curl()
storage =  BytesIO()
c = pycurl.Curl()
c.setopt(c.URL, ncpcURL)
c.setopt(pycurl.HTTPHEADER, ['content-type: application/x-www/form-urlencoded'])
c.setopt(pycurl.POST, 1)
c.setopt(pycurl.POSTFIELDS, 'congestion=30')
c.setopt(c.WRITEFUNCTION, storage.write)
c.perform()
c.close()

c = pycurl.Curl()
storage =  BytesIO()
c = pycurl.Curl()
c.setopt(c.URL, cpcURL)
c.setopt(pycurl.HTTPHEADER, ['content-type: application/x-www/form-urlencoded'])
c.setopt(pycurl.POST, 1)
c.setopt(pycurl.POSTFIELDS, 'congestion=10')
c.setopt(c.WRITEFUNCTION, storage.write)
c.perform()
c.close()

print ('*')
#------------------------------------------#
sleep(waitTime) #2

c = pycurl.Curl()
storage =  BytesIO()
c = pycurl.Curl()
c.setopt(c.URL, ncpcURL)
c.setopt(pycurl.HTTPHEADER, ['content-type: application/x-www/form-urlencoded'])
c.setopt(pycurl.POST, 1)
c.setopt(pycurl.POSTFIELDS, 'congestion=30')
c.setopt(c.WRITEFUNCTION, storage.write)
c.perform()
c.close()

c = pycurl.Curl()
storage =  BytesIO()
c = pycurl.Curl()
c.setopt(c.URL, cpcURL)
c.setopt(pycurl.HTTPHEADER, ['content-type: application/x-www/form-urlencoded'])
c.setopt(pycurl.POST, 1)
c.setopt(pycurl.POSTFIELDS, 'congestion=12')
c.setopt(c.WRITEFUNCTION, storage.write)
c.perform()
c.close()

print ('*')
#------------------------------------------#
sleep(waitTime) #2

c = pycurl.Curl()
storage =  BytesIO()
c = pycurl.Curl()
c.setopt(c.URL, ncpcURL)
c.setopt(pycurl.HTTPHEADER, ['content-type: application/x-www/form-urlencoded'])
c.setopt(pycurl.POST, 1)
c.setopt(pycurl.POSTFIELDS, 'congestion=40')
c.setopt(c.WRITEFUNCTION, storage.write)
c.perform()
c.close()

c = pycurl.Curl()
storage =  BytesIO()
c = pycurl.Curl()
c.setopt(c.URL, cpcURL)
c.setopt(pycurl.HTTPHEADER, ['content-type: application/x-www/form-urlencoded'])
c.setopt(pycurl.POST, 1)
c.setopt(pycurl.POSTFIELDS, 'congestion=20')
c.setopt(c.WRITEFUNCTION, storage.write)
c.perform()
c.close()

print ('*')
#------------------------------------------#
sleep(waitTime) #2

c = pycurl.Curl()
storage =  BytesIO()
c = pycurl.Curl()
c.setopt(c.URL, ncpcURL)
c.setopt(pycurl.HTTPHEADER, ['content-type: application/x-www/form-urlencoded'])
c.setopt(pycurl.POST, 1)
c.setopt(pycurl.POSTFIELDS, 'congestion=40')
c.setopt(c.WRITEFUNCTION, storage.write)
c.perform()
c.close()

c = pycurl.Curl()
storage =  BytesIO()
c = pycurl.Curl()
c.setopt(c.URL, cpcURL)
c.setopt(pycurl.HTTPHEADER, ['content-type: application/x-www/form-urlencoded'])
c.setopt(pycurl.POST, 1)
c.setopt(pycurl.POSTFIELDS, 'congestion=20')
c.setopt(c.WRITEFUNCTION, storage.write)
c.perform()
c.close()

print ('*')
#------------------------------------------#
sleep(waitTime) #2

c = pycurl.Curl()
storage =  BytesIO()
c = pycurl.Curl()
c.setopt(c.URL, ncpcURL)
c.setopt(pycurl.HTTPHEADER, ['content-type: application/x-www/form-urlencoded'])
c.setopt(pycurl.POST, 1)
c.setopt(pycurl.POSTFIELDS, 'congestion=30')
c.setopt(c.WRITEFUNCTION, storage.write)
c.perform()
c.close()

c = pycurl.Curl()
storage =  BytesIO()
c = pycurl.Curl()
c.setopt(c.URL, cpcURL)
c.setopt(pycurl.HTTPHEADER, ['content-type: application/x-www/form-urlencoded'])
c.setopt(pycurl.POST, 1)
c.setopt(pycurl.POSTFIELDS, 'congestion=15')
c.setopt(c.WRITEFUNCTION, storage.write)
c.perform()
c.close()

print ('*')
#------------------------------------------#
sleep(waitTime) #2

c = pycurl.Curl()
storage =  BytesIO()
c = pycurl.Curl()
c.setopt(c.URL, ncpcURL)
c.setopt(pycurl.HTTPHEADER, ['content-type: application/x-www/form-urlencoded'])
c.setopt(pycurl.POST, 1)
c.setopt(pycurl.POSTFIELDS, 'congestion=20')
c.setopt(c.WRITEFUNCTION, storage.write)
c.perform()
c.close()

c = pycurl.Curl()
storage =  BytesIO()
c = pycurl.Curl()
c.setopt(c.URL, cpcURL)
c.setopt(pycurl.HTTPHEADER, ['content-type: application/x-www/form-urlencoded'])
c.setopt(pycurl.POST, 1)
c.setopt(pycurl.POSTFIELDS, 'congestion=10')
c.setopt(c.WRITEFUNCTION, storage.write)
c.perform()
c.close()

print ('*')
#------------------------------------------#
#------------------------------------------#
sleep(waitTime) #2

c = pycurl.Curl()
storage =  BytesIO()
c = pycurl.Curl()
c.setopt(c.URL, ncpcURL)
c.setopt(pycurl.HTTPHEADER, ['content-type: application/x-www/form-urlencoded'])
c.setopt(pycurl.POST, 1)
c.setopt(pycurl.POSTFIELDS, 'congestion=15')
c.setopt(c.WRITEFUNCTION, storage.write)
c.perform()
c.close()

c = pycurl.Curl()
storage =  BytesIO()
c = pycurl.Curl()
c.setopt(c.URL, cpcURL)
c.setopt(pycurl.HTTPHEADER, ['content-type: application/x-www/form-urlencoded'])
c.setopt(pycurl.POST, 1)
c.setopt(pycurl.POSTFIELDS, 'congestion=5')
c.setopt(c.WRITEFUNCTION, storage.write)
c.perform()
c.close()

print ('*')
#------------------------------------------#
sleep(waitTime) #2

c = pycurl.Curl()
storage =  BytesIO()
c = pycurl.Curl()
c.setopt(c.URL, ncpcURL)
c.setopt(pycurl.HTTPHEADER, ['content-type: application/x-www/form-urlencoded'])
c.setopt(pycurl.POST, 1)
c.setopt(pycurl.POSTFIELDS, 'congestion=10')
c.setopt(c.WRITEFUNCTION, storage.write)
c.perform()
c.close()

c = pycurl.Curl()
storage =  BytesIO()
c = pycurl.Curl()
c.setopt(c.URL, cpcURL)
c.setopt(pycurl.HTTPHEADER, ['content-type: application/x-www/form-urlencoded'])
c.setopt(pycurl.POST, 1)
c.setopt(pycurl.POSTFIELDS, 'congestion=3')
c.setopt(c.WRITEFUNCTION, storage.write)
c.perform()
c.close()


print ('*')

sleep(waitTime) #2

c = pycurl.Curl()
storage =  BytesIO()
c = pycurl.Curl()
c.setopt(c.URL, ncpcURL)
c.setopt(pycurl.HTTPHEADER, ['content-type: application/x-www/form-urlencoded'])
c.setopt(pycurl.POST, 1)
c.setopt(pycurl.POSTFIELDS, 'congestion=10')
c.setopt(c.WRITEFUNCTION, storage.write)
c.perform()
c.close()

c = pycurl.Curl()
storage =  BytesIO()
c = pycurl.Curl()
c.setopt(c.URL, cpcURL)
c.setopt(pycurl.HTTPHEADER, ['content-type: application/x-www/form-urlencoded'])
c.setopt(pycurl.POST, 1)
c.setopt(pycurl.POSTFIELDS, 'congestion=3')
c.setopt(c.WRITEFUNCTION, storage.write)
c.perform()
c.close()
print ('*')

sleep(waitTime) #2

c = pycurl.Curl()
storage =  BytesIO()
c = pycurl.Curl()
c.setopt(c.URL, ncpcURL)
c.setopt(pycurl.HTTPHEADER, ['content-type: application/x-www/form-urlencoded'])
c.setopt(pycurl.POST, 1)
c.setopt(pycurl.POSTFIELDS, 'congestion=10')
c.setopt(c.WRITEFUNCTION, storage.write)
c.perform()
c.close()

c = pycurl.Curl()
storage =  BytesIO()
c = pycurl.Curl()
c.setopt(c.URL, cpcURL)
c.setopt(pycurl.HTTPHEADER, ['content-type: application/x-www/form-urlencoded'])
c.setopt(pycurl.POST, 1)
c.setopt(pycurl.POSTFIELDS, 'congestion=3')
c.setopt(c.WRITEFUNCTION, storage.write)
c.perform()
c.close()

print ('*')
sleep(waitTime) #2

c = pycurl.Curl()
storage =  BytesIO()
c = pycurl.Curl()
c.setopt(c.URL, ncpcURL)
c.setopt(pycurl.HTTPHEADER, ['content-type: application/x-www/form-urlencoded'])
c.setopt(pycurl.POST, 1)
c.setopt(pycurl.POSTFIELDS, 'congestion=10')
c.setopt(c.WRITEFUNCTION, storage.write)
c.perform()
c.close()

c = pycurl.Curl()
storage =  BytesIO()
c = pycurl.Curl()
c.setopt(c.URL, cpcURL)
c.setopt(pycurl.HTTPHEADER, ['content-type: application/x-www/form-urlencoded'])
c.setopt(pycurl.POST, 1)
c.setopt(pycurl.POSTFIELDS, 'congestion=3')
c.setopt(c.WRITEFUNCTION, storage.write)
c.perform()
c.close()

print ('*')


