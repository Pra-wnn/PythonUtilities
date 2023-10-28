import re

with open('QWM+3.txt','r') as rfile:
    # rfile.read()
    for line in rfile:
        # print(line)
        if line == "11":    #doens't work cuase of one extra space
            print("True")
        pattern = re.compile(r"11") #regex 
        matches = pattern.finditer(line)
        for match in matches:
            print(match)
