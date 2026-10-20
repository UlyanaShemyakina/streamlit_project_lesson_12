import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# st.title("Загрузка данных!")

# uploaded_file = st.file_uploader(
#     "Загрузите файл в формате CSV",
#     type=["csv"]
# )

# if uploaded_file:
#     df = pd.read_csv(uploaded_file)
#     st.subheader("Данные: ")
#     # print(df.head())
#     st.dataframe(df)

# отобразить отдельно мужчин и женщин
# сначала фильтруем по полю и отображаем данные

uploaded_file = st.file_uploader(
    "Загрузите файл в формате CSV",
    type=["csv"]
)

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    dfs = {
        "subscriber": df[df["member_type"] == "Subscriber"], 
        "casual": df[df["member_type"] == "Casual"]
    }

    for title, data in dfs.items():
        data.drop(columns=["member_type"], inplace=True)
        st.subheader(f"Данные: {title}")
        st.dataframe(data)

    st.subheader("Распеределение по городам у subscriber")
    fig, ax = plt.subplots()
    ax.hist(dfs["subscriber"]["city"])
    ax.set_title("Распеределение по городам у subscriber")
    st.pyplot(fig)

    st.bar_chart(data=dfs["subscriber"], x="bike_type", y=["city"])

    # построить линейный график зависимости price_eur от distance_km
    st.subheader("Зависимость distance_km от casual")
    st.line_chart(data=dfs["casual"][dfs["casual"]["distance_km"] > 10], x="distance_km", y="price_eur")