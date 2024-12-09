D_sales=(100,121,120,130,140,120,122,123,190,125)
count=0
for i in range(1,len(D_sales)):
    if D_sales[i]<D_sales[i-1]:
        count+=1
print(f"Number of sale decrease during {len(D_sales)} days compared to previous date is {count} days")