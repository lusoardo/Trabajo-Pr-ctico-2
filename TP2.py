
def procesar_linea_numeral(linea):
    montoA_L = int(linea[2:8])
    montoM_Z = int(linea[8:14])
    montoU = int(linea[14:20])

    return montoA_L, montoM_Z, montoU

def procesar_linea(linea):
  nombre = linea[:25]
  codigo = linea[25:31]
  monto_base = int(linea[31:39])
  if len(linea) == 40:
      cruz = linea[39]
  else:
      cruz = 'N'

  return nombre,codigo,monto_base,cruz

def calcular_monto(monto_base,montoA_L,montoM_Z,montoU,codigo):
    global numero
    global letra
    letra = codigo[0]
    numero = int(codigo[1] + codigo[2])

    r2 = r3 = r4 = r5 = r6 = 0
    if letra == "A":
        r2 = r2 + 1
    elif letra == "B":
        r3 = r3 + 1
    elif letra == "C":
        r4 = r4 + 1
    elif letra == "E":
        r5 = r5 + 1
    elif letra == "P":
        r6 = r6 + 1

    if "A" <= letra <= "L":
        monto_final = monto_base + montoA_L
    elif letra == "U":
        monto_final = monto_base + montoU
    else:
        monto_final = monto_base + montoM_Z

    # Porcentaje
    if len(codigo) == 3:
        porcentaje = 0
    elif len(codigo) == 5:
        porcentaje = int(codigo[4])
    else:
        porcentaje = int(codigo[4] + codigo[5])

    monto_final =  round((monto_final + monto_final * porcentaje / 100),2)

    return monto_final, r2, r3, r4, r5, r6

def capitulo(monto_final):
    suma_importe = 0
    cant_pacientes = 0
    if letra == "S" or (letra == "T" and numero <= 98):
        suma_importe += monto_final
        cant_pacientes += 1

    return suma_importe, cant_pacientes

def mayor(nombre,monto_final):
    may = None
    paciente_mayor = ''

    if letra != 'U':
        if may is None or may > monto_final:
            may = monto_final
            paciente_mayor = nombre

    return paciente_mayor,may

def principal():
    m = open('tratamientos.txt')
    for linea in m:
        if linea [-1] == "\n":
            linea = linea[0:-1]

        if linea [0] == '#':
            montoA_L, montoM_Z, montoU = procesar_linea_numeral(linea)
            print(montoA_L)
            print(montoM_Z)
            print(montoU)
        else:
            nombre, codigo, monto_base, cruz = procesar_linea(linea)
            print(nombre, codigo, monto_base, cruz)
            monto_final,r2,r3,r4,r5,r6 = calcular_monto(monto_base,montoA_L,montoM_Z,montoU,codigo)
            suma_importe, cant_pacientes = capitulo(monto_final)
            r8,r9 = mayor(nombre,monto_final)


    m.close()
    if cant_pacientes != 0:
     r7 = round(suma_importe / cant_pacientes,2)

    print('(r1) - Cantidad de tratamientos cargados:', r1)
    print('(r2) - Cantidad de tratamientos "A":', r2)
    print('(r3) - Cantidad de tratamientos "B":', r3)
    print('(r4) - Cantidad de tratamientos "C":', r4)
    print('(r5) - Cantidad de tratamientos "E":', r5)
    print('(r6) - Cantidad de tratamientos "P":', r6)
    print('(r7) – Importe final promedio (capítulo 19):', r7)
    print('(r8) – Paciente (no tipo "U") que pagó el mayor importe final:', r8)
    print('(r9) - Mayor importe pagado por ese paciente):', r9)
    print('(r10)- Porcentaje de tratamientos de alta complejidad con coste mayor al promedio:', r10)


principal()