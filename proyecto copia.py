from os import system 
system ("cls")
#Manejo de inversores

INVERSORES = {1065872355:'Jhorman Cardenas Chinchilla'}
INVERSIONES = {1065872355: 500000}
PROYECTO_PALMA = {1065872355: 'AGROPALMA S.A.S'}
PROYECTO_CACAO = {}
while True:
    inicio = input('Desea abrir Proyecto si/no -> ')
    if inicio == 'si':
        
        def nuevo_inversor():
            print("Proceso de Registro")
            llave = int(input("Ubique Documento del inversionista: "))
            valorN=input('Ingrese el nombre del inversionista: ')
            print('''En este momento se estan manejando Dos proyectos con un largo alcance de vision en manejo de tierras colombianas, 
            1. PROYECTO CACAO S.A.S 
            2. PROYEECTO AGROPALMA S.A.S''')
            proyecto = int(input('Seleccione uno de los proyectos 1/2 -> '))
            if proyecto == 1:
                
                EProyecto_cacao = 'CACAO S.A.S'
                print('El valor de aportacion como socio del proyecto CACAO S.A.S tiene un valor de $900.000 pesos.')
                inversion =  int(input('Ingrese el valor del la inversion dentro del proyecto -> '))
                costo_inversion = 900000
                valor_inversion = costo_inversion - inversion
                print(f'Su saldo pendiente para el cumplimiento de inversion es de ${valor_inversion} pesos')
                PROYECTO_CACAO[llave] = EProyecto_cacao
            elif proyecto == 2:
                EProyecto_palma= 'AGROPALMA S.A.S'
                print('el valor de aportacion como socio del proyecto AGROPALMA S.A.S es de $1.200.000 pesos')
                inversion = int(input("Ingrese el valor de la inversion dentro del proyecto -> "))
                costo_inversion = 1200000
                valor_inversion = costo_inversion - inversion
                print(f'Su saldo pendiente para el cumplimiento de inversion es de ${valor_inversion} pesos')
                PROYECTO_PALMA[llave] = EProyecto_palma
            INVERSORES[llave] = valorN
            INVERSIONES[llave] = inversion
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

            return
        print('SOCIOS ACTUALES')
        print(f'Nombres -> {INVERSORES}')
        print(f'Proyecto Palma -> {PROYECTO_PALMA}')
        print(f'Proyecto Cacao -> {PROYECTO_CACAO}')
        inicio = input("Ya esta registrado?, si lo es ubica 'INICIO' y si es nuevo ubica 'REGISTRAR'")
        if inicio == 'INICIO':
            login()
        elif inicio == 'REGISTRAR':
            nuevo_inversor()
    elif inicio == 'no':
        print("Programa cerrado")
        break