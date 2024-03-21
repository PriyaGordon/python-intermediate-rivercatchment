# flag : bool =  "hi" \ gives type error """
# flag : bool = True

# def greet(name:str) -> None:
#     print("Hello"  + name )

# greet(" Priya ")
# greet(43)

# some_data : tuple[int, bool, str]

# def greetAll(names : list[str]) ->None:
#     for names in names:
#         greet(name)

# names = (42, True, "Manchester")

# x: dict[str, float]= {"field1":2.0, "field2":3}


# def myDiv(x : float, y : float) -> (float|None):
#     if y!=0: return x/y 
#     else:    return None

# myDict : dict[str, float|str] = {"temp": 273.0, "units":"Kelvin"}

# from typing import TYPE_CHECKING 

# if TYPE_CHECKING:
#     reveal_type(len)


from typing import Any, TypeVar, Callable

T = TypeVar("T")

def first(xs : list[T]) -> T:
    return xs[0]

example0= first([1,2,3,4])
reveal_type(example0)

S = TypeVar('S')
T = TypeVar('T')

def memo(f: Callable)