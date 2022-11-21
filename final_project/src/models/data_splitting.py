from sklearn.model_selection import train_test_split

def data_splitting(df):
    label = "total_cases_per_million_level"
    y = df[label]
    X = df[df.columns.drop(label)]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=21)
    return X_train, X_test, y_train, y_test