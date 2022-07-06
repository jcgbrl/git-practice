print("hello")

a = 3
print(a)

strv = "hello world"
print(strv)

b, c, d = 5, 6.5, "gab"  # declare multiple variable

print("{} {}".format("value is", c))

print("value is", c)

values = [1, 2, "gab"]  # list
print(values[2])
print(values[-1])

values.insert(3, "jc")  # insert
print(values)

values[2] = "gabriel"  # update
print(values)

del values[0]  # delete
print(values)
