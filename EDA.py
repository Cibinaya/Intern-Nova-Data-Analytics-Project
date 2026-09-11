import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#1. load dataset
df=pd.read_csv('StudentCount_PuneRegion_.csv')

#2. handle missing values in standard column
Std_cols= [f'Std_{i}' for i in range(1,13)]
df[Std_cols]= df[Std_cols].fillna(0)

#3. create total students derived feature
df['Total_Students']=df[Std_cols].sum(axis=1)

print("1. DESCRIPTIVE STATISTICS")
print(df['Total_Students'].describe())

print("2. MANAGEMENT WISE AVERAGE STUDENTS")
print(df.groupby('schmgt_desc')['Total_Students'].mean().sort_values(ascending=False))

#generate and visualization chart
plt.figure(figsize=(12,6))
top_blocks=df['blkname'].value_counts().head(10)
top_blocks.plot(kind='bar',color='purple')
plt.title('TOP 10 BLOCKS BY SCHOOL COUNT')
plt.xlabel('Block Name')
plt.ylabel('Number of Schools')
plt.xticks(rotation=45)
plt.show()
plt.tight_layout()

#save charts as image
plt.savefig('block_school_distribution.png')
print("EDA Chart saved successfully as'block_school_distribution.png'")