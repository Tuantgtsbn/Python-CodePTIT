import re

string_text=""
while True:
    try:

        string_tmp=input().strip()
        string_text+=" "+string_tmp
        string_text=string_text.strip()
    except Exception:
        break
list_lines=re.split("[.?!]",string_text)
# line_sentence=re.findall('^\w.*[0-9][.]',string_text)


# print(list_lines)
for j in list_lines:
    if(j!=""):
        j=j.strip()
        j=j[0].upper()+j[1:len(j)].lower()
        list_tmp=j.split()
        print(list_tmp[0],end="")
        for word in list_tmp[1:]:
            if word not in [',',':']:
                print("",word,end="")
            else:
                print(word,end="")
        print()

