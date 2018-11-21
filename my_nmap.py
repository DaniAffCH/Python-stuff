import nmap
import argparse
__author__ = "DaniAffCH"
nm = nmap.PortScanner()
parser = argparse.ArgumentParser(description = "nmap scanner by "+__author__)
parser.add_argument("-c", "--comando" , type=str , help="Operazione consentite: scan | versione | info | servizi | statistiche | hosts | test-appartenenza | protocolli | porte-aperte | porte-precise")
parser.add_argument("-i", "--ip", type=str, default="192.168.0.1" ,help="Inserisci un ip o un range con /")
parser.add_argument("-p", "--porta", type=str, default="1-1028", help="Inserisci una porta o un range con -")
args = parser.parse_args()
scanner = nm.scan(args.ip, args.porta, '-v --version-all')
if args.comando == "scan":
    print(scanner)
if args.comando == "versione":
    result = nm.nmap_version()
    print (result)
elif args.comando == "info":
    result = nm.scaninfo()
    print (result)
elif args.comando == "servizi":
    result = nm.csv()
    print (result)
elif args.comando == "statistiche":
    result = nm.scanstats()
    print (result)
elif args.comando == "hosts":
    result = nm.all_hosts()
    print (result)
elif args.comando == "test-appartenenza":
    ip = input("Ip da verificare : ")
    function = lambda ip: nm[ip].state()
    print (function(ip))
elif args.comando == "protocolli":
    ip = input("ip per scansionare i protocolli (se vuoi scansionare il router premi invio): ")
    if ip == "":
        ip = args.ip
    function = lambda ip: nm[ip].all_protocols()
    print (function(ip))
elif args.comando == "porte-aperte":
    ip = input("ip per scansionare le porte aperte (se vuoi scansionare il router premi invio): ")
    if ip == "":
        ip = args.ip
    while True:
        protocol = input("Vuoi utilizzare il protocollo tcp o udf [tcp/udf]? ")
        if protocol == "tcp" or protocol == "udf":
            break
    try:
        function = lambda ip, protocol: nm[ip][protocol].keys()
        print (function(ip, protocol))
    except:
        print ("Errore!")
elif args.comando == "porte-precise":
    while True:
        port = input("Inserisci la porta da scansionare: ")
        port = int(port)
        if port >= 0 and port <= 1028:
            break
    ip = input("ip per scansionare le porte aperte (se vuoi scansionare il router premi invio): ")
    if ip == "":
        ip = args.ip
    function = lambda ip, port: [ip].has_tcp(port)
    print(function(ip, port))