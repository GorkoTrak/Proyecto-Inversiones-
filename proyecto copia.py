from os import system 
system ("cls")
#RECOMENDACION -> ABRIR CODIGO HA TRAVEZ DEL PYHON NO VISUAL POR ERROR DE VISUAL AL EN LA EJECUCION 

#Manejo de inversores
INVERSORES = {1065872355:'Jhorman Cardenas Chinchilla'}
INVERSORES_VERIFICADOS_cacao = {}
INVERSORES_VERIFICADOS_palma = {}
INVERSIONES = {1065872355: 500000}
PROYECTO_PALMA = {1065872355: 'AGROPALMA S.A.S'}
PROYECTO_CACAO = {}    
def nuevo_inversor():
            while True:
                try:
                    print("Proceso de Registro")
                    llave = int(input("Ubique Documento del inversionista: "))
                    valorN=input('Ingrese el nombre del inversionista: '); system('cls')
                    break
                except: 
                    print('Error en el digito')
            print('''En este momento se estan manejando Dos proyectos con un largo alcance de vision en manejo de tierras colombianas: 
1. PROYECTO CACAO S.A.S 
2. PROYEECTO AGROPALMA S.A.S
AVISO -> Solo puede realizar maximo DOS consignaciones, Inscripcion y Cancelacion de inversion.''')
            proyecto = str(input('Seleccione uno de los proyectos 1/2 -> ')); system('cls')
            if proyecto == '1':
                EProyecto_cacao = 'CACAO S.A.S'
                print('El valor de aportacion como socio del proyecto CACAO S.A.S tiene un valor de $900.000 pesos.')
                while True:
                    while True:
                        try:
                            inversion =  int(input('Ingrese el valor del la inversion dentro del proyecto -> '))
                            break
                        except:
                            print('Error en el digito')
                    costo_inversion = 900000
                    if inversion>0 and inversion<costo_inversion:
                        valor_inversion = costo_inversion - inversion
                        print(f'Su saldo pendiente para el cumplimiento de inversion es de ${valor_inversion} pesos')
                        PROYECTO_CACAO[llave] = EProyecto_cacao
                        INVERSIONES[llave] = inversion
                        INVERSORES[llave] = valorN
                        print('')
                        enter = str(input('oprima una tecla cualquiera para continuar: ')); system('cls')
                        if enter:
                            system('cls')
                        break
                    elif inversion>costo_inversion:
                        print('usted ingreso una cantidad mayor')
                    elif inversion<0:
                        print('usted ingreso una cantidad negativa')
                    elif inversion == costo_inversion:
                        if len(INVERSORES_VERIFICADOS_cacao.keys())<3:
                            INVERSORES_VERIFICADOS_cacao[llave] = EProyecto_cacao
                            print('Usted a cancelado el pago De inversion completo'); print('Bienvenido al proyecto CACAO S.A.S')
                            PROYECTO_CACAO[llave] = EProyecto_cacao
                            INVERSIONES[llave] = inversion
                            INVERSORES[llave] = valorN
                        elif len(INVERSORES_VERIFICADOS_cacao.keys()) >=3:
                            print('Ya se ha alcanzado el maximo de inversores para este proyecto')
                            INVERSORES[llave] = valorN
                            del(INVERSORES[llave])
                        enter = str(input('oprima una tecla cualquiera para continuar: ')); system('cls')
                        if enter:
                            system('cls')
                        break
                    
            elif proyecto == '2':
                EProyecto_palma= 'AGROPALMA S.A.S'
                print('el valor de aportacion como socio del proyecto AGROPALMA S.A.S es de $1.200.000 pesos')
                while True:
                    while True:
                        try:
                            inversion = int(input("Ingrese el valor de la inversion dentro del proyecto -> "))
                            break
                        except:
                            print('error en el digito')
                    if inversion>0 and inversion<1200000:
                        costo_inversion = 1200000
                        valor_inversion = costo_inversion - inversion
                        print(f'Su saldo pendiente para el cumplimiento de inversion es de ${valor_inversion} pesos')
                        PROYECTO_PALMA[llave] = EProyecto_palma
                        INVERSIONES[llave] = inversion
                        INVERSORES[llave] = valorN
                        print('')
                        enter = str(input('oprima una tecla cualquiera para continuar: ')); system('cls')
                        if enter:
                            system('cls')
                        break
                    elif inversion>1200000:
                        print('usted ingreso una cantidad mayor')
                    elif inversion<0:
                        print('usted ingreso una cantidad negativa')
                    elif inversion == 1200000:
                        if len(INVERSORES_VERIFICADOS_palma.keys()) < 2:
                            INVERSORES_VERIFICADOS_palma[llave] = EProyecto_palma
                            print('Usted a cancelado el pago De inversion completo'); print('Bienvenido al proyecto AGROPALMA S.A.S')
                            PROYECTO_PALMA[llave] = EProyecto_palma
                            INVERSIONES[llave] = inversion
                            INVERSORES[llave] = valorN
                        elif len(INVERSORES_VERIFICADOS_palma.keys()) >=2:
                            INVERSORES[llave] = valorN
                            print('Ya se ha alcanzado el maximo de inversores para este proyecto')
                            del(INVERSORES[llave])
                        enter = str(input('oprima una tecla cualquiera para continuar: ')); system('cls')
                        if enter:
                            system('cls')
                        break
            return
