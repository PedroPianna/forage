import pandas as pd
import matplotlib.pyplot as plt
pd.options.display.float_format = '{:.2f}'.format

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
    def transaction_counts(df):
        return df.value_counts('type')

    def transaction_counts_split_by_fraud(df):
        return df.loc[df['isFraud'] == 1].value_counts('type')

    fig, axs = plt.subplots(2, figsize=(6,10))
    transaction_counts(df).plot(ax=axs[0], kind='bar')
    axs[0].set_title('Transaction types bar chart')
    axs[0].set_xlabel('Type of transaction')
    axs[0].set_ylabel('Number of transactions')
    transaction_counts_split_by_fraud(df).plot(ax=axs[1], kind='bar')
    axs[1].set_title('Transaction types split by fraud bar chart')
    axs[1].set_xlabel('Type of transaction')
    axs[1].set_ylabel('Number of transactions')
    fig.suptitle('Number of transactions and fraudulent transactions by type')
    fig.tight_layout(rect=[0, 0.03, 1, 0.95])
    for ax in axs:
      for p in ax.patches:
          ax.annotate(p.get_height(), (p.get_x(), p.get_height()))
    return 'This plot allows us to draw inferences about trends in fraudulent transaction types'

def visual_2(df):
    def query(df):
        df = df.loc[df['type'] == 'CASH_OUT']
        orig_delta = []
        dest_delta = []
        for index, row in df.iterrows():
            orig_delta.append(row['oldbalanceOrg'] - row['newbalanceOrig'])
            dest_delta.append(row['newbalanceDest'] - row['oldbalanceDest'])
        df = pd.DataFrame({'orig_delta': orig_delta, 'dest_delta': dest_delta})
        # print(df)
        return df
    plot = query(df).plot.scatter(x='orig_delta',y='dest_delta')
    plot.set_title('Difference from origin and destination accounts in Cash Out transcations')
    plot.set_xlim(left=-1e3, right=1e3)
    plot.set_ylim(bottom=-1e3, top=1e3)
    return 'A plot that allows us to identify how the difference from origin and destination accounts in Cash Out transcations relate to each other, making it easier to spot patters and outliers'

def exercise_custom(df):
    def mean(list):
        return sum(list) / len(list)
    fraud = df.loc[df['isFraud'] == 1]
    df_transaction= fraud.loc[df['type'] == 'TRANSFER']
    df_cash_out = fraud.loc[df['type'] == 'CASH_OUT']
    amount_transaction = []
    amount_cash_out = []
    for index, row in df_transaction.iterrows():
        amount_transaction.append(row['amount'])
    for index, row in df_cash_out.iterrows():
        amount_cash_out.append(row['amount'])
    # make them the same lenth
    i = 0
    while len(amount_transaction) != len(amount_cash_out):
        if len(amount_transaction) > len(amount_cash_out):
            amount_cash_out.append(mean(amount_cash_out))
        else:
            amount_transaction.append(mean(amount_transaction))
        i += 1

    print(f'applied mean to {i} elements')
    
    df = pd.DataFrame({'amount_transaction': amount_transaction, 'amount_cash_out': amount_cash_out})
    return df
    
def visual_custom(df):
    plot = exercise_custom(df).plot.scatter(x='amount_transaction',y='amount_cash_out')
    plot.set_title('Distribution of transaction amounts in different types of fraudulent transactions')
    plot.set_xlim()
    plot.set_ylim()
    return 'Distribution of transaction amounts in different types of fraudulent transactions'

def bonus(df):
    df = df.loc[df['isFraud'] == 1].value_counts('amount')
    plot = df.plot(kind='hist')
    plot.set_title('Fraudulent transactions with same amounts histogram')
    plot.set_xlabel('Number of transactions with same amount')
    plot.set_ylabel('Number of transactions')
    return 'A way to spot trends in fraudulent transactions with the same amount'

# https://github.com/PedroPianna