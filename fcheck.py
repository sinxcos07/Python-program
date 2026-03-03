import pandas as pd
a={'c':[122,332],'c2':[344,666]}
p1=pd.DataFrame(a)
b={'c':[887,324],'c2':[554,311]}
p2=pd.DataFrame(b)
p3=pd.concat([p1,p2],ignore_index=False,sort=False)
print(p3)