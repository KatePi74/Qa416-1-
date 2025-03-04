import pandas as pd

# Загрузка данных
df = pd.read_csv("data.csv")

# Фильтрация данных (например, выбираем строки, где значение в колонке 'age' больше 30)
filtered_df = df[df["age"] > 30]

# Сохранение результата
filtered_df.to_csv("filtered_data.csv", index=False)

print("Фильтрация завершена, данные сохранены в 'filtered_data.csv'.")
