str = "this is string example....'wow'!!!"

prefix = str[1:5]
suffix = "wow!!!"
print (str.endswith(suffix))
print (str.endswith("!"))
print (str.endswith(suffix,20))
print (str.startswith(prefix))

suffix = "is"
print (str.endswith(suffix, 2, 4)) # 其中 2 是从 2 开始
print (str.endswith(suffix, 2, 6)) # 其中 6 是从 6 结束

str.find('k')# -1 不存在
str.find('t')# 0 存在
substr = "str"
print （str.find(substr, 10)# 其中 10 是从 10 结束
print (str.find(substr,3, ))# 其中 3 是从 3 开始
