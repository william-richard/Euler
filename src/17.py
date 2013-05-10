'''
Created on Jan 29, 2013

@author: Will
'''

units = {'0':'', '1': 'one', '2': 'two', '3':'three', '4':'four', '5':'five','6':'six','7':'seven','8':'eight','9':'nine', '10':'ten', '11':'eleven', '12':'twelve','13':'thirteen','14':'fourteen', '15':'fifteen', '16':'sixteen','17':'seventeen','18':'eighteen','19':'nineteen'}
tens = ['', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'senventy', 'eighty', 'ninty']
scales = ["hundred", "thousand", "million", "billion", "trillion"] 

def getIntLen(i):
    length = 0
    if i < 10:
        length += len(units[str(i)])
        return length
    
    if len(str(i)) >= 3:
        for j in range(1, len(str(i))):
            if int(str(i)[j+2]) > 0:
                length += len(scales[j])
                length += len(units[str(i)[j]])
                print j, scales[j]
    print length
    if int(str(i)[-2:]) == 0:
        pass        
    elif 9 < int(str(i)[-2:]) < 20:
        length += len('and') 
        length +=  len(units[str(i)[-2:]])
    else:
        length += len('and') 
        length += len(units[str(i)[-1]])
        length += len(tens[int(str(i)[-2])])

    
    return length

if __name__ == '__main__':
    #tot = 0
    #for i in range(1,1001):
    #    tot += getIntLen(i)
    #print getIntLen(1000)
    #print len(units['1']) + len(scales[1])
    #print tot
    
    tot = 0
    #0 - 19 for 1, 101, 201...
    for v in units.values():
        tot += len(v) * 10
    #21, 121, 221...
    for i in range(11):
        tot += len(units[str(i)]) * 80
    #2x, 12x, 22x...
    for v in tens:
        tot += len(v) * 100
    #hundreds
    tot += len('hundred') * 9
    for i in range(11):
        tot += len(units[str(i)]) * 100
    #ands
    tot += len('and') * 900
    print tot
    
    
    
    