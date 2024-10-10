immutable_var = (1, 2, 'a', 'b')
print(immutable_var)

#immutable_var[0] = 23 #Ошибка потому что кортеж работает как хранилище для списка,которое должно быть неизменным.

muteble_list = [1, 2, 'a', 'b', 'Modfied']
muteble_list[0:4] = '4', '25', 'ALT', 'Google'
print(muteble_list)