def login():
    while True:
        try:
            usuarios = int(input('Dijite su documento de identidad: '))
            try:
                if INVERSORES_VERIFICADOS_cacao[usuarios]:
                    print('USTED ES SOCIO EN EL PROYECTO CACAO S.A.S')
                    break
            except:
                print('')
            try:
                if INVERSORES_VERIFICADOS_palma[usuarios]:
                    print('USTED ES SOCIO EN EL PROYECTO AGROPALMA S.A.S')
                    break
            except:
                print('')
            if INVERSORES[usuarios]:
                print('Bienvenido')
                print(f'Nombre -> {INVERSORES[usuarios]}')
                print(f'Inversion realizada -> {INVERSIONES[usuarios]}')
                try :
                    print(f'Pertenece a proyecto-> {PROYECTO_PALMA[usuarios]}')
                except:
                    print("")
                try :
                    print(f'Pertenece a proyecto -> {PROYECTO_CACAO[usuarios]}')
                    
                except:
                    print('')
                while True:
                    conocer_saldo = str(input('Desea conocer su saldo pendiente? si/no: ')).lower()
                    if conocer_saldo == 'si':
                        try:
                            if PROYECTO_CACAO[usuarios]:
                                saldo_pendiente = 900000 -INVERSIONES[usuarios]
                                print(f'su saldo pendiente es de ${saldo_pendiente}')
                                while True:
                                    opcion_inversion = str(input('Desea cancelar su saldo? si/no: ')).lower(); print('''''')
                                    if opcion_inversion == 'si':
                                        while True:
                                            try:
                                                if len(INVERSORES_VERIFICADOS_cacao.keys()) >= 3:
                                                    print('El limite maximo de INVERSORES en PROYECTO CACA S.A.S FUE ALCANZADO')
                                                    retiro = str(input('Ingrese su CUENTA BANCARIA para la debolucion de su dinero: '))
                                                    if retiro:
                                                        print('Muchas Gracias por participar en esta EMPRESA DE INVERSIONES'); print('Su consignacion legara a su ceunta en las proximas horas')
                                                        del(INVERSORES[usuarios])
                                                    break
                                            except:
                                                print('')
                                            try:
                                                nueva_inversion = int(input('Ingrese el valor de la nueva inversion: '))
                                                if nueva_inversion == saldo_pendiente:
                                                    fin_saldo = nueva_inversion + INVERSIONES[usuarios]
                                                    print('Ya ust ha acumulado el total de la inversion')
                                                    print('Bienvenido al PROYECTO <33')
                                                    INVERSIONES[usuarios] = fin_saldo
                                                    INVERSORES_VERIFICADOS_cacao[usuarios] = PROYECTO_CACAO[usuarios]
                                                    
                                                    break
                                                else:
                                                    print('Error, el nuevo saldo no es suficiente')
                                            except:
                                                print('Error en el digito')
                                    elif opcion_inversion == 'no':
                                        print('')
                                        break
                                    
                                    else:
                                        print('Error, dijito incorrecto')
                                    break
                                break
                            else:   
                                print('')
                            
                        except:
                            print('')
                            
                        try:
                            if PROYECTO_PALMA[usuarios]:
                                saldo_pendiente = 1200000 - INVERSIONES[usuarios]
                                print(f'su saldo pendiente es de {saldo_pendiente}')
                                while True:
                                    opcion_inversion = input('Desea cancelar su saldo? si/no: ')
                                    if opcion_inversion == 'si':
                                        while True:
                                            try:
                                                if len(INVERSORES_VERIFICADOS_palma.keys()) >= 2:
                                                    print('El limite maximo de INVERSORES en PROYECTO AGROPALMA S.A.S FUE ALCANZADO')
                                                    retiro = str(input('Ingrese su CUENTA BANCARIA para la debolucion de su dinero: '))
                                                    if retiro:
                                                        print('Muchas Gracias por participar en esta EMPRESA DE INVERSIONES'); print('Su consignacion legara a su ceunta en las proximas horas')
                                                        del(INVERSORES[usuarios])
                                                    break
                                            except:
                                                print('')
                                            try:
                                                nueva_inversion = int(input('Ingresar el valor de la nueva inversion: '))
                                                if nueva_inversion == saldo_pendiente:
                                                        fin_saldo = nueva_inversion + INVERSIONES[usuarios]
                                                        print('ya ust ha acumulado el total de la inversion'); print('Bienvenido al proyecto <33')
                                                        INVERSIONES[usuarios] = fin_saldo
                                                        INVERSORES_VERIFICADOS_palma[usuarios] = PROYECTO_PALMA[usuarios]
                                                        
                                                        break
                                                else:
                                                    print('error, el nuevo saldo no es sufciente')
                                            except:
                                                print('Error en el digito')
                                    elif opcion_inversion == 'no':
                                        print('')
                                        break
                                    else:
                                        print('error, dijito incorrecto')    
                                    break 
                                break        
                            else:
                                print('')
                        except:
                            print('')
                    elif conocer_saldo == 'no':
                        print('')
                        break
                    else:
                        print('Error, dijito incorrecto')
                break
            break 
        except:
            print('Error, dijito equivocado')
        
    return
