price = 1000000
has_good_credit=True

if has_good_credit:
    pagamento=0.1*price
else:
    pagamento=0.2*price
print(f"Pagamento: ${pagamento}")