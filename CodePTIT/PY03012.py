numTest=int(input())
list=[]
for i in range(numTest):
    student={}
    student['name']=input()
    c,t=[int(x) for x in input().split()]
    student['lamdung']=c
    student['submit']=t
    # print(student)
    list.append(student)


list.sort(key=lambda x:(-1*x['lamdung'],x['submit'],x['name']))
for student in list:
    print(student['name'],student['lamdung'],student['submit'])