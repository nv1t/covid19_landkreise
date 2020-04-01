import pandas as pd
import datetime as dt

def run():
    config = {   
        'name': 'Rheinland-Pfalz',
        'url': 'https://msagd.rlp.de/de/unsere-themen/gesundheit-und-pflege/gesundheitliche-versorgung/oeffentlicher-gesundheitsdienst-hygiene-und-infektionsschutz/infektionsschutz/informationen-zum-coronavirus-sars-cov-2/',
        'table': 0
    }
    
    df = pd.DataFrame()

    df = pd.read_html(config['url'],decimal=',', thousands='.')[int(config['table'])]
    df = df.drop_duplicates(1,keep=False) # strange tables with lk and town splitted
    df = df[:-1] # remove last line, because it is just time information
    df.insert(2,'inzidenz','',True)
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
