def generatorFun():
    yield 1
    yield 2
    yield 3
  

x = generatorFun()
 
print(next(x))


