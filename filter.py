import pandas as pd

# Загрузка данных
df = pd.read_csv("data.csv")

# Фильтрация данных (например, выбираем строки, где значение в колонке 'weight' больше 100)
filtered_df = df[df["weight"] > 100]

# Сохранение результата
filtered_df.to_csv("filtered_data.csv", index=False)

print("Фильтрация завершена, данные сохранены в 'filtered_data.csv'.")
