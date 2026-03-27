import pandas as pd
import numpy as np

data = {
    'Name': ['John Doe', 'Alice Smith', 'Bob Johnson', 'Clara Brown', 'Eva Green', 'Mike Taylor', 'Sophia White', 'Liam Black'],
    'Country': ['USA', 'FRA', 'ESP', 'GBR', 'USA', 'CAN', 'DEU', 'ITA'],
    'Code': ['US001', 'FR002', 'ES003', 'GB004', 'US001', 'CA006', 'DE007', 'IT008'],
    'ADR': [150, 200, 180, 250, 170, 190, np.nan, 220],
    'Stays in Week Nights': [2, 3, np.nan, 4, 2, 3, 2, 5],
    'Stays in Weekend Nights': [1, 2, 1, 3, np.nan, 2, 1, 3],
    'Company': [np.nan, 123, np.nan, 456, np.nan, 789, np.nan, np.nan]
}
df = pd.DataFrame(data)
print(df.size)
df.drop_duplicates(inplace=True)
print(df.size)