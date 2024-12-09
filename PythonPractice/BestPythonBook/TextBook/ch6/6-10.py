tyo=(1,2,5,4,3,2,1,4,7,8,9,9,3,7,3)
tyo_s=set(tyo)
tyo_l=list(tyo)
idc={}
for num in tyo_s:
    l=tyo_l.count(num)
    idc[num]=l

max_v=max(idc.values())
