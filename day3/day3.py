res = open("day3.txt","r").readlines()
base = list()
for line in res:
  sub = list()
  line = line.replace("\n","")
  for i in range(200):
    for char in line:
      sub.append(char)
  base.append(sub)

def tree_counter(base, x_incr,y_incr):
  counter = x_incr
  trees = 0
  for i in range(y_incr,len(base),y_incr):
    row = base[i]
    char = row[counter]
    if char == '#':
      trees += 1
    counter  += x_incr
  return trees

print(tree_counter(base,3,1))

print(tree_counter(base,3,1)*  tree_counter(base,5,1) * tree_counter(base,1,2) * tree_counter(base,7,1) * tree_counter(base,1,1))