import copy
import sys	
import collections

if len(sys.argv) == 1:
	print "\n#################################"
	print "# Cyclic Group Generator Finder #"
	print "#################################\n"
	print "Usage  : " + sys.argv[0] + " --debug (optional) [group list] (required)"
	print "Example: " + sys.argv[0] + " --debug 0 1 2 3 4\n"
	sys.exit(0)

#init
cyclicGroup=copy.deepcopy(sys.argv);
showLogs=0
if(cyclicGroup[1] == "debug"):
	showLogs=1
	cyclicGroup.pop(1)
cyclicGroup.remove(cyclicGroup[0])
cyclicGroup.sort()
	
def checkIfNumberIsGenerator(number):
	if showLogs:
		print "testing number: " + str(number)
	accum = int(number)
	for cycle in xrange(1, len(cyclicGroup) + 1):
		if showLogs:
			print "    ("+ str(cycle) +") accum: " + str(accum)
		accum = (int(accum) * int(number)) % (len(cyclicGroup) + 1)
		auxCyclicGroup.append(str(accum))
		if showLogs:
			print "    cic: " + str(auxCyclicGroup)
	auxCyclicGroup.sort() 
	return collections.Counter(cyclicGroup) == collections.Counter(auxCyclicGroup)

for number in cyclicGroup:
	auxCyclicGroup = []
	if checkIfNumberIsGenerator(number):
		print "  Number " + str(number) + " is generator!"
	
