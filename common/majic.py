class User:
    table_name='user'  #类属性
    def __init__(self):
        self.username='xiaohong', #实例变量
        self.password='123456',
        self.email='hym@123.com'

    def method(self,value):
        print('hello %s'%value)

if __name__ == '__main__':
    print(User.__dict__) #通过类名可以获取到类的属性和方法
    user=User() #实例化User类
    print(user.__class__)  #通过实例可以获取到对应的类
    for k,v in User.__dict__.items():
        if not k.startswith('__'):
            print(k,':',v)

    print(user.__dict__)  #获取实例变量或属性
    # user.nickname='hhh'
    # print(user.__dict__)
    user.__setattr__('nickname','jjj')
    print(user.__dict__)

    setattr(user,'nickname2','ttt')
    print(user.__dict__)


    print(user.__getattribute__('method'))
    user.__getattribute__('method')('chengdu')

    getattr(user,'method')('dd')