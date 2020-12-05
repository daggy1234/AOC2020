res = open("day4.txt","r").readlines()
base = list()
some = list()
for i in range(0,len(res) + 2,1):
  try:
    #print(repr(res[i + 1]) == repr('\n'))
    if repr(res[i + 1]) == repr('\n'):
      base.append(res[i])
      some.append(base)
      base = list()
      i += 1
    else:
      base.append(res[i])
  except IndexError:
    some.append(base)

# c = 1
# for sub in some:
#   st = "".join(sub)
#   if ("byr:" in st) and ("iyr:" in st) and ("eyr:" in st) and ("hgt:" in st) and ("hcl:" in st) and ("ecl:" in st) and ("pid:" in st):
#     c += 1
#   else:
#     pass
# print(c)


def hcl(s):
  try:
    r = s.split("#")[1]
    if len(r) == 6:
      try:
        int(r,16)
        return True
      except Exception:
        return False
    else:
      return False
  except IndexError:
    return False

def pid(st):
  if len(st) == 9:
    try:
      int(st)
      return True
    except Exception as e:
      return False
  return False

def hgt(st):
  if st[-2:] == "cm":
    return 150 <= int(st[:-2]) <= 193
  elif st[-2:] == "in":
    return 59 <= int(st[:-2]) <= 76
  else:
    return False

correct = 1
for sub in some:
  st = "".join(sub)
  mylist = [l.split(":", 1) for l in st.split()]
  fic = {k: v for k, v in mylist}
  #print(pid(fic["pid"]))
  try:
    if (2020 <= int(fic["eyr"]) <= 2030) and (1920 <= int(fic["byr"]) <= 2002) and (2010 <= int(fic["iyr"]) <= 2020) and hcl(fic["hcl"]) and pid(fic["pid"]) and ((fic["ecl"] in ["amb","blu", "brn", "gry" ,"grn", "hzl", "oth"])) and hgt(fic["hgt"]):
      correct += 1
  except KeyError:
    pass
print(correct)
  #if repr(res[i + 1]) == "\n":
  #  print("bl")