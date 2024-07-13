import asyncio
import aiohttp
import time
import pandas as pd

async def get_pokemon_contests():
    """
    Docstring for get_pokemon_contests() fucntion
    """
    with aiohttp.ClientSession() as session:
        pass

lister=[[1,'N',12,[1,2,3,4,5,]],[2,'N',13,[1,2,3,]],[3,'N',14,[1]]]
df=pd.read_excel('Input_File.xlsx')
print(df)
api_str='https://pokeapi.co/api/v2/contest-type/'


start = time.time()

def get_tasks(session,Affected_CIs):
    tasks = []
    for CI in Affected_CIs:
        param={}
        param["id"]=CI
        tasks.append(asyncio.create_task(session.get(api_str,params = param, ssl=False)))
    return tasks

async def get_symbols(Affected_CIs):
    async with aiohttp.ClientSession() as session:
        tasks = get_tasks(session,Affected_CIs)
        results=[]
        # you could also do
        # tasks = [session.get(URL.format(symbol, API_KEY), ssl=False) for symbol in symbols]
        responses = await asyncio.gather(*tasks)
        for response in responses:
            results.append(await response.json())
        return results

#asyncio.run(get_symbols())
for i in lister:
    CHGNum=i[0]
    CHGState=i[1]
    CHGTime=i[2]
    Affected_CIs=i[3]
    results=asyncio.run(get_symbols(Affected_CIs))
    print(results)
