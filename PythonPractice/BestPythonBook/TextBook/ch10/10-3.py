persons=[('GilDong','Hong',27),('SunSin','Lee',46),('YuSin','Gim',34)]
k=sorted(persons, key=lambda x: x[2])
print(k)

persons=[('GilDong','Hong',27),('SunSin','Lee',46),('YuSin','Gim',34)]
k=sorted(persons, key=lambda x: x[1])
print(k)

persons=[('GilDong','Hong',27),('SunSin','Lee',46),('YuSin','Gim',34)]
k=sorted(persons, key=lambda x: x[2], reverse=True)
print(k)