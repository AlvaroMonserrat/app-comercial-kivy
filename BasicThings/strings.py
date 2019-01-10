#String

"""
s1 = "Esto es un string"
s2 = 'Esto tambien es un string'
"""
a = chr(67) #retorna el caracter que esta asociado al numero ascii
b = ord('A') #retorna el numero ascii asociado al caracter

s = "Alvaro Javier Monserrat Aguirre"
lt = s.split(" ")

k = s.replace("Javier", "")

print(a)
print(b)
print(lt)
print(k)

for k, v in enumerate("Iterando Strings"):
    print(k, v)