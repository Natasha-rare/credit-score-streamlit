# импортируем библиотеку streamlit
import streamlit as st

# импортируем библиотеку pandas
import pandas as pd
# Название
st.title("Песочница")

# Заголовок
st.header("Это заголовок")

# Подзаголовок
st.subheader("Это подзаголовок")

# Подзаголовок
st.subheader("Это подзаголовок")

# Текст
st.text("Просто текст")
data = pd.read_csv('data/data_score.csv')
st.write(data)
#
# if st.checkbox("Show/Hide"):
#     # показываем текст если чекбокс выбран
#     st.text("Showing the widget")
#
# status = st.radio("Select Gender: ", ('Male', 'Female'))
#
# if (status == 'Male'):
#     st.error("Male")
# else:
#     st.success("Female")
#
#
# st.title('Калькулятор индекса массы тела (ИМТ)')
#
# # СЧИТЫВАЕМ ВЕС
# weight = st.number_input("Введите ваш вес (в килограммах)")
#
# # СЧИТЫВАЕМ РОСТ
# # используем radio button, чтобы указать единицы измерения
# status = st.radio('Укажите единицы измерения роста: ', ('см', 'м', 'футы'))
#
# # сравниваем различные статусы для единиц измерения роста
# if (status == 'см'):
#     # считываем значение роста в сантиметрах
#     height = st.number_input('Сантиметры')
#
#     try:
#         bmi = weight / ((height / 100) ** 2)
#     except:
#         st.text("Введите ваш рост")
#
# elif (status == 'м'):
#     # считываем значение роста в метрах
#     height = st.number_input('Метры')
#
#     try:
#         bmi = weight / (height ** 2)
#     except:
#         st.text("Введите ваш рост")
#
# else:
#     # считываем значение роста в футах
#     height = st.number_input('Футы')
#
#     # 1 meter = 3.28
#     try:
#         bmi = weight / (((height / 3.28)) ** 2)
#     except:
#         st.text("Введите ваш рост")
#
# # проверяем нажата кнопка или нет
# if (st.button('Рассчитать ИМТ')):
#
#     # напечатать значение ИМТ
#     st.text(f"Ваш ИМТ равен {bmi:.2f}")
#
#     # интерпретация ИМТ
#     if (bmi < 16):
#         st.error("Выраженный дефицит массы тела")
#     elif (bmi >= 16 and bmi < 18.5):
#         st.warning("Недостаточная (дефицит) масса тела")
#     elif (bmi >= 18.5 and bmi < 25):
#         st.success("Норма")
#     elif (bmi >= 25 and bmi < 30):
#         st.warning("Избыточная масса тела")
#     elif (bmi >= 30):
#         st.error("Любитель вкусняшек")
#
# import plotly_express as px
#
# PATH = "https://www.dropbox.com/scl/fi/226nfwteim6x2x7q0c36a/football.csv?dl=1&rlkey=cd2t0odbqr8g0yxnnul51mykb"
#
# df = st.cache_data(pd.read_csv)(PATH)
#
# clubs = st.sidebar.multiselect('Выберите клуб', df['Club'].unique())
# nationalities = st.sidebar.multiselect('Укажите национальность игроков', df['Nationality'].unique())
#
# new_df = df[(df['Club'].isin(clubs)) & (df['Nationality'].isin(nationalities))]
# st.write(new_df)
#
# # строим графики используя plotly express
# fig = px.scatter(new_df, x='Overall', y='Age', color='Name')
#
# # рисуем!
# st.plotly_chart(fig)