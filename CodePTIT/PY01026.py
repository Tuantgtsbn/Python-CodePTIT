numTest=int(input())
def check(str1,str2):
    ls1=sorted([str(i) for i in str1])
    ls2=sorted([str(i) for i in str2])
    if(ls1==ls2):
        return "YES"
    else:
        return "NO"
        
for i in range(numTest):
    string_1=input()
    string_2=input()
    print("Test {}: {}".format(i+1,check(string_1,string_2)))