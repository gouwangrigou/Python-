sandwich_orders = ['yangrou', 'niurou', 'zhurou','yangrou', 'yangrou']
finished_sandwich = []

while sandwich_orders:
    finished_sandwich = sandwich_orders.pop()
    if finished_sandwich == 'yangrou':
        print("yangroumaiwanle")
        continue
    print(finished_sandwich)

print(sandwich_orders)
