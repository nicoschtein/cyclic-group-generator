# cyclicGroup = [0, 1, 2, 3, 4, 5]
cyclicGroup = [1, 2, 3, 4]
cyclicGroup.sort()
debug = 1
for number in cyclicGroup:
	auxCyclicGroup = []
	if debug:
		print "testing number: " + str(number)
	accum = number
	for cycle in xrange(1, len(cyclicGroup) + 1):
		if debug:
			print "    ("+ str(cycle) +") accum: " + str(accum)
		accum = (accum * number) % (len(cyclicGroup) + 1)
		auxCyclicGroup.append(accum)
		if debug:
			print "    cic: " + str(auxCyclicGroup)
	auxCyclicGroup.sort()
	if cyclicGroup == auxCyclicGroup:
		print "  Number " + str(number) + " is generator!"