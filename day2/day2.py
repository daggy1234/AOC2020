import re

def pword_check():
  correct = []
  for val in (v := [val for val in open("day2.txt","r").readlines()]):
    split_list = val.split(":")
    split_range = split_list[0].split(" ")
    search = split_list[1].replace(" ","").replace("\n","")
    char = split_range[1]
    start = int(split_range[0].split("-")[0])
    end = int(split_range[0].split("-")[1])
    vi =  len(re.findall(char, search))
    #print(f"Query:{search}\nCharacter:{char}\nStart:{start}\nEnd:{end}#\nMatches:{vi}")
    #print(start <= vi <= end)
    if start <= vi <= end:
      correct.append(search)
  print(len(correct))

def correct_pword_check():
  correct = []
  for val in (v := [val for val in open("day2.txt","r").readlines()]):
    split_list = val.split(":")
    split_range = split_list[0].split(" ")
    search = split_list[1].replace(" ","").replace("\n","")
    char = split_range[1]
    index_one = int(split_range[0].split("-")[0])
    index_two = int(split_range[0].split("-")[1])
    if search[index_one - 1] == char and search[index_two - 1] != char:
      correct.append(search)
    elif search[index_one - 1] != char and search[index_two - 1] == char:
      correct.append(search)
    else:
      pass
  print(len(correct))

pword_check()
correct_pword_check()
