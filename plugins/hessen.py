import pandas as pd
import datetime as dt

def run():
    config = {   
        'name': 'Hessen',
        'url': 'https://soziales.hessen.de/gesundheit/infektionsschutz/coronavirus-sars-cov-2/taegliche-uebersicht-der-bestaetigten-sars-cov-2-faelle-hessen',
        'table': 0,
        'remove_columns': [2,5,6]
    }
    
    df = pd.DataFrame()

    df = pd.read_html(config['url'],decimal=',', thousands='.')[int(config['table'])]
    if 'remove_columns' in config:
        df = df.drop(df.columns[config['remove_columns']],axis=1)
    df = df[2:]
    df.columns = ['Landkreis','Faelle','Todesfaelle','Inzidenz']
    df['Faelle'] = df['Faelle'].astype(str).str.split(n=1,expand=True)
    df['Faelle'] = df['Faelle'].str.replace('.','').astype(float)
    df['Todesfaelle'] = pd.to_numeric(df['Todesfaelle'],errors='coerce')
    df['Inzidenz'] = pd.to_numeric(df['Inzidenz'],errors='coerce')
    df.insert(0,"Bundesland",config['name'],True)

    df.index = pd.Series([dt.datetime.now()]*len(df))
    df['date'] = [d.date() for d in df.index]
    df['time'] = [d.time() for d in df.index]
    
    return df
