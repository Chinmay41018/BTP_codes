class paper:
	def __init__(self,paper_no,paper_title):
		self.number = paper_no
		self.title = paper_title
		self.a_list = []
		self.year = None
	def add(self, node):
		self.a_list.append(node)
	def add_year(year):
		self.year = year
class author:
	def __init__(self,a_no,a_name,p_number):
		self.name = a_name
		self.number = a_no
		self.paper = [p_number]
	def add_paper(p_num):
		self.paper.append(p_num)

with open('paper_title','r') as myfile:
	titles = myfile.read().splitlines()
with open('paper_authors','r') as myfile:
	authors = myfile.read().splitlines()
nodes = []
indices = []
for title in titles:
	a,b = title.split('\t')
	nodes.append(paper(int(a),b))
	indices.append(int(a))

a_indices = []
p_length = len(nodes)
i = 0
for line in authors[:50000]:
	a,b = line.split('\t')
	c,d = b.split('[')
	d = d[:-1]
	node = indices.index(int(a))
	nodes[node].add(c)
	try:
		present = p_length + a_indices.index(c)
		nodes[present].add_paper(int(a))
	except:
		a_indices.append(c)
		nodes.append(author(int(d),c,int(a)))
	# asdsa
	i+=1
	

for node in nodes:
	try:
		if len(node.paper)>1:
			print node.name
	except:
		pass 