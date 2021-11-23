with open("day14sample.txt") as f:
    txt = f.readlines()

def binarytodenary(n):
    x = len(n)
    i = 0
    t = 0
    tf = 0
    m = (x - 1)
    while i < x:
        c = n[i]
        c = int(c)
        t = c*(2**m)
        m -= 1
        tf = tf + t
        i += 1
    return tf
def denarytobinary(d2):
    r = 0
    e = 0
    x = []
    base = ""
    while d2 != 0:
        r = int(d2%2)
        e = int(d2/2)
        x.append(r)
        d2 = int(e)
    for i in list(reversed(x)):
        base += str(i)
    return base
def apply_mask_part_a(mask,adder):
  base = ""
  bi = denarytobinary(adder)
  bi = (36 - len(bi)) * "0" + bi
  for i in range(0,36):
    if mask[i] == "X":
      base += bi[i]
    else:
      base += mask[i]
  return binarytodenary(base)

def apply_mask_part_b(mask,loc):
  base = ""
  bi = denarytobinary(loc)
  bi = (36 - len(bi)) * "0" + bi
  for i in range(0,36):
    if mask[i] == "X":
      base += "X"
    elif mask[i] == "0":
      base += bi[i]
    else:
      base += mask[i]
  ini = [""]
  for char in base:
    if char == "0" or char == "1":
      ini = [item + char for item in ini]
    else:
      la = [item + "1" for item in ini]
      lb = [item + "0" for item in ini]
      ini = la + lb
  return [binarytodenary(base) for base in ini]

def part_a():
  mem = {}
  mask = None
  for line in txt:
    if line.startswith("mask = "):
      mask = line.replace("mask = ","")
    else:
      adder = int(line.split(" = ")[1])
      loc = line.split(" = ")[0].replace("mem[","").replace("]","")
      mem[loc] = apply_mask_part_a(mask,adder)

  print(sum(mem.values()))

def part_b():
  mem = {}
  mask = None
  for line in txt:
    if line.startswith("mask = "):
      mask = line.replace("mask = ","")
    else:
      add_num = int(line.split(" = ")[1])
      location = line.split(" = ")[0].replace("mem[","").replace("]","")
      for out in apply_mask_part_b(mask,int(location)):
        mem[out] = add_num
  print(mem)
  print(sum(mem.values()))


part_a()
part_b()