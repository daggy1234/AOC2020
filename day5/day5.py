q_vec = [line for line in  open("day5.txt","r").readlines()]
seats = list()
for q in q_vec:
    rows = [0,127]
    row_term = q[:7]
    for char in row_term:
        by_t = int((rows[1] - rows[0]) / 2)
        if char == "F":
            rows = [rows[0],rows[0] + by_t]
        elif char == "B":
            rows = [rows[1] - by_t,rows[1]]
        else:
            print(char)
            raise ValueError("Bad")
    row = rows[0]

    columns = [0,7]
    c_term = slice(7,10)
    for char in q[c_term]:
        by_t = int((columns[1] - columns[0]) / 2)
        if char == "L":
            columns = [columns[0],columns[0] + by_t]
        elif char == "R":
            columns = [columns[1] - by_t,columns[1]]
        else:
            print(char)
            raise ValueError("Bad")
    column = columns[0]

    seat_id = row * 8 + column
    seats.append(seat_id)
ma = max(seats) + 1
mi = min(seats) - 1
print(f"Max: {ma}\nMin: {mi}")

mis = 0
for val in range(mi,ma):
    if val not in seats:
       mis = val

print(f"Missing: {mis}")