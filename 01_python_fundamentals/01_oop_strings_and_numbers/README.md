# Python — объектная модель, type, object и метаклассы

## 1. Всё в Python является объектом

В Python числа, строки, функции, классы и даже сами метаклассы являются объектами.

Каждый объект обладает тремя основными характеристиками:

- **Identity (идентичность)** — уникальная идентичность объекта, которую можно исследовать через `id()`.
- **Type (тип)** — определяет допустимые операции и поведение объекта.
- **Value (значение)** — данные, которые представляет объект.

```python
a = 10
b = "Python"

print(type(a))  # <class 'int'>
print(type(b))  # <class 'str'>
```

Переменная в Python — это имя, связанное с объектом. При присваивании нового значения имя может начать ссылаться на другой объект.

```python
a = 10
a = "Python"

print(type(a))  # <class 'str'>
```

Тип объекта `10` не изменился. Изменилась привязка имени `a`.

---

## 2. Что такое `type()`?

При вызове с одним аргументом `type(obj)` возвращает **сам объект класса**, которому принадлежит объект `obj`.

Он не возвращает строку.

```python
a = 10

result = type(a)

print(result)         # <class 'int'>
print(result is int)  # True
```

`result` и `int` ссылаются на один и тот же объект класса.

Вывод `<class 'int'>` — это текстовое представление класса.

Сравнение:

```python
a = 10

type(a)           # Объект класса int
type(a).__name__  # Строка 'int'
repr(type(a))     # Строка "<class 'int'>"
```

Проверка:

```python
print(type(type(a)))          # <class 'type'>
print(type(type(a).__name__)) # <class 'str'>
```

**Вывод:** `type()` возвращает класс как объект, поэтому результат можно передавать в функции, сравнивать и использовать для создания экземпляров.

---

## 3. Классы сами являются объектами

Рассмотрим:

```python
class User:
    pass

user = User()
```

Здесь:

- `user` — экземпляр класса `User`.
- `User` — сам объект класса.
- `type` — метакласс, экземпляром которого является `User`.

```python
print(type(user))  # <class '__main__.User'>
print(type(User))  # <class 'type'>
```

Цепочка:

```text
user
 │ type(user)
 ▼
User
 │ type(User)
 ▼
type
```

Это справедливо и для встроенных классов:

```python
print(type(int))   # <class 'type'>
print(type(str))   # <class 'type'>
print(type(list))  # <class 'type'>
```

Важно: `type` — метакласс по умолчанию. Пользовательские классы могут иметь собственные метаклассы, наследующиеся от `type`.

---

## 4. Что такое `object`?

`object` — корневой базовый класс стандартной иерархии классов Python.

Если при объявлении класса не указан родитель, он обычно наследуется непосредственно от `object`.

```python
class User:
    pass

print(User.__bases__)
# (<class 'object'>,)
```

Это эквивалентно:

```python
class User(object):
    pass
```

У встроенных классов тоже есть связь с `object`:

```python
print(int.__bases__)
# (<class 'object'>,)

print(issubclass(int, object))
# True
```

Отсюда:

```python
user = User()

print(isinstance(user, object))  # True
print(isinstance(10, object))    # True
```

`isinstance()` учитывает наследование. Поэтому объект может быть экземпляром `object`, хотя его непосредственный тип — `User` или `int`.

---

## 5. Разница между `object` и `type`

Эти классы выполняют разные роли.

**`object`** — основа наследования классов.

**`type`** — метакласс, используемый по умолчанию для создания объектов классов.

Между ними существуют две связи:

```python
print(issubclass(type, object))  # True
print(type(object))              # <class 'type'>
```

Это означает:

1. `type` наследуется от `object`.
2. `object` является экземпляром `type`.

Также:

```python
print(type(type))  # <class 'type'>
```

Метакласс `type` является экземпляром самого себя. Это специальная особенность объектной модели Python.

**Наследование и принадлежность к типу — разные отношения.**

---

## 6. Разница между `type()`, `isinstance()` и `issubclass()`

### `type(obj)`

Возвращает непосредственный тип объекта.

```python
class Animal:
    pass

class Dog(Animal):
    pass

dog = Dog()

print(type(dog) is Dog)     # True
print(type(dog) is Animal)  # False
```

### `isinstance(obj, cls)`

Проверяет, является ли объект экземпляром класса или его подкласса.

```python
print(isinstance(dog, Dog))     # True
print(isinstance(dog, Animal))  # True
print(isinstance(dog, object))  # True
print(isinstance(dog, type))    # False
```

### `issubclass(A, B)`

Проверяет, является ли класс `A` подклассом `B`, включая случай, когда `A` и `B` — один класс.

```python
print(issubclass(Dog, Animal))   # True
print(issubclass(Dog, object))   # True
print(issubclass(Animal, Dog))   # False
print(issubclass(Dog, Dog))      # True
```

**Главное отличие:** `type()` сообщает непосредственный класс, а `isinstance()` учитывает наследование.

---

## 7. Почему функции тоже являются объектами?

