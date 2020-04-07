import pandas as pd
data = {
    'state':['ohio','ohio','ohio','nevada','nevada'],
    'year':[2000,2001,2002,2003,2004],
    'pop':[1.1,1.3,2.5,4.2,5]
    }
fram = pd.DataFrame(data)
# print(fram.head(3))
frame2 = pd.DataFrame(data,index=['one','two','three','four','five'],columns=['year','state','pop','debt'])
print(frame2.columns)

