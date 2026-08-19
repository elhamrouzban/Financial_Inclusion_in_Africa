import pandas as pd
from sklearn.model_selection import train_test_split


def load_and_split_data():
    train = pd.read_csv("../data/Train_clean.csv")

    X = train.drop(columns=["bank_account"])
    y = train["bank_account"]

    X_train, X_valid, y_train, y_valid = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
        stratify=y
    )

    return X_train, X_valid, y_train, y_valid