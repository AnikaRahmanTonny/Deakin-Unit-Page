import pandas as pd

# Read the original dataset
df = pd.read_csv('train.csv')

# Select only the 'question' and 'human_ans_spans' columns
filtered_df = df[['question', 'human_ans_spans']]

# Drop rows where 'human_ans_spans' is "ANSWERNOTFOUND"
filtered_df = filtered_df[filtered_df['human_ans_spans'] != "ANSWERNOTFOUND"]

# Rename the 'human_ans_spans' column to 'answer'
filtered_df.rename(columns={'human_ans_spans': 'answer'}, inplace=True)

# Save the filtered dataframe to a new CSV file
#filtered_df.to_csv('new.csv', index=False)
filtered_df.to_excel('new.xlsx', index=False)