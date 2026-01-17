from scapy.all import sniff, IP, TCP, UDP

def packet_analyzer(packet):
    if IP in packet:
        print("\n[+] Packet Captured")
        print("Source IP:", packet[IP].src)
        print("Destination IP:", packet[IP].dst)

        if TCP in packet:
            print("Protocol: TCP")
            print("Source Port:", packet[TCP].sport)
            print("Destination Port:", packet[TCP].dport)

        elif UDP in packet:
            print("Protocol: UDP")
            print("Source Port:", packet[UDP].sport)
            print("Destination Port:", packet[UDP].dport)

def start_sniffer():
    print("Starting Network Sniffer...")
    sniff(prn=packet_analyzer, store=False)

if __name__ == "__main__":
    start_sniffer()
