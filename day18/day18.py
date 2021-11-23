
import re

def get_op(l):
    try:
      return l[-1]
    except IndexError:
      return None

def check_priority(op1, op2):
    precedences = {'+' : 1, '*' : 0}
    return precedences[op1] > precedences[op2]

suma = 0
for line in open("day17.txt","r").readlines():
  line = line.replace("\n","")
  parsed = re.findall("[+/*()-]|\d+", line)
  operators = []
  nums = []
  out = 0

  def evaluate():
    global nums,operators
    op = operators.pop()
    numb = nums.pop()
    numa = nums.pop()
    nums.append(eval(f"{numa}{op}{numb}"))
    
  for token in parsed:
    if token in "123456789":
      nums.append(int(token))
    elif token == "(":
      operators.append("(")
    elif token == ")":
      top = get_op(operators)
      while top != "(" and top != None:
          evaluate()
          top = get_op(operators)
      operators.pop()
    else:
      top = get_op(operators)
      while top and top not in "()" and check_priority(top,token):
        evaluate()
        top = get_op(operators)
      operators.append(token)
  while get_op(operators) != None:
    evaluate()
  suma += nums[0]
print(suma)