# JUST A PLAY EXAMPLE WITH NO GUARANTEE TO RUN
from datetime import date

import matplotlib.pyplot as plt
import mysql.connector
import pandas as pd
# get raw data from somewhere
from pandas import DataFrame

cnx = mysql.connector.connect(user='sseltmann', password='secret',
                              host='127.0.0.1',
                              database='employees')
cursor = cnx.cursor()

query = ("SELECT first_name, last_name, hire_date, salary, department FROM employees "
         "WHERE hire_date BETWEEN %s AND %s")

hire_start = date(1999, 1, 1)
hire_end = date(1999, 12, 31)

cursor.execute(query, (hire_start, hire_end))

my_employes = []
for (first_name, last_name, hire_date, salary, department) in cursor:
    my_employes.append([first_name, last_name, hire_date, salary, department])
    print("{}, {} was hired on {:%d %b %Y}".format(
        last_name, first_name, hire_date))

cursor.close()
cnx.close()

# convert to dataframe
df_employes = pd.DataFrame(my_employes, columns=['Vorname', 'Nachname', 'Datum Einführung', 'Löhne', 'Abteilung'])

# clean dataframe
df_employes.fillna(inplace=True)
df_employes.columns = df_employes.columns.str.lower()
df_employes.columns = df_employes.columns.str.replace('ü', 'ue')
df_employes.columns = df_employes.columns.str.replace('ö', 'oe')
df_employes.columns = df_employes.columns.str.replace('ä', 'ae')
df_employes.columns = df_employes.columns.str.replace(' ', '_')

# make barplot
df_plot: DataFrame = df_employes.groupby('abteilung')['loehne'].sum()
df_plot.plot(kind='barh')
plt.show()
df_plot.to_parquet('/home/ubuntu/some_project/data_files/barplot_data.pqt')


cnx = mysql.connector.connect(user='sseltmann', password='secret',
                              host='127.0.0.1',
                              database='employees')
cursor = cnx.cursor()

query = ("SELECT * FROM transactions ")
cursor.execute(query)
transactions_raw = [row for row in cursor]
cursor.close()
cnx.close()

df_transactions = pd.DataFrame(transactions_raw)

df_transactions.fillna(inplace=True)
df_transactions.columns = df_transactions.columns.str.lower()
df_transactions.columns = df_transactions.columns.str.replace('ü', 'ue')
df_transactions.columns = df_transactions.columns.str.replace('ö', 'oe')
df_transactions.columns = df_transactions.columns.str.replace('ä', 'ae')
df_transactions.columns = df_transactions.columns.str.replace(' ', '_')

df_transactions.to_parquet('/home/ubuntu/some_project/data_files/transactions.pqt')


# make barplot
df_plot: DataFrame = df_employes.groupby('transaction_type')['amount'].sum()
df_plot.plot(kind='barh')
plt.show()



