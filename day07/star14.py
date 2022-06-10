class Node:
	def __init__(self, value, children, parents=None):
		self.value = value
		self.children = children
		if parents is None:
			self.parents = []
		else:
			self.parents = parents
		self.visited = False

	def __repr__(self):
		parents = [parent.value for parent in self.parents]
		return "Node({value}, parents={parents}, children={children}".format(value=self.value, parents=parents, children=self.children)

def parse_line(line):
	line = line.strip()
	parents, children_str = line.split(' bags contain ')
	if children_str.startswith('no'):
		return parents, []
	children_str = children_str.strip().rstrip('.')
	children_list = children_str.split(',')
	children = []
	for child in children_list:
		child = child.strip()
		num, adjective, noun, _ = child.split(' ')
		children.append([int(num), '{} {}'.format(adjective, noun)])
	return parents, children

def parse_rules(fname):
	node_dict = {}
	for line in open(fname):
		value, children = parse_line(line)
		n = Node(value, children)
		node_dict[value] = n

	for key, n in node_dict.items():
		for _, btype in n.children:
			try:
				n_child = node_dict[btype]
				n_child.parents.append(n)
			except KeyError:
				continue

	return node_dict

containers = set()
def find_containing_bags(node):
	for parent in node.parents:
		containers.add(parent.value)
		find_containing_bags(parent)

def find_contained_bags(btype, node_dict):
	count = 1
	for num, child in node_dict[btype].children:
		count += num*find_contained_bags(child, node_dict)
	return count

node_dict = parse_rules('input.txt')
n = node_dict['shiny gold']
find_containing_bags(n)
print("containing bags = ", len(containers))

print("contained bags = ", find_contained_bags('shiny gold', node_dict) - 1)