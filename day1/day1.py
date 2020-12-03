
def summer_two():
  for val in (v := [int(val) for val in open("day1.txt","r").readlines()]):
    for subval in v:
      if val + subval == 2020:
        return f"Val: {val}\nSubVal: {subval}\nMultiplies: {val * subval}"


def summer_three():
  for val in (v := [int(val) for val in open("day1.txt","r").readlines()]):
    for subval in v:
      for thirdval in v:
        if val + subval + thirdval == 2020:
          return f"Val: {val}\nSubVal: {subval}\nthirdval: {thirdval}\nMultiplies: {val * subval * thirdval}"

print(summer_two())
print(summer_three())
