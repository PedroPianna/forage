import pandas as pd
import matplotlib.pyplot as plt

def exercise_0(file):
    return pd.read_csv(file)

def exercise_1(df):
    return df.columns

def exercise_2(df, k):
    return df[:k]

def exercise_3(df, k):
    return df.sample(k)

def exercise_4(df):
    return df.value_counts('type')

def exercise_5(df):
    return df.value_counts('nameDest')[:10]

def exercise_6(df):
    return df.loc[df['isFraud'] == 1]

def exercise_7(df):
    df = df.groupby('nameOrig').apply(lambda x: x.nameDest.nunique())
    return df.sort_values(ascending=False)

def visual_1(df):
    pass

def visual_2(df):
    pass

def exercise_custom(df):
    pass
    
def visual_custom(df):
    pass
