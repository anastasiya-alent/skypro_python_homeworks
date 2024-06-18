from smartphone import Smartphone

catalog = [Smartphone('Apple', 'iPhone 7', '+79511955616'), 
           Smartphone('Apple', 'iPhone 8', '+79511965565'), 
           Smartphone('Apple', 'iPhone 11', '+79056549823'),
           Smartphone('Apple', 'iPhone 12', '+79009875263'),
           Smartphone('Apple', 'iPhone 15', '+79191239865')]

for phone in catalog:
    phone.fullinfo()