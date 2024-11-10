individual = 7
Grupal = 5
Intermedio = 2
examen_final=6


Promedio_nota_individual=(individual*13.95)/20
Promedio_nota_grupal= (Grupal * 14.47)/20
Promedio_Prueba_intermedio= (Intermedio * 14.80)/20
promedio_Examen_final=(examen_final* 15.95)/20

PROMEDIO_GENERAL=Promedio_nota_individual + Promedio_nota_grupal + Promedio_Prueba_intermedio + promedio_Examen_final

print( "promeido en nota individual es: " + str(Promedio_nota_individual))
print( "promedio en nota grupal es: " + str(Promedio_nota_grupal))
print( "Promedio en exame intermedio es: " + str(Promedio_Prueba_intermedio))
print ( "Poreido en el examen final es: " + str(promedio_Examen_final))


if PROMEDIO_GENERAL > 13.55:
    print(PROMEDIO_GENERAL)
    print("FELICIDADES PASTES")
    
else:
    print("Estudia mmv te quedaste a suples")
    print(PROMEDIO_GENERAL)
   