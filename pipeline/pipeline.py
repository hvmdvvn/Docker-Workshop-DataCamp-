import sys
import pandas as pd

month = sys.argv[1]

df = pd.DataFrame({'day': [1, 2, 3], 'num_passengers': [10, 20, 30]})
df['month'] = month

df.to_parquet(f'passengers_{month}.parquet', index=False)