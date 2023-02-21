# krypton
## overthewire.org's Krypton wargame write up by Timothy J.C. Low

### Krypton1
This level requires us to use a rotations to discover the encrypted message. To preform a rotation, you must change each letter in the encoded message by the same increment across all letters. You have up to 26 unique versions of the encoded message using rotations, but in theory, only one rotation contains the decoded message.

We will preform a brute force approach, and test all 26 different rotations of the encoded message.

```
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
```
We find the following message:
LEVEL TWO PASSWORD ROTTEN

Thus giving us our decoded password to level 2.
