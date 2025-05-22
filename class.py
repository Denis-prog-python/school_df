import pandas as pd

# Создаём данные
data = {
    'Ученик': ['Иван', 'Мария', 'Алексей', 'Ольга', 'Дмитрий', 'Елена', 'Сергей', 'Анна', 'Павел', 'Наталья'],
    'Математика': [5, 4, 3, 5, 4, 3, 2, 5, 4, 3],
    'Физика': [4, 5, 4, 3, 2, 4, 5, 3, 4, 5],
    'Химия': [3, 4, 5, 2, 3, 4, 3, 5, 4, 3],
    'Литература': [5, 5, 4, 3, 4, 5, 4, 3, 2, 5],
    'История': [4, 3, 2, 5, 4, 3, 5, 4, 3, 2]
}

df = pd.DataFrame(data)

print("Первые 3 строки DataFrame:")
print(df.head(3))

mean_grades = df.mean(numeric_only=True)
print("\nСредние оценки по предметам:")
print(mean_grades)

median_grades = df.median(numeric_only=True)
print("\nМедианные оценки по предметам:")
print(median_grades)

Q1_math = df['Математика'].quantile(0.25)
Q3_math = df['Математика'].quantile(0.75)
IQR_math = Q3_math - Q1_math

print(f"\nQ1 (25-й перцентиль) по математике: {Q1_math}")
print(f"Q3 (75-й перцентиль) по математике: {Q3_math}")
print(f"IQR по математике: {IQR_math}")

std_grades = df.std(numeric_only=True)
print("\nСтандартное отклонение оценок:")
print(std_grades)
