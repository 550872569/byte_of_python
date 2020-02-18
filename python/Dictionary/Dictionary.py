'''
class Mapping(_Collection[_KT], Generic[_KT, _VT_co]):
    # TODO: We wish the key type could also be covariant, but that doesn't work,
    # see discussion in https: //github.com/python/typing/pull/273.
    @abstractmethod
    def __getitem__(self, k: _KT) -> _VT_co:
        ...
    # Mixin methods
    @overload
    def get(self, k: _KT) -> Optional[_VT_co]: ...
    @overload
    def get(self, k: _KT, default: Union[_VT_co, _T]) -> Union[_VT_co, _T]: ...
    def items(self) -> AbstractSet[Tuple[_KT, _VT_co]]: ...
    def keys(self) -> AbstractSet[_KT]: ...
    def values(self) -> ValuesView[_VT_co]: ...
    def __contains__(self, o: object) -> bool: ...
'''

'''
Python 中的字典提供了一种灵活的访问和组织数据的方式
字典是由很多值组成的集合
字典的索引可以是不同的数据类型，同样也不止是整数，也有字符串
字典的索引被称为“键”，键及键所关联的值叫键值对（类似于Java中的Map集合）
字典是另一种可变容器模型，且可存储任意类型对象。
字典的每个键值 key=>value 对用冒号 : 分割，每个键值对之间用逗号 ,
 分割，整个字典包括在花括号 {} 中 ,格式如下所示：
dictionary  = {'url1':'baidu', 'url':'google', 'num1':12, 'num2':34};
'''
'''
# 访问字典数据
DictDog = {'size':'big','color':'white','character':'gentle'}

# 字典值通过[‘键’]来访问
print(DictDog['size'])

print('My Dog has '+DictDog['color']+' fur.' + ' and it has a ' + DictDog['character']+' character')

# change dict value for key
DictDog['size'] = 'litle'
print(DictDog)

del DictDog['size']
print(DictDog)

'''
# big
# My Dog has white fur. and it has a gentle character
# {'size': 'litle', 'color': 'white', 'character': 'gentle'}
# {'color': 'white', 'character': 'gentle'}
'''

# del DictDog
# DictDog.clear()
# {}

# 字典的函数
length = len(DictDog)
print(length)
str(DictDog)
print(DictDog)

print(type(DictDog))
# <class 'dict'>

# 即赋值会随父对象的修改而修改，拷贝不会随父对象的修改而修改
DictDogCopy = DictDog.copy()

DictDogMutableCopy = DictDogCopy
DictDogCopy['color'] = 'red'
print(DictDogCopy)
print(DictDog)
print(DictDogMutableCopy)
'''
# {'color': 'red', 'character': 'gentle'}
# {'color': 'white', 'character': 'gentle'}
# {'color': 'red', 'character': 'gentle'}

DictCar = {}
seqCar = ('name', 'color')
valueCar = ('BenChi', 'red')
DictCar = DictCar.fromkeys(seqCar)
print(DictCar)
DictCar = DictCar.fromkeys(seqCar, ('BenChi', 'red'))
DictCar['name'] = valueCar[0]
DictCar['color'] = valueCar[1]
print(DictCar)
# {'name': 'BenChi', 'color': 'red'}
print(DictCar.get('name'))
# BenChi

print(DictCar.get('age'))
# None

if 'Age' in DictCar:
    print('ture')
else:
    print('false')

print(DictCar.items())
# dict_items([('name', 'BenChi'), ('color', 'red')])
print(DictCar.keys())
# dict_keys(['name', 'color'])
print(DictCar.values())
# dict_values(['BenChi', 'red'])


'''
class MutableMapping(Mapping[_KT, _VT], Generic[_KT, _VT]):
    @abstractmethod
    def __setitem__(self, k: _KT, v: _VT) -> None: ...
    @abstractmethod
    def __delitem__(self, v: _KT) -> None: ...

    def clear(self) -> None: ...
    @overload
    def pop(self, k: _KT) -> _VT: ...
    @overload
    def pop(self, k: _KT, default: Union[_VT, _T] = ...) -> Union[_VT, _T]: ...
    def popitem(self) -> Tuple[_KT, _VT]: ...
    def setdefault(self, k: _KT, default: _VT = ...) -> _VT: ...
    # 'update' used to take a Union, but using overloading is better.
    # The second overloaded type here is a bit too general, because
    # Mapping[Tuple[_KT, _VT], W] is a subclass of Iterable[Tuple[_KT, _VT]],
    # but will always have the behavior of the first overloaded type
    # at runtime, leading to keys of a mix of types _KT and Tuple[_KT, _VT].
    # We don't currently have any way of forcing all Mappings to use
    # the first overload, but by using overloading rather than a Union,
    # mypy will commit to using the first overload when the argument is
    # known to be a Mapping with unknown type parameters, which is closer
    # to the behavior we want. See mypy issue  #1430.
    @overload
    def update(self, __m: Mapping[_KT, _VT], **kwargs: _VT) -> None: ...
    @overload
    def update(self, __m: Iterable[Tuple[_KT, _VT]], **kwargs: _VT) -> None: ...
    @overload
    def update(self, **kwargs: _VT) -> None: ...
'''
DictCarNew = {'name': 'BaoMa', 'color': 'Blue', 'age': '3', 'super': 'eric'}
DictCar.update(DictCarNew)
print(DictCar)
# {'name': 'BaoMa', 'color': 'Blue', 'age': '3', 'super': 'eric'}
print(DictCar.pop('age'))
# 3
print(DictCar)
# {'name': 'BaoMa', 'color': 'Blue', 'super': 'eric'}