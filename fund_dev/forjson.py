import json
import pandas as pd
import matplotlib.pyplot as plt
import csvtomd as cm

with open('1.json', 'r') as f:
    data = f.readlines()[0]

data = data.replace("'", '"')

# data = json.loads(data)

data = pd.read_json(data).T

data.fundnum = data.fundnum.astype(int)

fundnum_sort = data.sort_values(by='fundnum')


most_fund = fundnum_sort[-10:]
name = most_fund.name.tolist()
fundnum = most_fund.fundnum.tolist()
code = most_fund.code.tolist()
to_write = ''
to_write+='|股票名称|股票代码|被持有基金数|\n|---|---|---|\n'
for i in range(len(name)):
    str_i = '|' + str(name[i])+'|'+str(code[i])+'|'+str(fundnum[i])+'|'+'\n'
    to_write+=str_i

with open ('1.md','w') as f:
    f.write(to_write)


# print(most_fund.name)
