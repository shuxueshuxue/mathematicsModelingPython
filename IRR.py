from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"

## 计算现金流的现值
## 假设投资者未来10年每年收到10000元的退休年金，期间贴现率为5%，请问这笔投资的现值为?



# 计算每一期的现金流，将他们依次加起来
# total = 0
# for i in range(10):
#     cf = 10000 / (1 + 0.05) ** (i+1)
#     total += cf
# print(total)

# 用函数封装
def discount(number, money, rate):
    total = 0
    for i in range(number):
        cashflow = money / (1 + rate) ** (i+1)
        total += cashflow
    return total

print(discount(10, 10000, 0.05))





## 计算净现值(npv)
## 假设贴现率为5%，有A、B两个项目，前期均需投入120万. A项目第一年至五年分别收入10.30、50、40、10万, 项目B第一至五年分别收入30、40、40、20、10万，
## 项目A和B哪个投资价值高? (判断哪个项目的投资价值更高，可以考虑分别计算2个项目的净现值)



## 首先考虑项目计算的输入为贴现率、现金流，输出为净现值
cashflow_A = [-120, 10, 30, 50, 40, 10]
cashflow_B = [-120, 30, 40, 40, 20, 10]

#利用enumerate函数将数据对象组合成索引序列， 同时列出数据下标和数据本身
def net_present_value(rate, cashflows):
    total = 0
    for i, cashflow in enumerate(cashflows):
        total += cashflow / (1 + rate) ** i
    return total

npv_A = net_present_value(0.05, cashflow_A)
npv_B = net_present_value(0.05, cashflow_B)
print(npv_A, npv_B)

# 采用二分法
def internal_rate_of_return(cashflows, iterations = 10000):
    rate_0 = 0
    rate_1 = 1
    rate = (rate_0 + rate_1) / 2
    npv = net_present_value(rate, cashflows)
    while abs(npv) > 0.0001:
        if npv > 0:
            rate_0 = rate
            rate = (rate_0 + rate_1) / 2
            npv = net_present_value(rate, cashflows)
        else:
            rate_1 = rate
            rate =  (rate_0 + rate_1) / 2
            npv = net_present_value(rate, cashflows)
    return rate

IRR_A = internal_rate_of_return(cashflow_A, iterations = 10000)
IRR_B = internal_rate_of_return(cashflow_B, iterations = 10000)
print(IRR_A, IRR_B)