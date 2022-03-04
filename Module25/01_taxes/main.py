from PropertyClasses import Car
from PropertyClasses import Apartment
from PropertyClasses import CountryHouse


tax_summ = 0
fund = int(input('Введите количество денег: '))
car = Car(int(input('Введите стоимость машины: ')))
apartment = Apartment(int(input('Введите стоимость квартиры: ')))
country_house = CountryHouse(int(input('Введите стоимость дачи: ')))

tax_summ += car.calc_tax()
tax_summ += apartment.calc_tax()
tax_summ += country_house.calc_tax()
print('=' * 40)
print('Налог на имущество составляет: ', tax_summ, '$', sep='')
if fund < tax_summ:
    print('На имущество не хватает денег: ', abs(fund - tax_summ),'$', sep='')
