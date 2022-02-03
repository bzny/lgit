from doctest import testfile
from pyexpat import native_encoding
from re import T
import re
from enum import Enum
from xml.etree.ElementTree import tostring
import logging
from functools import reduce

def log(func):
    def wrapper(*args,**kw):
        print('run %s' %func.__name__)
        return func(*args,**kw)
    return wrapper

def decrator(text):
    def log(func):
        def wrapper(*args,**kw):
            print(text,func.__name__)
            return func(*args,**kw)
        return wrapper
    return log
@decrator('excute')
def qqren():
    print('qqren vs Ayaka')


class kanmusu(object):
    def __init__(self, name, nationality, type, rarity):
        self.__name = name
        self.__nationality = nationality
        self.__type = type
        self.__rarity = rarity
    def get_nationality(self):
        return self.__nationality
    def set_nationality(self,a):
        self.__nationality = a
    def get_type(self):
        return self.__type
    def set_type(self,a):
        self.__type = a
    def get_rarity(self):
        return self.__rarity
    def set_rarity(self,a):
        self.__rarity = a
    def shoot(self,ammo='AP'):
        print('shooting %s !'  %ammo)

class lolikanmusu(kanmusu):
    def __init__(self, name, nationality, type, rarity,torpedo='533mm torpedo'):
        self.__name = name
        self.__nationality = nationality
        self.__type = type
        self.__rarity = rarity
        self.__torpedo=torpedo
    def torpedo_fire(self):
        print('%s fires a %s!' %(self.__name,self.__torpedo))
    
    def torpedo_salvo(self, amount=3):
       for n in range(amount):
           self.torpedo_fire()
       
shimakaze=lolikanmusu('shimakaze','J','destroyer','5','610mm torpedo')

shimakaze.shoot()
shimakaze.torpedo_fire()
shimakaze.torpedo_salvo(5)


class animal(object):
    def __init__(self,name):   #实例初始化，传入name属性，以_animal__name为变量名储存
        self.__name=name
    def run(self):
        print("%s is running" %self.__name)  #调用_animal__name进行输出

class cat(animal):
    def __init__(self, name):  #通过重写一遍__init__方法的方式初始化,此时name储存的名字是_cat__name，再调用父类的run方法就会出错
        self.__name=name
    def run(self):
        print("%s is running" %self.__name)

class dog(animal):
    def __init__(self, name):   #通过引用父类的__init__方法的方式初始化，此时name储存的名字和父类一样是_animal__name，可以直接使用父类的run方法，但是如果要自己再增加方法
        super().__init__(name)  #比如增加一个eat，则要写成"%s is running" %self._animal__name
    def eat(self):
        print('%s is eating' %self._animal__name)
a=cat('aa')

class Screen(object):
    @property
    def width(self):
        return self._width
    
    @width.setter
    def width(self,value):
        self._width=value
    
    @property
    def height(self):
        return self._height
    
    @height.setter
    def height(self,value):
        self._height=value
    
    @property
    def resolution(self):
        self._resolution=self._width*self._height
        return self._resolution

class xxfunc(object):
    def __init__(self):
        self.a,self.b=0,1
    
    def __iter__(self):
        return self
    
    def __next__(self):
        self.a=self.a + self.b
        self.b=self.a * self.b
        if self.a>100000:
            raise StopIteration
        return self.a
    
    def __getitem__(self,n):
        a,b=0,1
        for x in range(n):
            a=a+b
            b=a*b
        return a

for n in xxfunc():
    print(n)

class Chain(object):

    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path
    
    def __call__(self,path):
        return Chain('%s/:%s' % (self._path, path))


try:
    print(10/0)
    print(10/1)
except Exception as e:
    logging.exception(e)
finally:
    print('continuing')

nationality =Enum('nationality',('C','U','E','J','G','F','I','S','et'))
for name, member in nationality.__members__.items():
    print(name, '=>', member)

with open('testfile.txt','a') as f:
    f.write('\naqqqaaa')
