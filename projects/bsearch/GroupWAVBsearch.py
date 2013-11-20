#Hezekiah
#Michelle
#Sacha
#Eboni
#Ashanti
#Tyler

waveList = ['Too', 'Wavy', 'For', 'These', 'Jawns', 'Cause', 'Im', 'From', 'Atlantis']

def bsearch():
	lo = 0
	hi = len(waveList)- 1
	target = False
	destination = waveList[5]
	while lo < hi and target == False:
		mid = ((lo + hi)//2)
		if waveList[mid] < destination:
			lo = mid + 1
		elif waveList[mid] > destination:
			hi = mid - 1
		else:
			target = True
	if target:
		print 'Success'
	else:
		print '-1'		

bsearch ()
