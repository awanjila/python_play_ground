'''def listsum(numlist):
	thesum=0
	for i in numlist:
		thesum=thesum+1
	returm thesum
print(listsum([1,2,3,4,5]))
'''


def listsum(numlist):
	if len(numlist)==1:
		return numlist[0]
	else:
		return numlist[0] + listsum(numlist[1:])
print(listsum([1,2,3,4,5]))


