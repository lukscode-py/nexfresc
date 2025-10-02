from os import system
try:
  import prov_for_vix # Importa funcoes da ferramenta!
  from pyfiglet import figlet_format # Importa bibioteca criar titulos inicial
  from rich import print # Importa rich
  from simple_term_menu import TerminalMenu
  import nmap3
except ImportError as e:
    print(f'Faltou bibioteca {e}')
    if input(f'baixar bibiote necessario? [Y/n]? ').lower() == "y":
        system("pip3 install pyfiglet simple-term-menu rich python-nmap && apt install -y nmap")
        system('cls')
        system('clear')
        print('Reinicie o programa!')
    exit()


# Variaveis Gerais:
prov = prov_for_vix


def restart_title():
    system('cls')
    system('clear')
    print(f'[red]{figlet_format("NEX FRESC", font="slant")}[/red]')

start = True
while start:
    restart_title()
    match TerminalMenu(['Scanner Rodeado wifi - Somente se disponivel', 'Scanner ip - Sem root', 'Scanner ports for IP - Depende', 'Sair']).show()+1:
        case 1:
            ip = input('Qual IP do seu rodeador? [Para saber,basta ir nas config de wi-fi do aparelho!] > ')
            print(f'RESULTADO FOR JSON:\n\n{prov.scan_portas(ip)}')
            input('\n\n\n Voltar < Tela inicial > ')
        
        case 2:
            ip = input('Qual IP para scanner? ')
            print(f'RESULTADO FOR JSON:\n\n{prov.scan_ip(ip)}')
            input('\n\n\n Volta < Tela inicial > ')

        case 3:
            ip = input('Qual IP para scanner portas abertas? ')
            print(f'RESULTADO FOR JSON:\n\n{prov.scan_portas(ip)}')
            input('\n\n\n Volta < Tela inicial > ')

        case 4:
            start = False