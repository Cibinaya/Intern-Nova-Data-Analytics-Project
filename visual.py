import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#style
sns.set_theme(style="dark")

#load dataset
df=pd.read_csv('StudentCount_PuneRegion_.csv')

#handle missing values
Std_cols=[f'Std_{i}' for i in range(1,13)]
df[Std_cols]=df[Std_cols].fillna(0)
df['Total_Students']= df[Std_cols].sum(axis=1)

#chat 1 bar plot
plt.figure(figsize=(10,5))
top_blocks=df['blkname'].value_counts().head(10)
top_blocks.plot(kind='bar',color='red')
plt.title('1. TOP 10 BLOCKS BY SCHOOL COUNT')
plt.xlabel('Block Name')
plt.ylabel('Number of Schools')
plt.xticks(rotation=45)
plt.show()
plt.tight_layout()
plt.savefig('block_school_distribution.png')
plt.close()

#chart 2  lineplot
plt.figure(figsize=(12,5))
grade_totals=df[Std_cols].sum()
sns.lineplot(x=[f'Std_{i}' for i in range(1,13)],y=grade_totals.values, markers='o',color='pink',linewidth=2.5)
plt.title("2.TOTAL STUDENT ENROLLMENT TREND ACROSS STANDARDS" , fontsize=12, fontweight='bold')
plt.xlabel('Standard')
plt.ylabel('Total students')
plt.xticks(rotation=45)
plt.show()
plt.tight_layout()
plt.savefig('chart 2 grade enrollment trend.png')
plt.close()

#chart 3 barplot
plt.figure(figsize=(11,5))
mgt_avg=df.groupby('schmgt_desc')['Total_Students'].mean().sort_values(ascending=False)
sns.barplot(x=mgt_avg.values,y=mgt_avg.index,palette='viridis')
plt.title("3. AVERAGE STUDENT STRENGHT BY SCHOOL MANAGEMENT TYPE", fontsize=12, fontweight='bold')
plt.xlabel('Average number of students per school')
plt.ylabel('Mnagement Description')
plt.show()
plt.tight_layout()
plt.savefig('chart 3 management avg students.png')
plt.close()

#chart 4 boxplot
plt.figure(figsize=(8,4))
sns.boxplot(x=df['Total_Students'], color='orange')
plt.title('4. DISTRIBUTION AND OUTLIER ANALYSIS OF TOTAL STUDENTS PER SCHOOL', fontsize=12, fontweight='bold')
plt.xlabel('Total Students')
plt.show()
plt.tight_layout()
plt.savefig('chart4 total students boxplot.png')
plt.close()

#chart 5  count plot
plt.figure(figsize=(10,5))
sns.countplot(y=df['schmgt_desc'], order=df['schmgt_desc'].value_counts().index, palette='magma')
plt.title('5. TOTAL NUMBER OF SCHOOLS UNDER EACH MANAGEMENT CATEGORY', fontsize=12, fontweight='bold')
plt.xlabel('Number of schools')
plt.ylabel('Management Type')
plt.show()
plt.tight_layout()
plt.savefig('chart 5 management school count.png')
plt.close()

print("All 5 visualizations generated and saved successfully as PNG images")