def hello():
    print('Hello，World')

hello_return = hello()
print(hello_return)

def hello(name): #其中 name 是变量
    return('Hello,'+ name)
john = 'Mike' #定义 john = ‘Mike’
hello_Mike = hello(john) #此处可以直接用 john 而不是 ‘john’
print(hello_Mike)
