import re
s=input()
numUpper=len(re.findall('[A-Z]',s))
numLower=len(re.findall('[a-z]',s))
# print(numLower,numUpper)
if(numUpper>numLower):
    print(s.upper())
else:
    print(s.lower())