# Title: Krypton1 Solution
# Author: Timothy J.C. Low
# Date: 2/21/2023

encoded= "YRIRY GJB CNFFJBEQ EBGGRA"

i = 0
temp_str = ""
while i < 26:
    encoded = encoded.split()
    for j in encoded:
        for k in j:
            temp = ord(k) + 1
            if (temp > 90):
                temp = 65
            temp_str += chr(temp)
        temp_str += " "
    print(temp_str)
    encoded = temp_str
    temp_str = ""
    i += 1
