import pandas as pd
import streamlit as st
from PIL import Image
from model import open_data, preprocess_data, split_data, load_model_and_predict, fit_and_save_model


def process_main_page():
    show_main_page()
    process_side_bar_inputs()


def show_main_page():
    image = Image.open('data/img.jpg')

    st.set_page_config(
        layout="wide",
        initial_sidebar_state="auto",
        page_title="Credit default",
        page_icon=image,
    )

    st.write(
        """
        # Классификация дефолта
        Определение дефолта по данным клиента
        """
    )

    st.image(image)


def write_user_data(df):
    st.write("## Ваши данные")
    # print(df.columns.values)
    st.write(df[['gender_cd', 'age', 'education_cd','car_own_flg', 'good_work_flg',
                 'income', 'region_rating', 'appl_rej_cnt', 'out_request_cnt']])


def write_prediction(prediction, prediction_probas):
    st.write("## Предсказание")
    if prediction == 'Вы выплатите кредит!':
        st.success(prediction)
    else:
        st.error(prediction)
    # st.write(prediction)

    st.write("## Вероятность предсказания")
    st.write(prediction_probas)


def process_side_bar_inputs():
    st.sidebar.header('Заданные пользователем параметры')
    user_input_df = sidebar_input_features()
    write_user_data(user_input_df)

    train_df = open_data()
    train_X_df, _ = split_data(train_df)
    full_X_df = pd.concat((user_input_df, train_X_df), axis=0)
    preprocessed_X_df = preprocess_data(full_X_df, test=False)

    user_X_df = preprocessed_X_df[:1]


    prediction, prediction_probas = load_model_and_predict(user_X_df)
    write_prediction(prediction, prediction_probas)


def sidebar_input_features():
    sex = st.sidebar.selectbox("Пол", ("Мужской", "Женский"))
    education = st.sidebar.radio("Степень образования", (
    "Школьник", "Выпускник школы", "Студент", 'Аспирант', 'Окончил университет'))

    age = st.sidebar.slider("Возраст", min_value=18, max_value=72, value=21,
                            step=1)
    car_own = st.sidebar.checkbox('Есть ли у вас машина', ('Да', 'Нет'))
    print(car_own)

    good_work = st.sidebar.checkbox('Считаете ли вы свою работу хорошей?', ('Да', 'Нет'))

    region_rating = st.sidebar.slider("Оцените регион, в котором вы живете", min_value=0, max_value=100, value=50,
                            step=10)

    income = st.sidebar.number_input("Укажите ваш ежемесячный доход в рублях")

    app_rejected = st.sidebar.slider("Укажите число отказанных прошлых заявок", min_value=0, max_value=35, value=0,
                            step=1)

    requests_cnt = st.sidebar.slider("Укажите число ваших запросов в бюро", min_value=0, max_value=55, value=0,
                                     step=1)

    translatetion = {
        "Мужской": 0,
        "Женский": 1,
        'Школьник': 'SCH',
        'Выпускник школы': 'GRD',
        'Студент': 'UGR',
        'Аспирант': 'PGR',
        'Окончил университет': 'ACD',
        'Да': 1,
        'Нет': 0
    }

    data = {
        "gender_cd": translatetion[sex],
        "age": age,
        'education_cd': translatetion[education],
        'car_own_flg': car_own,
        'good_work_flg': good_work,
        'income': income,
        'region_rating': region_rating,
        'appl_rej_cnt': app_rejected,
        'out_request_cnt': requests_cnt
    }

    df = pd.DataFrame(data, index=[0])

    return df


if __name__ == "__main__":
    process_main_page()