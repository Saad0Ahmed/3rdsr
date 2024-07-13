#to create dataframes from dictionary and csv file
import pandas as pd
data = {
    "calories": [234,567,789],
    "duration": [40,56,78]
}
df = pd.DataFrame(data)
print("datarames created using dictionary")
print(df)
df = pd.read_csv('Book.csv')
print("\ndataframe created using file\n")
print(df)