import datetime
t1 = datetime.datetime.now()
with open('paper_title','r') as myfile:
	titles = myfile.read().splitlines()
with open('paper_authors','r') as myfile:
	authors = myfile.read().splitlines()
paper_number = {}
paper_author = {}
author_number = {}
for title in titles:
	a,b = title.split('\t')
	paper_number[int(a)] = b
for a_list in authors:
	try:
		a,b = a_list.split('\t')
		c,d = b.split('[')
		d = d[:-1]
		author_number[int(d)]= c
		if int(a) in paper_author:
			paper_author[int(a)].append(int(d))
		else:
			paper_author[int(a)] = [int(d)]
	except:
		pass

t2 = datetime.datetime.now()
ind = list(author_number.values()).index('George Angelos Papadopoulos')
a_no = author_number.keys()[ind]
ans = []
for pap in paper_author:
	if a_no in paper_author[pap]:
		ans.append(pap)

for an in ans:
	print paper_number[an]

t3 = datetime.datetime.now()
print t3-t2
print t2-t1
