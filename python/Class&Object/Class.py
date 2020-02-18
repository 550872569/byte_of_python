'''
面向对象是一种抽象，是一种用分类的方式看待问题的方法，
用 Java 的编程思想来说就是：万物皆对象；
面向对象有三大特性：封装、继承、多态。

面向对象是一种用分类的方式看待问题的方法，
一个分类就是一个类，可以把类看作是一个抽象的模板，如：Car 类

对象是根据类创建出来的一个个实例。

'''

# 类的定义
class Car:
    # 定义 Car 类的属性 name
    name: ''
    speed: ''
    def __init__(self, name):
        self.name = name

    '''
    类方法（可调类变量、可被实例调用、可被类调用）
    1、类方法通过@classmethod装饰器实现，只能访问类变量，不能访问实例变量；
    2、通过cls参数传递当前类对象，不需要实例化。
    '''

    @classmethod
    def runClass(cls, speed):
        print('runClass', speed)

    '''
    静态方法（可调类变量、可被实例调用、可被类调用）
    1、用 @staticmethod 装饰的不带 self 参数的方法；
    2、静态方法名义上归类管理，实际中在静态方法中无法访问类和实例中的任何属性；
    3、调用时并不需要传递类或实例。
    '''
    @staticmethod
    def runStatic(name, street):
        print(name, 'runStatic in', street)

    '''
     实例方法（可调类变量、可调实例变量、可被实例调用）
     第一个参数强制为实例对象 self。
    '''
    def run(self, speed):
        print(self.name, speed, 'speed run in street everyWhere!')
    pass


# car = Car('bwm')
# Car.runClass('200km/h')
# Car.runStatic('1900', 'qinghuadonglu')
# car.run('200km/h')


# 类的继承 基本语法：class ClassName(BaseClassName)
class CarBMW(Car):
        def __init__(self):
            self.name = 'BMW'
            self.speed = '0-300km/h'

carBMW = CarBMW()
carBMW.run(carBMW.speed)


class CarBenChi(Car):
    def __init__(self):
        self.name = 'BenChi'
        self.speed = '0-200km/h'

carBC = CarBenChi()
carBC.run(carBC.speed)

