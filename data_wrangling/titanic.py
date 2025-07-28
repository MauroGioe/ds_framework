from sklearn.model_selection import train_test_split

def data_wrangling(data, target):
    data = data.dropna()
    y = data[target]
    X = data.drop(target, axis=1)
    X = X[["Pclass","Sex", "Age"]]
    X["Sex"] = X["Sex"] == "male"
    X_train, X_test, y_train, y_test = train_test_split(X, y,test_size=0.30, random_state=42)
    return X_train, X_test, y_train, y_test