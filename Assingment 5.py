import pandas as pd
import findspark
findspark.init()
import pyspark
from pyspark.sql import SparkSession

from pyspark import SparkContext
from pyspark.sql import SQLContext
#sc = SparkContext("local", "App Name")
#sql = SQLContext(sc)

def der_artb(df):
    list = df['BRAND_ID'].unique()
    a = ''
    b = 0
    for i in range(0, len(df)):
        j = list[b]
        if j == df.loc[i, 'BRAND_ID']:
            if a == '':
                a = df.loc[i, 'PARENT_CATEGORY_ID']
                df.loc[i, 'Web_TREE'] = a
            else:
                a = a + '_' + df.loc[i, 'PARENT_CATEGORY_ID']
                df.loc[i, 'Web_TREE'] = a
        else:
            a = ''
            b = b + 1
            if a == '':
                a = df.loc[i, 'PARENT_CATEGORY_ID']
                df.loc[i, 'Web_TREE'] = a

if __name__ == "__main__":
    df = pd.read_excel('I:\C driver\Ingrity\Session 5 Python Assignment (1).xlsx')
    #spark = SparkSession.Builder().appName("Practice").master("local[2]").getOrCreate()
    #df1 = pyspark.pandas.read_excel('I:\C driver\Ingrity\Session 5 Python Assignment (1).xlsx', header=TRUE)
    der_artb(df)
    print(df)

    #df2 = sql.createDataFrame(df)
    #df2.write.csv('I:\C driver\Ingrity\Output',header=TRUE)
    #df2.write.json('I:\C driver\Ingrity\Output')
    #df2.write.parquet('I:\C driver\Ingrity\Output')
