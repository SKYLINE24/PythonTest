name='Erbil Can2'
surname='Keleş'
age=23

#print('My name is {} {}. I am {} years old.'.format(name,surname,age))
#print('my name is {1} {0}. I am {2} years old.'.format(name,surname,age))
print(f'My name is {name} {surname}. I am {age} years old.')
#f fonksiyonu ile .format yazmamıza gerek kalmıyor direk {} içerisine yazıyoruz

result=200/700

print('the result is {r:1.3}'.format(r=result))
#3 bilgisi virgülden sonrasında kaç basamak olması gerektiğini sağlıyor
#1 bilgisi virgülden önce kaç basamak olması gerektiğini sağlıyor