while True:
    inicio = input('Desea abrir Proyecto si/no -> ').lower(); system('cls')
    if inicio == 'si':
            while True:
                if inicio == 'si':
                    print('')
                    print("*"*60)
                    break
            
            print(''''''); print('inversores actuales')
            print('------------------------')
            for key,value in INVERSORES.items():
                print(key, ' -> ', value) 
            print('------------------------')

            print(''''''); print('inversiones actuales')
            print('------------------------')
            for key,value in INVERSIONES.items():
                print(key, ' -> ', value) 
            print('------------------------')

            print(''''''); print('Maximo SOCIOS PROYECTO AGROPALMA S.A.S -> 2')

            print(''''''); print('inversores verificados de palma')
            print('------------------------')
            for key,value in INVERSORES_VERIFICADOS_palma.items():
                print(key, ' -> ', value)
            print('------------------------');print('''''')
            print(''''''); print('Maximo SOCIOS PROYECTO CACAO S.A.S -> 3')
            print(''''''); print('inversores verificados de cacao')
            print('------------------------')

            for key,value in INVERSORES_VERIFICADOS_cacao.items():
                print(key, ' -> ', value)
            print('------------------------');print('''''')
            
            print(f'cantidad de inversores en proyecto CACAO -> ')
            print(len(PROYECTO_CACAO.keys()))
            
            print(f'cantidad de inversores en proyecto PALMA -> ')
            print(len(PROYECTO_PALMA.keys()))
            while True:
                inicio1 = str(input("Ya esta registrado?, si lo es ubica 'INICIO' y si es nuevo ubica 'REGISTRAR': ")).lower(); system('cls')
                if inicio1 == 'inicio':
                    login()
                    break
                elif inicio1 == 'registrar':
                    nuevo_inversor()
                    break
                else:
                    print('''Error en el digito
                    
                ''')
    elif inicio == 'no':
        print("Programa cerrado")
        break
    else:
        print('Error en el digito')