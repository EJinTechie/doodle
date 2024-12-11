alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm']
c_alpha1=alpha[1:-1]
c_alpha2=alpha[::-1]
c_alpha3=alpha[::3]
c_alpha4=alpha[-1::-3]
c_alpha5=alpha[2::3]
c_alpha6=alpha[-5::-3]

print(c_alpha1)
print(c_alpha2)
print(c_alpha3)
print(c_alpha4)
print(c_alpha5)
print(c_alpha6)

s_alpha1=''.join(c_alpha1)
s_alpha2=''.join(c_alpha2)
s_alpha3=''.join(c_alpha3)
s_alpha4=''.join(c_alpha4)
s_alpha5=''.join(c_alpha5)
s_alpha6=''.join(c_alpha6)

print(s_alpha1)
print(s_alpha2)
print(s_alpha3)
print(s_alpha4)
print(s_alpha5)
print(s_alpha6)
