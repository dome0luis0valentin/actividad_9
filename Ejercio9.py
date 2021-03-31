simbolos = '!"#$%&/()=?¡+*¨{[}]<>-_.:,;'
print("Ingrese un heterograma")
frase = input()
correcto = 'Si'
for i in frase:
    if (frase.count(i) > 1) and not(i in simbolos):
        correcto = 'No'
print(f'La Frase {correcto} era un Heterograma')
