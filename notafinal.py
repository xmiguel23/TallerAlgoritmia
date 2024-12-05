notamin = float(input("Ingresa la Nota mínima para aprobar la Materia: "))
notatuya = float(input("Ingresa la nota que saco el estudiante y la cual deseas comrpobar: "))

if notatuya < notamin: 
    print ("El Estudiante ha Reprobado la Materia")
else:
    print ("El Estudiante ha Aprobado la Materia")
