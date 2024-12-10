a_list=['a','b','c','d']
def to_upper(x):
    return x.upper()
fn=lambda x : x.upper()

upper_a_list=list(map(fn,a_list))
print(upper_a_list)

upper_a_list=[]
for i in a_list:
    upper_a_list.append(to_upper(i))
print(upper_a_list)

n_list=[10,20,30]
def twice(x):
    return 2*x
def triple(x):
    return 3*x

k=[]
y=[]
for i in n_list:
    k.append(twice(i))
    y.append(triple(i))
print(k)
print(y)