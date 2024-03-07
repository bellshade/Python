# DECORATORS CHAINING
# Mari kita coba buat rantai fungsi decorators

# ================================= #

# Buatlah fungsi decorators yang di inginkan
def add(func):
  def wrap():
    x = func()
    return x + x
  return wrap

def add_quadrat(func):
  def wrap():
    x = func()
    return x**2
  return wrap
  
# Cara menggunakan rantai decorators
@add
@add_quadrat
def num1():
  return 25

@add_quadrat
@add
def num2():
  return 25
  
print(num1())
print(num2())