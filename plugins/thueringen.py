import pandas as pd
import datetime as dt

def run():
    config = {   
        'name': 'Thueringen',
        'url': 'https://corona.thueringen.de/covid-19-bulletin/',
        'table': 1,
        'remove_columns': [1,3,4,5,6]
    }
    
    df = pd.DataFrame()

    df = pd.read_html(config['url'],header=0,decimal=',', thousands='.')[int(config['table'])]
    if 'remove_columns' in config:
        df = df.drop(df.columns[config['remove_columns']],axis=1)
    df.insert(2,'Inzidenz','',True)
    df.columns = ['Landkreis','Faelle','Inzidenz','Todesfaelle']
    df['Faelle'] = df['Faelle'].astype(str).str.split(n=1,expand=True)
    df['Faelle'] = df['Faelle'].str.replace('.','').astype(float)
    df['Todesfaelle'] = pd.to_numeric(df['Todesfaelle'],errors='coerce')
    df['Inzidenz'] = pd.to_numeric(df['Inzidenz'],errors='coerce')
    df.insert(0,"Bundesland",config['name'],True)

    df.index = pd.Series([dt.datetime.now()]*len(df))
    df['date'] = [d.date() for d in df.index]
    df['time'] = [d.time() for d in df.index]
    
    return df
