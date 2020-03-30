import pandas as pd
import datetime as dt

bundeslaender = [
    {
        'name': 'Sachsen',
        'url': 'https://www.coronavirus.sachsen.de/infektionsfaelle-in-sachsen-4151.html',
        'table': 0
    },
    {
        'name': 'Hessen',
        'url': 'https://soziales.hessen.de/gesundheit/infektionsschutz/coronavirus-sars-cov-2/taegliche-uebersicht-der-bestaetigten-sars-cov-2-faelle-hessen',
        'table': 0
    },
    {
        'name': 'Bayern',
        'url': 'https://www.lgl.bayern.de/gesundheit/infektionsschutz/infektionskrankheiten_a_z/coronavirus/karte_coronavirus/index.htm',
        'table': 2,
        'remove_columns': [2,5] 
    }
]

result = pd.DataFrame()

for i in bundeslaender:
    df = pd.read_html(i['url'],header=0,decimal=',', thousands='.')[int(i['table'])]
    if 'remove_columns' in i:
        df = df.drop(df.columns[i['remove_columns']],axis=1)
    df.columns = ['Landkreis','Faelle','Inzidenz','Todesfaelle']
    df['Faelle'] = df['Faelle'].astype(str).str.split(' ',n=1,expand=True)
    df = df.fillna('-')
    df.insert(0,"Bundesland",i['name'],True)

    result = pd.concat([result,df])

result.index = pd.Series([dt.datetime.now()]*len(result))
result['date'] = [d.date() for d in result.index]
result['time'] = [d.time() for d in result.index]

print(result.to_csv(encoding='utf-8'))
