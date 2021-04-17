import numpy as np
import pandas as pd
df = pd.DataFrame(np.random.randint(0,100,size=(2000, 1000)))
df1 = pd.DataFrame(np.random.randint(0,100,size=(1000, 8)))
df.to_csv("matTestA.csv",index=False, header=False)
df1.to_csv("matTestB.csv",index=False, header=False)