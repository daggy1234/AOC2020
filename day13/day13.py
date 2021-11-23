lines = open("day13sample2.txt","r").readlines()
from functools import reduce

def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod
 
 
 
def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1
  
def part_a():
  timor = int(lines[0])
  splitted = [int(char) for char in lines[1].split(",") if char != "x"]
  ans = list()
  for l in splitted:
    inj = timor // l
    if inj * l > timor:
      ans.append((l,inj*l))
    else:
      ans.append((l,(inj+1)*l))
  smol = 99999999999999
  answer = (0,0)
  mi = min([val[1] for val in ans])
  for val in ans:
    if val[1] == mi:
      answer = val
  print(answer[0] * (answer[1] - timor))

def part_b():
  splitted = [int(char) for char in lines[0].split(",") if char != "x"]
  print(splitted)


part_b()

