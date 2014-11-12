# cyclicGroup = [0, 1, 2, 3, 4, 5]
cyclicGroup = [0, 1, 2, 3, 4]
cyclicGroup.sort()

for number in cyclicGroup:
	auxCyclicGroup = []
	for testGen in xrange(1, len(cyclicGroup) + 1):
		congruent = (number * testGen) % len(cyclicGroup)
		auxCyclicGroup.append(congruent)
	auxCyclicGroup.sort()
	if cyclicGroup == auxCyclicGroup:
		print "Number " + str(number) + " is generator!"