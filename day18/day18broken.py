import re

def meth(st: str) -> int:
    out = 0
    #print(f"Got : {repr(st)}")
    st = st.replace(")","").replace("+"," +").replace("*"," *").replace("  "," ")
    l = st.split(" ")
    if len(l) == 3:
      return eval(st)
    #print(l)
    cop = l.copy()
    for i,v in enumerate(l):
        if l[len(cop)-1] != cop[len(cop)-1]:
            break
        if len(l) == 3:
            print(l)
            out = eval("".join([str(item) for item in l]))
            break
        if v == "+":
            l[i+1] = (int(l[i-1]) + int(l[i+1]))
        elif v == "*":
            l[i+1] = (int(l[i-1]) * int(l[i+1]))
        else:
            continue
    #print(l[len(cop)-1])
    return l[len(cop)-1]

def bracket_sex(st: str) -> str:
    #print(10*"=")
    clone_s = st
    stt = st
    #print(f"OG {repr(st)}")
    for inds,char in enumerate(st):
        if char == "(":
            pst = st[:(inds)]
            st = st[inds:]
            break
    #print(f"St A: {st}")
    for ind, char in enumerate(stt):
        if char == ")":
            
            st = clone_s[inds+1:(ind+1)]
            
            cst = clone_s[(ind+2):]
            break
    #print(f"Pre: {pst}")
    #print(f"St B: {st}")
    #print(f"Suff {cst}")
    if "(" in st and ")" in st:
        st  = bracket_sex(st)
    if "(" in pst and ")" in pst:
        pst  = bracket_sex(pst)
    if "(" in cst and ")" in cst:
        cst  = bracket_sex(cst)
    outa = meth(st)
    final = pst + str(outa) + cst
    #print(final)
    return final

summer = 0
ls = list()
for line in open("day17.txt","r").readlines():
  try:
    line = line.replace("\n","")
    if ("(" in line) and ("(" in line):
      summer += meth(bracket_sex(line))
    else:
      summer += meth(line)
  except ValueError:
    ls.append(line)
print(summer)
#print(ls)
print("\n".join(ls))
