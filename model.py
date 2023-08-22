from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from pickle import dump, load
import pandas as pd
import joblib
from sklearn.preprocessing import MinMaxScaler

def split_data(df: pd.DataFrame):
    y = df['default_flg']
    X = df.drop(columns=['default_flg'])
    return X, y


def open_data(path="data/data_score.csv"):
    df = pd.read_csv(path)
    return df


def preprocess_data(df: pd.DataFrame, test=True):
    # df.dropna(inplace=True)
    df['education_cd'].fillna('SCH', inplace=True)
    num_cols = df.drop(
        columns=['education_cd']).columns
    for col in num_cols:
        if df[col].isna().sum():
            mean = df[col].mean()
            df[col].fillna(mean, inplace=True)
    # print(df)
    if test:
        X_df, y_df = split_data(df)
    else:
        X_df = df

    to_encode = ['education_cd']

    for col in to_encode:
        dummy = pd.get_dummies(X_df[col], prefix=col)
        X_df = pd.concat([X_df, dummy], axis=1)
        X_df.drop(col, axis=1, inplace=True)
    # if test:
    #     scaler = MinMaxScaler()
    #     train_ds = X_df.copy()
    #     train_ds.to_csv('data/train_data.csv')
    #     scaler.fit(X_df)
    #     joblib.dump(scaler, 'data/scaler.gz')
    # else:
    #     scaler = joblib.load('data/scaler.gz')
    #     train_ds = pd.read_csv('data/train_data.csv', index_col='id')
    # X_df.drop(columns=['id'], inplace=True)
    # X_df[train_ds.columns] = scaler.transform(X_df)

    if test:
        return X_df, y_df
    else:
        return X_df


def fit_and_save_model(X_df, y_df, path="data/model_weights_2.mw"):
    model = RandomForestClassifier(n_estimators=500, max_depth=11)
    model.fit(X_df, y_df)

    test_prediction = model.predict(X_df)
    accuracy = accuracy_score(test_prediction, y_df)
    print(f"Model accuracy is {accuracy}")

    with open(path, "wb") as file:
        dump(model, file)

    print(f"Model was saved to {path}")


def load_model_and_predict(df, path="data/model_weights_2.mw"):
    with open(path, "rb") as file:
        model = load(file)

    prediction = model.predict(df)[0]
    # prediction = np.squeeze(prediction)

    prediction_proba = model.predict_proba(df)[0]
    # prediction_proba = np.squeeze(prediction_proba)

    encode_prediction_proba = {
        0: "Вы получите дефолт с вероятностью",
        1: "Вы не получите дефолт с вероятностью"
    }

    encode_prediction = {
        0: "Сожалеем, вы получите дефолт",
        1: "Вы выплатите кредит!"
    }

    prediction_data = {}
    for key, value in encode_prediction_proba.items():
        prediction_data.update({value: prediction_proba[key]})

    prediction_df = pd.DataFrame(prediction_data, index=[0])
    prediction = encode_prediction[prediction]

    return prediction, prediction_df


if __name__ == "__main__":
    df = open_data()
    X_df, y_df = preprocess_data(df)
    fit_and_save_model(X_df, y_df)