Когда Python выполняет `def`, он создаёт объект функции и связывает его с указанным именем.

```python
def analyze_operation(a, b, operator):
    return a + b
```

Проверим:

```python
print(type(analyze_operation))
# <class 'function'>
```

У функций существует собственный класс `function`.

Его можно получить через модуль `types`:

```python
import types

print(isinstance(analyze_operation, types.FunctionType))
# True
```

Но:

```python
print(isinstance(analyze_operation, type))
# False
```

Почему?

Потому что `analyze_operation` — экземпляр `function`, а не `type`.

Теперь:

```python
print(isinstance(type(analyze_operation), type))
# True
```

Разбор:

1. `type(analyze_operation)` возвращает объект класса `function`.
2. Класс `function` является экземпляром метакласса `type`.
3. Поэтому `isinstance(..., type)` возвращает `True`.

Цепочка:

```text
analyze_operation
       │ type(...)
       ▼
    function
       │ type(...)
       ▼
      type
```

Аналогично:

```python
a = 10

print(isinstance(a, type))        # False
print(isinstance(type(a), type))  # True
```

Число `10` — экземпляр `int`, а сам класс `int` — экземпляр `type`.

---

## 8. Почему `isinstance(..., object)` часто возвращает True?

Рассмотрим:

```python
def foo():
    pass

class Bar:
    pass
```

```python
print(isinstance(foo, object))  # True
print(isinstance(Bar, object))  # True

print(isinstance(foo, type))    # False
print(isinstance(Bar, type))    # True
```

Объяснение:

- `foo` — экземпляр `function`, который наследуется от `object`.
- `Bar` — экземпляр `type`, который также наследуется от `object`.
- `foo` не является экземпляром `type`.
- `Bar` является экземпляром `type`.

Следовательно, **каждый обычный объект Python является экземпляром `object`, но не каждый объект является экземпляром `type`**.

---

## 9. Что такое `__name__`?

`__name__` — атрибут, содержащий имя функции или класса в виде строки.

```python
print(int.__name__)    # int
print(str.__name__)    # str
print(float.__name__)  # float
```

Для собственной функции:

```python
def foo():
    pass

print(foo.__name__)  # foo
```

Для собственного класса:

```python
class User:
    pass

print(User.__name__)  # User
```

Поэтому выражение:

```python
a = 10

print(type(a).__name__)  # int
```

выполняется последовательно:

1. `type(a)` возвращает объект класса `int`.
2. Python получает атрибут `__name__` у этого класса.
3. Возвращается строка `"int"`.

`__name__` — атрибут, поэтому круглые скобки для его вызова не нужны.

---

## 10. Почему `int.__name__` работает, хотя его нет в `int.__dict__`?

Проверим:

```python
print("__name__" in int.__dict__)   # False
print("__name__" in type.__dict__)  # True
```

Класс `int` является экземпляром `type`.

В метаклассе `type` определён специальный дескриптор `__name__`.

```python
print(type.__dict__["__name__"])
```

В CPython результат выглядит примерно так:

```text
<attribute '__name__' of 'type' objects>
```

При обращении:

```python
int.__name__
```

механизм поиска атрибутов класса использует дескриптор его метакласса `type`.

Поэтому `int.__name__` доступен, несмотря на отсутствие соответствующего ключа в `int.__dict__`.

Это пример работы дескрипторов и механизма поиска атрибутов.

---

## 11. Полезные специальные атрибуты

| Атрибут | Назначение |
|---|---|
| `__class__` | Класс объекта |
| `__name__` | Имя класса или функции |
| `__dict__` | Словарь атрибутов объекта, если поддерживается |
| `__bases__` | Непосредственные базовые классы |
| `__mro__` | Порядок разрешения методов при наследовании |
| `__module__` | Имя модуля, с которым связан класс или функция |

Пример:

```python
class User:
    pass

user = User()

print(user.__class__)
print(User.__class__)
print(User.__bases__)
print(User.__mro__)
print(User.__name__)
```

Важно: не каждый объект имеет собственный `__dict__`. Например, обычные экземпляры `int` его не имеют.

---

## 12. Итог

1. В Python числа, строки, функции и классы являются объектами.
2. Переменные — имена, ссылающиеся на объекты.
3. `type(obj)` возвращает сам объект класса, а не строку.
4. `object` — базовый класс стандартной иерархии наследования.
5. `type` — метакласс по умолчанию, экземплярами которого являются классы.
6. Классы являются объектами, но не все объекты являются классами.
7. Функции — экземпляры класса `function`.
8. `isinstance()` проверяет принадлежность к классу с учётом наследования.
9. `issubclass()` проверяет наследование между классами.
10. `__name__` позволяет получить имя класса или функции.
11. Атрибуты могут предоставляться не только самим классом, но и его метаклассом.
12. `type` наследуется от `object`, а `object` является экземпляром `type`.

**Основная мысль:** Python имеет единую объектную модель, в которой даже классы и функции являются полноценными объектами со своими типами, атрибутами и поведением.

