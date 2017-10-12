file_name = 'citation_network'
with open(file_name,'r') as myfile:
	citations = myfile.read().splitlines()

bibliographic_couplings = {}
cocitation_numbers = {}
doc = 0
while doc<len(citations):
	docID,cite = citations[doc].split('\t')
	cites = []
	while (doc<len(citations) and int(docID)==int(citations[doc].split('\t')[0])):
		dID,c_no= citations[doc].split('\t')
		try:
			cites.append(int(c_no))
		except:
			doc+=1
			continue
		if int(c_no) in bibliographic_couplings:
			bibliographic_couplings[int(c_no)].append(int(dID))
		else:
			bibliographic_couplings[int(c_no)] = [int(dID)]
		doc += 1
	#random
	for cite_no in range(len(cites)-1):
		for cite_no2 in range(cite_no+1,len(cites)):
			if int(cites[cite_no]) in cocitation_numbers:
				if int(cites[cite_no2]) in cocitation_numbers[int(cites[cite_no])]:
					cocitation_numbers[int(cites[cite_no])][int(cites[cite_no2])] += 1
				else:
					cocitation_numbers[int(cites[cite_no])][int(cites[cite_no2])] = 1
			else:
				cocitation_numbers[int(cites[cite_no])] = {}
				cocitation_numbers[int(cites[cite_no])][int(cites[cite_no2])] = 1
			if int(cites[cite_no2]) in cocitation_numbers:
				if int(cites[cite_no]) in cocitation_numbers[int(cites[cite_no2])]:
					cocitation_numbers[int(cites[cite_no2])][int(cites[cite_no])] += 1
				else:
					cocitation_numbers[int(cites[cite_no2])][int(cites[cite_no])] = 1
			else:
				cocitation_numbers[int(cites[cite_no2])] = {}
				cocitation_numbers[int(cites[cite_no2])][int(cites[cite_no])] = 1


bibliographic_numbers = {}
for doc in bibliographic_couplings:
	b_couples = bibliographic_couplings[doc]
	for bc_ID in range(len(b_couples)-1):
		for bc_ID2 in range(bc_ID,len(b_couples)):
			if int(b_couples[bc_ID]) in bibliographic_numbers:
				if int(b_couples[bc_ID2]) in bibliographic_numbers[int(b_couples[bc_ID])]:
					bibliographic_numbers[int(b_couples[bc_ID])][int(b_couples[bc_ID2])] += 1
				else:
					bibliographic_numbers[int(b_couples[bc_ID])][int(b_couples[bc_ID2])] = 1
			else:
				bibliographic_numbers[int(b_couples[bc_ID])] = {}
				bibliographic_numbers[int(b_couples[bc_ID])][int(b_couples[bc_ID2])] = 1
	