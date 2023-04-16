from os import system 
system ("cls")
#Manejo de inversores

INVERSORES = {1065872355:'Jhorman Cardenas Chinchilla'}
INVERSIONES = {1065872355: 500000}
PROYECTO_PALMA = {1065872355: 'AGROPALMA S.A.S'}
PROYECTO_CACAO = {}
while True: 
    inicio = input('Desea abrir Proyecto si/no -> '); system('cls')
    if inicio == 'si':
        
        def nuevo_inversor():
            print("Proceso de Registro")
            llave = int(input("Ubique Documento del inversionista: "))
            valorN=input('Ingrese el nombre del inversionista: '); system('cls')
            print('''En este momento se estan manejando Dos proyectos con un largo alcance de vision en manejo de tierras colombianas, 
            1. PROYECTO CACAO S.A.S 
            2. PROYEECTO AGROPALMA S.A.S''')
            proyecto = int(input('Seleccione uno de los proyectos 1/2 -> ')); system('cls')
            if proyecto == 1:
                if len(PROYECTO_CACAO.keys()) <= 2:
                    EProyecto_cacao = 'CACAO S.A.S'
                    print('El valor de aportacion como socio del proyecto CACAO S.A.S tiene un valor de $900.000 pesos.')
                    inversion =  int(input('Ingrese el valor del la inversion dentro del proyecto -> '))
                    costo_inversion = 900000
                    valor_inversion = costo_inversion - inversion
                    print(f'Su saldo pendiente para el cumplimiento de inversion es de ${valor_inversion} pesos')
                    PROYECTO_CACAO[llave] = EProyecto_cacao
                    INVERSIONES[llave] = inversion
                else:
                    print('Cantidad de inversores maxima'); system('cls')
                        
            elif proyecto == 2:
                if len(PROYECTO_PALMA.keys()) <= 2:
                    EProyecto_palma= 'AGROPALMA S.A.S'
                    print('el valor de aportacion como socio del proyecto AGROPALMA S.A.S es de $1.200.000 pesos')
                    inversion = int(input("Ingrese el valor de la inversion dentro del proyecto -> "))
                    costo_inversion = 1200000
                    valor_inversion = costo_inversion - inversion
                    print(f'Su saldo pendiente para el cumplimiento de inversion es de ${valor_inversion} pesos')
                    
                    PROYECTO_PALMA[llave] = EProyecto_palma
                    INVERSIONES[llave] = inversion
                    
                else:
                    print('Cantidad de inversores maxima alcanzada'); system('cls')
                        
            INVERSORES[llave] = valorN
            
            print(INVERSIONES)
            print(INVERSORES)
            return

        def login():
            usuarios = int(input('Dijite su documento de identidad: '))
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
                conocer_saldo = input('Desea conocer su saldo pendiente? si/no: ')
                if conocer_saldo == 'si':
                    try:
                        if PROYECTO_CACAO[usuarios]:
                            saldo_pendiente = 900000 -INVERSIONES[usuarios]
                            print(f'su saldo pendiente es de ${saldo_pendiente}')
                            while True:
                                opcion_inversion = input('Desea cancelar su saldo? si/no: ')
                                if opcion_inversion == 'si':
                                    nueva_inversion = int(input('Ingrese el valor de la nueva inversion: '))
                                    if nueva_inversion == saldo_pendiente:
                                        fin_saldo = nueva_inversion + INVERSIONES[usuarios]
                                        print('Ya ust ha acumulado el total de la inversion')
                                        print('Bienvenido al PROYECTO <33')
                                        break
                                    else:
                                        print('Error, el nuevo saldo no es suficiente')
                                    
                                else:
                                    print('')
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
                                    nueva_inversion = int(input('Ingresar el valor de la nueva inversion: '))
                                    if nueva_inversion == saldo_pendiente:
                                            fin_saldo = nueva_inversion + INVERSIONES[usuarios]
                                            print('ya ust ha acumulado el total de la inversion')
                                            ('Bienvenido al proyecto <33')
                                            break
                                    else:
                                        print('error, el nuevo saldo no es sufciente')
                                else:
                                    print('')        
                        else:
                            print('')
                    except:
                        print('')
            return
        print('SOCIOS ACTUALES')
        print(f'Nombres -> {INVERSORES}')
        print(f'Proyecto Palma -> {PROYECTO_PALMA}')
        print(f'Proyecto Cacao -> {PROYECTO_CACAO}')
        print(f'cantidad de inversores en proyecto CACAO -> ')
        print(len(PROYECTO_CACAO.keys()))
        print(f'cantidad de inversores en proyecto PALMA -> ')
        print(len(PROYECTO_PALMA.keys()))
        inicio = input("Ya esta registrado?, si lo es ubica 'INICIO' y si es nuevo ubica 'REGISTRAR'"); system('cls')
    
        if inicio == 'INICIO':
            login()
        elif inicio == 'REGISTRAR':
            nuevo_inversor()
    elif inicio == 'no':
        print("Programa cerrado")
        break