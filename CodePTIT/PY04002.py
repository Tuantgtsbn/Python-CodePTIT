class Rectangle:
    def __init__(self,a,b,c):
        self.height=a
        self.weight=b
        self.color1=c
        pass
    def perimeter(self):
        return ((self.height+self.weight)*2)
    def area(self):
        return (self.height*self.weight)
    def color(self):
        return self.color1.title()
if __name__ == '__main__':
    arr = input().split()
    if int(arr[0])>0 and int(arr[1])>0:

        r = Rectangle(int(arr[0]), int(arr[1]), arr[2])
        print('{} {} {}'.format(r.perimeter(), r.area(), r.color()))
    else:
        print('INVALID')