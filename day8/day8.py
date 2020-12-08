with open("day8.txt","r") as file:
  lines = file.readlines()

def parse_list(lines: list):
  instructions = list()
  for line in lines:
    line = line.replace("\n","").split(" ")
    instructions.append((line[0],int(line[1])))
  return instructions
def checker(instructions: list):
  acc = 0
  indexer = 0
  base = list()
  process = 0
  outs = False
  while True:
    try:
      ins = instructions[indexer]
    except IndexError:
      outs = True
      break
    l  = len(base)
    breaker = 0
    if l > 6:
      try:
        for c, el in enumerate(base):
          if not c == l-3:
            if el == base[l-3]:
              if base[c + 1] == base[l-2]:
                if base[c + 2] == base[l-1]:
                  l_c = [el,base[c + 1],base[c+2]]
                  breaker = 1
                  break
      except IndexError:
        pass
    if breaker == 1:
      for val in l_c:
        if val[0] == "acc":
          acc -= val[1]
      break
    if ins[0] == "nop":
      indexer += 1
    elif ins[0] == "jmp":
      indexer += ins[1]
    elif ins[0] == "acc":
      acc += ins[1]
      indexer += 1
    else:
      raise ValueError("FML")
    base.append(ins)
    process += 1
  return [acc,outs]

print(checker(parse_list(lines)))

answers = list()
for i,line in enumerate(lines):
  clone = lines.copy()
  f = line
  if "nop" in line:
    f = f.replace("nop","jmp")
  elif "jmp" in line:
    f = f.replace("jmp","nop")
  else:
    f = line
  clone[i] = f
  out = checker(parse_list(clone))
  if out[1]:
    print(out)
    break
  else:
    answers.append((out,clone))
