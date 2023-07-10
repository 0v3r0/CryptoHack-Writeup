secret=12
e=65537
p= 17
q=23

mod=p*q

res= pow(secret,e,mod)
print(res)