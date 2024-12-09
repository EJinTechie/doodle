tup1=[(),1,(),(),(1,),('a',),('a','b'),((),),('a','b'),'']

result = [x for x in tup1 if x!= ()]
result1=[y for y in result if y!='']
print(result)