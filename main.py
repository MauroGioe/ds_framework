import argparse
import importlib
import importlib.util
import sys
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.metrics import accuracy_score, root_mean_squared_error

def load_module(package, module):
    try:
        spec = importlib.util.spec_from_file_location(module, "../../"+package+"/"+input_table+".py")
        loaded_module = importlib.util.module_from_spec(spec)
        sys.modules[module] = loaded_module
        spec.loader.exec_module(loaded_module)
        print(f"The module {module} in the package {package} was loaded correctly")
    except:
        print(f"The module {module} was not found in the package {package}")
        loaded_module = "Empty"
    return loaded_module

def default_data_wrangling(data, target):
    y = data[target]
    X = data.drop(target, axis=1)
    X_train, X_test, y_train, y_test = train_test_split(X, y,test_size=0.30, random_state=42)
    return X_train, X_test, y_train, y_test

def train_model(X_train, y_train, model):
    models = {
        "logistic_regression": LogisticRegression,
        "linear_regression":LinearRegression
    }
    choosen_model = models[model]
    print(f"Running {model}")
    choosen_model = choosen_model().fit(X_train,y_train)
    return choosen_model

def testing(X_test, y_test, model, target_type):
    y_pred = model.predict(X_test)
    if target_type == "binary":
        acc = accuracy_score(y_test, y_pred)
        print(f"Accuracy equal to {round(acc, 2)}")
    if target_type == "continuos":
        rmse = root_mean_squared_error(y_test, y_pred)
        print (f"RMSE equal to {round(rmse, 2)}")

def main(input_table, input_path, target, target_type, model):
    ingestion = load_module("ingestion", input_table)
    data = ingestion.ingestion(input_path)
    print(data)
    data_wrangling = load_module("data_wrangling", input_table)
    try:
        X_train, X_test, y_train, y_test = data_wrangling.data_wrangling(data, target)
    except AttributeError:
        print("Running default data wrangling")
        X_train, X_test, y_train, y_test = default_data_wrangling(data, target)
    feature_engineering = load_module("feature_engineering", input_table)
    try:
        X_train, X_test = feature_engineering.feature_engineering(data, target)
    except AttributeError:
        print("Feature engineering step was not executed")
    choosen_model = train_model(X_train, y_train, model)
    testing(X_test, y_test, choosen_model, target_type)

parser = argparse.ArgumentParser()
parser.add_argument("--input_table")
parser.add_argument("--input_path")
parser.add_argument("--target")
parser.add_argument("--target_type")
parser.add_argument("--model")

args = parser.parse_args()
input_table = args.input_table
input_path = args.input_path
target = args.target
target_type = args.target_type
model = args.model


main(input_table, input_path, target, target_type, model)