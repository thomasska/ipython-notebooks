#!/usr/bin/env python
import pexpect

def getreading(IP):
    #print 'getting readings from %s' % IP
    outstring=''

    outstring = outstring + IP + ','

    try:
        child = pexpect.spawn('telnet %s' % IP)
        child.expect ('User Name : ',timeout=1)
        child.send ('apc\r')
        child.expect ('Password  : ',timeout=1)
        child.send ('meerkatpdu\r')
        child.expect ('Name      : ')
        child.expect ('Date :')
        temp = child.before
        outstring = outstring + temp.rstrip() + ','
        child.expect ('apc>',timeout=2)
    except:
        outstring = outstring + 'ERROR' + ',0,0,0,0,0,0,0,0,0,0'
        return outstring

    try:
        child.send ('devReading 1:power\r')
        child.expect ('E000: Success',timeout=2)
        child.expect ('apc>',timeout=2)
        temp = child.before
        thisline = temp.split('\r\n')[1]
        outstring = outstring + thisline.split(' ')[0] + ','
    except:
        outstring = outstring + '0,0,0,0,0,0,0,0,0,0'
        return outstring

    try:
        child.send ('phReading 1:all power\r')
        child.expect ('E000: Success',timeout=2)
        child.expect ('apc>',timeout=2)
        temp = child.before
        for thisline in temp.split('\r\n')[1:4]:
            outstring = outstring + thisline.split(' ')[1] + ','
    except:
        outstring = outstring + '0,0,0,0,0,0,0,0,0'
        return outstring


    try:
        child.send ('phReading 1:all current\r')
        child.expect ('E000: Success', timeout=2)
        child.expect ('apc>',timeout=2)
        temp = child.before
        for thisline in temp.split('\r\n')[1:4]:
            outstring = outstring + thisline.split(' ')[1] + ','
    except:
        outstring = outstring + '0,0,0,0,0,0'
        return outstring


    try:
        child.send ('phReading 1:all pf\r')
        child.expect ('E000: Success', timeout=2)
        child.expect ('apc>',timeout=2)
        temp = child.before
        for thisline in temp.split('\r\n')[1:4]:
            outstring = outstring + thisline.split(' ')[1] + ','
    except:
        outstring = outstring + '0,0,0'
        return outstring

    child.send ('quit\r')

    return outstring[:-1]    # strip trailing comma


# this list from the MeerKAT IP List spreadsheet, 6 October 2016
iplist=['10.99.3.1',
'10.99.3.3',
'10.99.3.2',
'10.99.3.5',
'10.99.3.4',
'10.99.3.7',
'10.99.3.6',
'10.99.3.9',
'10.99.3.8',
'10.99.3.11',
'10.99.3.10',
'10.99.3.12',
'10.99.3.13',
'10.99.3.14',
'10.99.3.15',
'10.99.3.16',
'10.99.3.30',
'10.99.3.31',
'10.99.3.32',
'10.99.3.33',
'10.99.3.34',
'10.99.3.35',
'10.99.3.36',
'10.99.3.37',
'10.99.3.38',
'10.99.3.39',
'10.99.3.40',
'10.99.3.41',
'10.99.3.42',
'10.99.3.43',
'10.99.3.44',
'10.99.3.45',
'10.99.3.46',
'10.99.3.60',
'10.99.3.61',
'10.99.3.62',
'10.99.3.63',
'10.99.3.64',
'10.99.3.65',
'10.99.3.66',
'10.99.3.67',
'10.99.3.68',
'10.99.3.69',
'10.99.3.80',
'10.99.3.81',
'10.99.3.82',
'10.99.3.90']



print 'IP,Name,TotalkW,ph1kW,ph2kW,ph3kW,ph1A,ph2A,ph3A,ph1PF,ph2PF,ph3PF'
for IP in iplist:
    print getreading(IP)
#print getreading('10.99.99.99')   # this will definitely throw an error

