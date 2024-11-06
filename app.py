import streamlit as st
import pandas as pd
from io import BytesIO


# Функция для преобразования DataFrame в .xlsx формат
def convert_df_to_excel(df):
    output = BytesIO()
    with pd.ExcelWriter(output, engine="xlsxwriter") as writer:
        df.to_excel(writer, index=False, sheet_name="Sheet1")
    return output.getvalue()


# Настройка интерфейса
st.title("CSV to Excel Converter")

# Загрузка CSV файла
uploaded_file = st.file_uploader("Загрузите ваш CSV файл", type="csv")

# Выбор разделителя
delimiter = st.selectbox("Выберите разделитель", (",", "\\t", ";"))

# Конвертация и загрузка
if uploaded_file is not None:
    # Определение разделителя
    sep = delimiter if delimiter != "\\t" else "\t"

    # Чтение CSV файла
    df = pd.read_csv(uploaded_file, sep=sep)

    # Отображение загруженного DataFrame
    st.write("Предварительный просмотр данных:")
    st.dataframe(df)

    # Конвертация в Excel
    excel_data = convert_df_to_excel(df)

    # Кнопка для скачивания файла
    st.download_button(
        label="Скачать как .xlsx",
        data=excel_data,
        file_name="converted_file.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
    )
