import os
import sys
import importlib
import datetime
import pandas as pd

if __name__ == '__main__':
    result = pd.DataFrame()

    modules = [os.path.splitext(f)[0] for f in os.listdir('plugins') if os.path.isfile(os.path.join('plugins',f))]
    
    if len(sys.argv) > 1:
        df = pd.DataFrame()
        m = importlib.import_module('plugins.'+sys.argv[1])
        df = m.run()

        print(df)
        sys.exit(0)

    for module in modules:
        try:
            df = pd.DataFrame()
            m = importlib.import_module('plugins.'+module)
            df = m.run()
            result = pd.concat([result,df])
        except:
            with open('error.log','a') as fh:
                fh.write("%s [ERR] Module %s\n" % (datetime.datetime.now(),module))
        
    print(result.to_csv(encoding='utf-8'))
