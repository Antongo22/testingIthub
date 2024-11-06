import pandas as pd

def get_name_average_tuples(filename):
    df = pd.read_csv(filename, encoding='utf-8', sep=',')

    required_columns = ['Test1', 'Test2', 'Test3', 'Test4']
    if not all(col in df.columns for col in required_columns):
        raise ValueError(f"Не найдены все необходимые столбцы: {required_columns}")

    df['Average'] = df[required_columns].mean(axis=1).round(1)

    name_average_tuples = [
        (f"{row['First name']} {row['Last name']}", row['Average'])
        for _, row in df.iterrows()
    ]

    return name_average_tuples

def get_name_final_tuples(filename):
    df = pd.read_csv(filename, encoding='utf-8', sep=',')

    if 'Final' not in df.columns:
        raise ValueError("Не найден столбец 'Final' в файле.")

    name_final_tuples = [
        (f"{row['First name']} {row['Last name']}", row['Final'])
        for _, row in df.iterrows()
    ]

    return name_final_tuples



def get_list(filename):
    result1 = get_name_final_tuples(filename)
    result2 = get_name_average_tuples(filename)

    combined_results = [
        [avg[1], final[1]]
        for avg, final in zip(result2, result1)
    ]

    return combined_results

filename = "grades.csv"
result = get_list(filename)
print(result)