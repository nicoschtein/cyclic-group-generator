# cyclicGroup = [0, 1, 2, 3, 4, 5]
cyclicGroup = [0, 1, 2, 3, 4]
cyclicGroup.sort()
debug = 1
for number in cyclicGroup:
	auxCyclicGroup = []
	if debug:
		print "testing number: " + str(number)
	for testGen in xrange(1, len(cyclicGroup) + 1):
		if debug:
			print "    testgen: " + str(testGen)
		congruent = (number * testGen) % len(cyclicGroup)
		auxCyclicGroup.append(congruent)
		if debug:
			print "    cic: " + str(auxCyclicGroup)
	auxCyclicGroup.sort()
	if cyclicGroup == auxCyclicGroup:
		print "  Number " + str(number) + " is generator!"