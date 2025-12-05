def dial(file):
    file_object = open(file, "r")
    curr = 50
    password = 0
    for line in file_object:
        # print(line.strip())
        rotate = line.strip()
        dir = rotate[0]
        steps = int(rotate[1:])
        if steps > 100:
            password += steps // 100
            steps = steps % 100
            
        # print(dir, steps)
        if dir == "L":
            if curr < steps:
                if curr != 0:
                    password += 1
                curr = curr - steps + 100
                
            else:
                curr = curr - steps
        elif dir == "R":
            curr = curr + steps
            if curr > 100:
                curr = curr - 100
                password += 1
        if curr == 100 or curr == 0:
            curr = 0
            password += 1
        print(rotate, curr, password)
        
    file_object.close()
    return password
    
file = "input.txt"
print(dial(file))
