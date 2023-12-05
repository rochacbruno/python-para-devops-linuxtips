result = 0
while True:
    try:
        result += sum(map(int, [input(), input(), input()]))
    except EOFError:
        break 
    

print(result)
    