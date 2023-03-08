import pandas
import requests
import urllib.request
import urllib


def clean_qcew_frame(year,qtr,area):
    df = df.replace('[/\W+/g]','',regex=True) #remove ""
    df.columns = df.iloc[0]
    df.drop([0], inplace=True)
    df = df.loc[df['own_code']=='5'] #set ownership code to 5 for private businesses 
