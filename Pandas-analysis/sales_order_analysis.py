import sys
import pandas as pd
import numpy as np
import pyodbc
import logging
import matplotlib

logging.basicConfig(filename='logs',level=logging.DEBUG,
                    format='%(asctime)s:%(levelname)s:%(message)s')

#Funtion to get the data from sql and saving it as csv. Reading 100mb from Sql takes longer time for each code exection I prefered to save it as csv to run the code faster for my outputs.
def get_csv_sql(connection_string,query,out_filename):
    '''
    Example of geting csv file from DB
    connection_string = r'DRIVER={SQL Server};SERVER=hostnmae;DATABASE=DBnmae;UID=usename;PWD=pasword'--> your connection sting 
    query = 'select * from INC_ZSOBOOK where RID=(select max(RID) from INC_ZSOBOOK)'-->you query from sqlserver
    # out_filename = 'testcsv'-->desired output filename 
    get_csv_sql(connection_string,query,out_filename)
    '''
    try:
        
        connection = pyodbc.connect(connection_string)
        logging.debug('connection to sql server is successful')

    except pyodbc.InterfaceError as err:

        logging.error('''connection to sql server failed: check the connection srting:''')
        logging.error(connection_string)
        logging.error(err)
 
    SQL_data = pd.read_sql(query,connection)
    return SQL_data.to_csv(('{}.csv'.format(out_filename)), encoding='utf-8', index=False)

#Reading csv file 
RAW_DF = pd.read_csv('sobook.csv', index_col=0)
RAW_DF.head()

