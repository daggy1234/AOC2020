nums = [int(num) for num in open("day9.txt","r").readlines()]
preamble = 25
errors = list()
for i,num in enumerate(nums):
  if (i+1) - preamble > 0:
    spliced = nums[(i-preamble):i]
    base = list()
    for j,v in enumerate(spliced):
      copied = spliced.copy()
      copied.pop(j)
      summed = [val + v for val in copied]
      base += summed
    if not num in base:
      errors.append(num)
enum = errors[0]
for i,v in enumerate(nums):
  spliec = nums[i:]
  breaker = 0
  summer = 0
  numa = list()
  for val in spliec:
    summer += val
    if summer == enum:
      numa.append(val)
      breaker = 1
      break
    numa.append(val)
  if breaker == 1:
    break
print(min(numa) + max(numa))