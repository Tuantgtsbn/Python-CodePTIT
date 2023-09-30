class Rectangle:
    def __init__(self,a,b,c):
        self.height=a
        self.weight=b
        self.color=c
        pass
    def perimeter(self):
        return (self.height*)
if __name__ == '__main__':
    arr = input().split()
    r = Rectangle(int(arr[0]), int(arr[1]), arr[2])
    print('{} {} {}'.format(r.perimeter(), r.area(), r.color()))