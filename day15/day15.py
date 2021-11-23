import functools
import time

def timer(function):
    @functools.wraps(function)
    def wrapper(*args, **kwargs) -> float:
        time_list = []
        ans = None
        for i in range(0, 10):
            start = time.perf_counter()
            ans = function(*args, **kwargs)
            end = time.perf_counter()
            time_list.append(end - start)
            i += 0
        return [round((sum(time_list) / len(time_list)) * 1000, 2),ans]
    return wrapper

def sol_a(input: list,num: int):
    
    m = num
    last =input[len(input)-1]
    turns =  dict()
    for i, val in enumerate(input):
        turns[str(i)]= val


    def get_turn_diff(val) -> int:
        rev = [val for val in val["data"].values()][::-1]
        ans = []
        for i,ansa in enumerate(rev):
            if ansa == val["val"]:
                ans.append(len(rev)-i)
            if len(ans) == 2:
                break
        return ans[0] - ans[1]

    for i in range(len(input),m):
        prev = last
        cc = [val for val in turns.values()].count(prev)
        if 1 == cc:
            turns[str(i)] = 0
            last = 0
        else:
            dtp = {"val": prev, "data": turns}
            out = get_turn_diff(dtp)
            turns[str(i)] = out
            last = out
    return turns[str(m-1)]

@timer
def sol_b(input: list,times: int):
    indexer = dict()
    last = input[len(input)-1]

    def set_index(n,d):
        try:
            indexer[n]["count"] += 1
            indexer[n]["index"].append(d)
        except KeyError:
            indexer[n] = {"index": [d], "count": 1}
    
    for i,val in enumerate(input):
        try:
            l = indexer[str(val)]
            continue
        except KeyError:
            indexer[str(val)] = {"index": [i], "count": 1}
    
   
    for i in range(len(input),times):
        try:
            if indexer[str(last)]["count"] == 1:
                set_index(str(0),i)
                last = 0
            else:
                indexes = indexer[str(last)]["index"][::-1]
                last  = indexes[0] - indexes[1]
                set_index(str(last),i)
        except KeyError:
            set_index(str(last),i)
        #print(indexer)
    return last

def sol_c(input: list,times: int):
    indexer = dict()
    last = input[len(input)-1]

    def set_index(n,d):
        try:
           indexer[n] = (indexer[n][1],d)
        except KeyError:
            indexer[n] = (None,d)
    
    for i,val in enumerate(input):
        indexer[str(val)] = (None,i)
    
   
    for i in range(len(input),times):
        try:
            if indexer[str(last)][0] == None:
                set_index(str(0),i)
                last = 0
            else:
                indexes = indexer[str(last)]
                last  = indexes[1] - indexes[0]
                set_index(str(last),i)
        except KeyError:
            set_index(str(last),i)
        #print(indexer)
    return last
    
input = [0, 13, 1, 8, 6, 15]
print(f"Sol A: {sol_a(input, 2020)[0]}ms")
print(f"Sol B: {sol_b(input, 2020)[0]}ms")
print(f"Sol A: {sol_c(input, 2020)[0]}ms")
print(f"2020 answer: {sol_c(input,2020)[1]}")
print(f"2020 answer: {sol_c(input,30000000)[1]}")


