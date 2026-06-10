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


    return nombre, codigo, monto_base, cruz


def calcular_monto(monto_base, montoA_L, montoM_Z, montoU, codigo):
    letra = codigo[0]

    if "A" <= letra <= "L":
        monto_final = monto_base + montoA_L
    elif letra == "U":
        monto_final = monto_base + montoU
    else:
        monto_final = monto_base + montoM_Z

    if codigo[4] == ' ' and codigo[5] == ' ':
        porcentaje = 0
    elif codigo[5] == ' ':
        porcentaje = int(codigo[4])
    else:
        porcentaje = int(codigo[4] + codigo[5])

    monto_final += monto_final * porcentaje / 100

    return round(monto_final, 2)

def recorrer(promedio):
    m = open("tratamientos.txt")
    cant_altacomplejidad_mayoralpromedio = 0

    for linea in m:
        if linea[-1] == '\n':
            linea = linea[:-1]

        if linea[0] == '#':
            montoA_L, montoM_Z, montoU = procesar_linea_numeral(linea)

        else:
            nombre, codigo, monto_base, cruz = procesar_linea(linea)
            monto_final = calcular_monto(monto_base, montoA_L, montoM_Z, montoU, codigo)

            if cruz == "X" and monto_final > promedio:
                cant_altacomplejidad_mayoralpromedio +=1

    return cant_altacomplejidad_mayoralpromedio



def principal():
    m = open("tratamientos.txt")


    r1 = r2 = r3 = r4 = r5 = r6 = r7= r10 = suma_montos = cant_altacomplejidad = 0

    # sirve para r7
    suma_importe = 0
    cant_pacientes = 0

    # sirve r8 y r9
    r9 = None

    for linea in m:
        if linea[-1] == '\n':
            linea = linea[0:-1]

        if linea[0] == '#':
            montoA_L, montoM_Z, montoU = procesar_linea_numeral(linea)

        else:
            nombre, codigo, monto_base, cruz = procesar_linea(linea)

            #Cantidad de personas tratadas
            r1 += 1

            letra = codigo[0]

            global numero
            numero = int(codigo[1] + codigo[2])

            if letra == 'A':
                r2 += 1
            elif letra == 'B':
                r3 += 1
            elif letra == 'C':
                r4 += 1
            elif letra == 'E':
                r5 += 1
            elif letra == 'P':
                r6 += 1

            monto_final = calcular_monto(monto_base,montoA_L,montoM_Z,montoU,codigo)

            # r7
            if letra == 'S' or (letra == 'T' and numero <= 98):
                suma_importe += monto_final
                cant_pacientes += 1

            # r8 y r9
            if letra != 'U':
                if r9 is None or monto_final > r9:
                    r9 = monto_final
                    r8 = nombre

            #r10
            suma_montos += monto_final

            if cruz == 'X':
                cant_altacomplejidad += 1

    m.close()


    if cant_pacientes != 0:
        r7 = round(suma_importe / cant_pacientes, 2)

    if r1 != 0:
        promedio = suma_montos / r1


    cant_altacomplejidad_mayoralpromedio = recorrer(promedio)

    if cant_altacomplejidad != 0:
     r10 = cant_altacomplejidad_mayoralpromedio * 100 / cant_altacomplejidad


    print('(r1) - Cantidad de tratamientos cargados:', r1)
    print('(r2) - Cantidad de tratamientos "A":', r2)
    print('(r3) - Cantidad de tratamientos "B":', r3)
    print('(r4) - Cantidad de tratamientos "C":', r4)
    print('(r5) - Cantidad de tratamientos "E":', r5)
    print('(r6) - Cantidad de tratamientos "P":', r6)
    print('(r7) - Importe final promedio (capítulo 19):', r7)
    print('(r8) - Paciente (no tipo "U") que pagó el mayor importe final:', r8)
    print('(r9) - Mayor importe pagado por ese paciente:', r9)
    print('(r10)- Porcentaje de tratamientos de alta complejidad con coste mayor al promedio:', r10)

principal()