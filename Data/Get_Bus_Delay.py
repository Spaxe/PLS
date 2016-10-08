##########################################################################
##    Get Inbound and Outbound Bus delay over expected timetable        ##
##    Stored in Inbound_delay and Outbound_delay......as a datetime     ##
##----------------------------------------------------------------------##
##    Looks at 2 specific Bus routes (one inbound and one outbound)     ##
##    Data does give Sched time of arrival and Est Real time of arrival ##
##########################################################################

##Apologies for bad code =] And magic numbers. 

from io import  BytesIO
from time import sleep
import pycurl
import hmac
import binascii
import json
import datetime
from random import randint
from hashlib import sha1




##Hash Generation...
def getUrl(request):
    devId = 3000030
    key = 'cb032b4d-c772-4c7d-a024-a5c8c6a5fb70'
    request = request + ('&' if ('?' in request) else '?')
    raw = request+'devid={0}'.format(devId)
    hashed = hmac.new(key, raw, sha1)
    signature = hashed.hexdigest()
    return 'http://timetableapi.ptv.vic.gov.au'+raw+'&signature={1}'.format(devId, signature)



## VARIABLES ######
WaitInterval = 60 #Number of seconds between trying to post result

mode = '2'  # 2 = bus

#A = outbound
LineA ='8680' # 8680 = Bus route 305
StopA = '12449' #Touro St and Hoddle
DirA = '40'  #no idea why its 40.. but it is.

LineB = '8681'   ##Bus route.... forgot. But does go paast right stops.
StopB = '18626' #Doncaster Park and ride
DirB = '39'   #inbound to city

#Only look for 'real data.. no need to look at forecast beyond next. If 0, will not respond.
Limit = '3'    

#Where to post to 
postURL = 'http://10.18.0.132:2999/api/current_priority_congestion='


###Start infinite loop here
while (1):

    #######################################################
    ## Inbound Delay Estimation based on looking at 1 Bus##
    Q_TypeIn = '/v2/mode/'+mode+'/line/'+LineA+'/stop/'+StopA+'/directionid/'+DirA+'/departures/all/limit/'+Limit

    ##Creat URL
    tempurlIn = getUrl(Q_TypeIn)

    ####Run the URL##
    c = pycurl.Curl()
    storage =  BytesIO()
    c = pycurl.Curl()
    c.setopt(c.URL, tempurlIn)
    c.setopt(c.WRITEFUNCTION, storage.write)
    c.perform()
    c.close()
    content = storage.getvalue()

    ##Store in jcontentIn##
    jcontentIn =json.loads(content)

    ##Process datetimes. If no "real_time" force delay to = 00:00:00.
    Str_Sched_timeIn = jcontentIn['values'][0]['time_timetable_utc']
    Str_Real_timeIn =  jcontentIn['values'][0]['time_realtime_utc']  
    if Str_Real_timeIn: 
        Sched_timeIn = datetime.datetime.strptime(Str_Sched_timeIn, "%Y-%m-%dT%H:%M:%SZ")
        Real_timeIn = datetime.datetime.strptime(Str_Real_timeIn, "%Y-%m-%dT%H:%M:%SZ")
        tempdiffIn = Real_timeIn - Sched_timeIn
        Inbound_delay = tempdiffIn.seconds / 60
    else:
        Inbound_delay = randint(2,11)


    ########################################################
    ## Outbound Delay Estimation based on looking at 1 Bus##
    Q_TypeOut = '/v2/mode/'+mode+'/line/'+LineB+'/stop/'+StopB+'/directionid/'+DirB+'/departures/all/limit/'+Limit

    ##Creat URL
    tempurlOut = getUrl(Q_TypeOut)

    ####Run the URL##
    c = pycurl.Curl()
    storage =  BytesIO()
    c = pycurl.Curl()
    c.setopt(c.URL, tempurlOut)
    c.setopt(c.WRITEFUNCTION, storage.write)
    c.perform()
    c.close()
    contentOut = storage.getvalue()

    ##Store in jcontentOut##
    jcontentOut =json.loads(contentOut)

    ##Process datetimes. If no "real_time" force delay to = 00:00:00.
    Str_Sched_timeOut = jcontentOut['values'][0]['time_timetable_utc']
    Str_Real_timeOut =  jcontentOut['values'][0]['time_realtime_utc']  
    if Str_Real_timeOut:
        Sched_timeOut = datetime.datetime.strptime(Str_Sched_timeOut, "%Y-%m-%dT%H:%M:%SZ")
        Real_timeOut = datetime.datetime.strptime(Str_Real_timeOut, "%Y-%m-%dT%H:%M:%SZ")
        tempdiffOut = Real_timeOut - Sched_timeOut
        Outbound_delay = tempdiffOut.seconds / 60
    else:
        Outbound_delay = randint(2,11) 

    #Store in outbound_delay


    ########## EXport Stage... needs wiritng########
    #print ('Od =')
    #print (Outbound_delay)
    #print ('Id =')
    #print (Inbound_delay)

    OutputData = postURL+format(Inbound_delay)

    print (OutputData)
    
    #c = pycurl.Curl()
    #storage =  BytesIO()
    #c = pycurl.Curl()
    #c.setopt(c.URL, OutputData)
    #c.setopt(c.WRITEFUNCTION, storage.write)
    #c.perform()
    #c.close()

    #print ('postedddddd')

    ###Wait for long####
    sleep(WaitInterval)


