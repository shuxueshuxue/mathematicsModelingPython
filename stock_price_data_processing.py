import requests

ur1 = 'http://qt.gtimg.cn/g=sh600036'
stk_text = requests.get(ur1).text

stk_full_tick = stk_text.split('~')

last_price = float(stk_full_tick[3])
dt = stk_full_tick[30]
