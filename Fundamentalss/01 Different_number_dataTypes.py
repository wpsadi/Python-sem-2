a = 5
print(a, "is of type", type(a))

a = 2.0
print(a, "is of type", type(a))

a = 1+2j
print(a.real) # gives output in float
print(a.imag) # gives output in float
print(a, "is complex number?", isinstance(1+2j,complex))