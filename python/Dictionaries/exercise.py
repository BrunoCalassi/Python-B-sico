phone=input('Fone: ')
digits_mapping={
    '1':'Um',
    '2':'Dois',
    '3':'Tres',
    '4':'Quatro'
}
output=''
for ch in phone:
    output+=digits_mapping.get(ch,"!") + " "
print(output)
