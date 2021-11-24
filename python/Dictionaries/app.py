customer={
    'name':'john',
    'age': 30,
    'is_verified':True
}
print(customer.get('name'))
print(customer.get('birthday','jan 1 1980'))
customer['age']=29
print(customer.get('age'))


