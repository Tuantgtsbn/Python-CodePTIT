lines_1=input()
lines_2=input()
index=int(input())-1
part_1=lines_1[0:index]
part_2=lines_1[index:]
print(part_1+lines_2+part_2)