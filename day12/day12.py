cords = []
for v in open("day12.txt","r").readlines():
  direction = v[0]
  num = int(v[1:])
  cords.append((direction,num))

def parse_dir(f,num):
  if f == "N":
    return (0,num)
  elif f == "S":
    return (0,-num)
  elif f == "E":
    return (num,0)
  elif f == "W":
    return (-num,0)
  else:
    raise ValueError("WTF")

def parse_degress(deg):
  if 0 > deg:
    deg = 360 + deg
  if deg > 360:
    deg = deg - 360
  if deg == 360:
    deg = 0
  return deg

def p1():
  deg = 0
  start = [0,0]
  for val in cords:
    if val[0] == "R" or val[0] == "L":
      if val[0] == "R":
        deg -= val[1]
      else:
        deg += val[1]
      deg = parse_degress(deg)
    elif val[0] == "F":
      if deg == 90:
        dir_char = "N"
      elif deg == 180:
        dir_char = "W"
      elif deg == 0:
        dir_char = "E"
      elif deg == 270:
        dir_char = "S"
      else:
        raise ValueError(deg)
      ret = parse_dir(dir_char,val[1])
      start[0] += ret[0]
      start[1] += ret[1]
    else:
        ret = parse_dir(val[0],val[1])
        start[0] += ret[0]
        start[1] += ret[1] 
  print(abs(start[1]) + abs(start[0]))

def p2():
  deg = 0
  boat = [0,0]
  start = [10,1]
  c = 0
  for val in cords:
    if val[0] == "R" or val[0] == "L":
      if val[0] == "R":
        deg = val[1]
      else:
        deg = 360 - val[1]
      if deg == 90:
        temp = start.copy()
        start[0] = temp[1]
        start[1] = -temp[0]
      elif deg == 180:
        start[0] = -start[0]
        start[1] = -start[1]
      elif deg == 270:
        temp = start.copy()
        start[0] = -temp[1]
        start[1] = temp[0]
      else:
        raise ValueError(val)
    elif val[0] == "F":
      multiplier = val[1]
      boat[0] += start[0] * multiplier
      boat[1] += start[1] * multiplier
    else:
        ret = parse_dir(val[0],val[1])
        start[0] += ret[0]
        start[1] += ret[1] 
    # print(f"Way: {start}")
    # print(f"boat: {boat}")
  print(abs(boat[1]) + abs(boat[0]))

p1()
p2()