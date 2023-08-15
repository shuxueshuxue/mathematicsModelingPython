import requests
import pandas as pd

headers = {
    'Cookie': 's=c51y0g1kmn; xq_a_token=370309a4cfdfe4bc2704623d41715a1159be59eb; xq_r_token=39f1ce2c9cbdf041c8e7e72471a441c2aa4879b2; xq_id_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ1aWQiOi0xLCJpc3MiOiJ1YyIsImV4cCI6MTY5NDIxOTc3NywiY3RtIjoxNjkxNjQzMDg2MDY4LCJjaWQiOiJkOWQwbjRBWnVwIn0.VHbJeKH13ujSCMlBvtGYMjVcX0UDLwpZ2CNbl-9xjbJjIkvLfj3CK_qGwWpoDmEAVdtKlEfbxgudntt26vQ7OW5rvnmx6PwLIPe7CZ114QfOhdqqueWSUfAyfVuTH1gZzTbwK82FbKdoi4xL_-dO4-LD1kU7ytsw9MeCMr6nxlcRVsWLPDCMDuzJFsQL5GbwbXE2X6kWIoPbXYoJv41uCYigUfJeZPKen6wbxGNea78F1EZwZM3VOsdgGfUJHDqe5-W7zffeOXSiXU5lt61Ox-JFCDWbcwQZMnhUXon21eqAy6FrLCG7VHY-wKbGeYklZbl6QQeONxmn4a35cH55nw; Hm_lvt_1db88642e346389874251b5a1eded6e3=1691643111; u=831691643111444; device_id=21b090697496c915c29d729b947101e5; Hm_lpvt_1db88642e346389874251b5a1eded6e3=1691643449',
    'Origin': 'https://xueqiu.com',
    'Referer': 'https://xueqiu.com/hq',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
}

url = 'https://stock.xueqiu.com/v5/stock/screener/quote/list.json?page=1&size=30&order=desc&orderby=percent&order_by=percent&market=CN&type=sh_sz'

response = requests.get(url=url, headers=headers)
json_data = response.json()
# .text获取文本内容
# .content获取图像内容，为二进制数据
# .json()获取字典数据

data_list = json_data['data']['list']
dataframe = pd.DataFrame(data_list)

outputpath ='stock_spider\\output.xlsx'
dataframe.to_excel(outputpath,index=True,header=True)


# for i in range(0, len(data_list)):
#     symbol = print(data_list[i]['symbol'])
#     name = print(data_list[i]['name'])
#     chg = print(data_list[i]['name'])
