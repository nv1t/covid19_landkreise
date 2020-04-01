import os
import importlib
import pandas as pd

if __name__ == '__main__':
    result = pd.DataFrame()

    modules = [os.path.splitext(f)[0] for f in os.listdir('plugins') if os.path.isfile(os.path.join('plugins',f))]
    
    for module in modules:
        df = pd.DataFrame()
        m = importlib.import_module('plugins.'+module)
        df = m.run()
        result = pd.concat([result,df])
        
    print(result.to_csv(encoding='utf-8'))
