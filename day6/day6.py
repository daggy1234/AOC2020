from itertools import islice

res = open("day6.txt","r").readlines()
base = list()
some = list()
for i in range(0,len(res) + 2,1):
  try:
    if repr(res[i + 1]) == repr('\n'):
      base.append(res[i])
      some.append(base)
      base = list()
      i += 1
    else:
      base.append(res[i])
  except IndexError:
    base.append(res[i])
    some.append(base)
    break

base = 0
for d in some:
#d = some[len(some)-1]
    el = "".join(d).replace(" ","").replace("\n","")
    counts = list()
    for char in el:
        if char not in counts:
            counts.append(char)
    base += len(counts)
print(f"Part 1: {base}")

b_t = 0
for d in some:
    s = 0
    el = "".join(d).replace(" ","")
    l = [e for e in el.split("\n") if e != ""]
    answers = [set([a for a in answer]) for answer in l]
    coms = len(set.intersection(*answers))
    b_t += coms
print(f"Part 2: {b_t}")