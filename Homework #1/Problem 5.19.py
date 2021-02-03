# Madison Fletcher
# 1868748

print('Davy\'s auto shop services')
print('Oil change -- $35')
print('Tire rotation -- $19')
print('Car wash -- $7')
print('Car wax -- $12\n')
service1 = str(input('Select first service:\n'))
service2 = str(input('Select second service:\n\n'))
print('Davy\'s auto shop invoice\n')
shop_services = {'Oil change':', $35', 'Tire rotation':', $19', 'Car wash':', $7','Car wax':', $12'} # shop services put into a dictionary
prices = {'Oil change': 35,'Tire rotation': 19,'Car wash': 7,'Car wax':12} # dictionary with prices as integers instead of strings
if service2 == '-':
    print('Service 1:',service1+shop_services[service1])
    print('Service 2: No service\n')
    print('Total: ${}'.format(prices[service1]))
elif service1 == '-':
    print('Service 1: No service')
    print('Service 2:', service2 + shop_services[service2])
    print('\nTotal: ${}'.format(prices[service2]))
else:
    print('Service 1:', service1+shop_services[service1])
    print('Service 2:', service2+shop_services[service2])
    total = prices[service1] + prices[service2]
    print('\nTotal: ${}'.format(total))




