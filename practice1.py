class Test(object):
    x_num = 4
    num = 1
    y = 5
    def __init__(self, num):
        self.num = num
    def change(self,num):
        Test.num = num
        Test.x_num = 21
    def test(self,x,y):
        self.x = 12
        self.y = 15
a = Test(11)
print 'Test.num =', Test.num             #   '这里指定了是类的成员'
print 'Test.y =', Test.y
print 'Test.x_num =', Test.x_num           #  '这里指定了是类的成员'
print 'a.num =' , a.num                    # '对象中有num成员'
print 'a.x_num =', a.x_num                  # '对象中没有x_num成员，但是类成员中有x_num'
print 'a.y =', a.y
a.test(8,9)
print 'test(),self.x = 12 -> a.x =', a.x                  # '非构造函数可以任意声明对象的成员'
print 'test(),self.y = 15 -> a.y =', a.y
a.change(6)
print 'a.change(6), Test.num=6 -> Test.num =', Test.num   # '因为change中使用了Test.num，所以类中所有值都变了'
print 'a.change(6), Test.x_num=21 -> a.x_num =', a.x_num  # '即使a已经创建了，改了Test.x_num, a的x_num是会变的'
a.x_num = 18
print 'a.x_num=10 -> Test.x_num =',Test.x_num            #'这里是直接调用的，相当于只改了当前对象的类成员值，其他的类成员值不会改'
print 'a.x_num=12 -> Test().x_num = ', Test(123).x_num
print a.__dict__

class Atem(object):
  def __init__(self,x,y):
    self.x = x
    self.y = y
  def add(self):
    return self.x + self.y
data=Atem(10,15)
t=data.add()
print "data=",t
