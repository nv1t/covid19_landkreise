import pandas as pd
import datetime as dt

def run():
    config = {   
        'name': 'Niedersachsen',
        'url': 'https://www.apps.nlga.niedersachsen.de/corona/download.php?csv',
        'remove_columns': [0,1,5,7]
    }
    
    df = pd.DataFrame()

    df = pd.read_csv(config['url'],sep=';',decimal=',', thousands='.')
    if 'remove_columns' in config:
        df = df.drop(df.columns[config['remove_columns']],axis=1)
    df.columns = ['Landkreis','Faelle','Inzidenz','Todesfaelle']
    df['Faelle'] = df['Faelle'].astype(str).str.split(n=1,expand=True)
    df['Faelle'] = df['Faelle'].str.replace('.','').astype(float)
    df['Todesfaelle'] = pd.to_numeric(df['Todesfaelle'],errors='coerce')
    df['Inzidenz'] = pd.to_numeric(df['Inzidenz'], errors='coerce')
    df.insert(0,"Bundesland",config['name'],True)

    df.index = pd.Series([dt.datetime.now()]*len(df))
    df['date'] = [d.date() for d in df.index]
    df['time'] = [d.time() for d in df.index]
    
    return df
