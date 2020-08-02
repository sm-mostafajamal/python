def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans/1000
    crates = jars/100
    return jelly_beans, jars, crates

start_point = 10000
beans, jars, crates = secret_formula(start_point) # inside the fuction variables are temporary 

#remenber that this is anothr way to format a string
print("with a starting point of: {}".format(start_point))
# it's just  like with an f"" string
print(f"we'd have {beans} beans, {jars} jars, and {crates}crates.")

start_point = start_point/10

print("we can also do that this way:")
formula = secret_formula(start_point)
# this is an easy way to apply a list to a format string
print("we'd have {} beans, {} jars, and {}crates.".format(*formula)) # *formula use to print all result on paranthesis
