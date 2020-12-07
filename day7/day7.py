import re
base = dict()
for val in (v := [val for val in open("day7.txt","r").readlines()]):
  spli = (val.split("contain"))
  spli_items = spli[1].strip().replace("\n","").replace(".","").replace("bags","bag").split(",")
  key = spli[0].strip().replace("bags","bag")
  new = dict()
  for i in spli_items:
    if i.strip()[:2] == "no":
      pass
    else:
      num = int(i.strip()[:2])
      new[i.strip()[2:]] = num
  base[key] = new


def bcheck(x):
  if x == "shiny gold bag":
    return True
  for bags in base[x]:
    if bcheck(bags):
      return True
  return False



def counter_f(x):
  c = 1
  for item, num in base[x].items():
    c += (num * counter_f(item)) 
  return c


counter = 0
sum_count = 0
for key in base.keys():
  if bcheck(key):
    counter += 1
print(counter - 1)
print(counter_f("shiny gold bag") - 1 )