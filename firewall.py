import subprocess
import argparse

# -----------------------------
# Ajouter une règle de blocage d'IP
# -----------------------------
def block_ip(ip):
    print(f"🔒 Blocage de l'adresse IP : {ip}")
    subprocess.run(["sudo", "iptables", "-A", "INPUT", "-s", ip, "-j", "DROP"])

# -----------------------------
# Ajouter une règle de blocage de port
# -----------------------------
def block_port(port):
    print(f"🔒 Blocage du port : {port}")
    subprocess.run(["sudo", "iptables", "-A", "INPUT", "-p", "tcp", "--dport", str(port), "-j", "DROP"])

# -----------------------------
# Lister les règles actuelles
# -----------------------------
def list_rules():
    print("📋 Règles actuelles :")
    subprocess.run(["sudo", "iptables", "-L", "INPUT", "--line-numbers"])

# -----------------------------
# Réinitialiser les règles INPUT
# -----------------------------
def reset_rules():
    print("♻️  Réinitialisation des règles INPUT...")
    subprocess.run(["sudo", "iptables", "-F", "INPUT"])
    print("✅ Toutes les règles ont été supprimées.")

# -----------------------------
# Fonction principale
# -----------------------------
def main():
    parser = argparse.ArgumentParser(description="Mini pare-feu en Python (iptables)")
    parser.add_argument("--block-ip", help="Bloquer une adresse IP")
    parser.add_argument("--block-port", type=int, help="Bloquer un port TCP")
    parser.add_argument("--list-rules", action="store_true", help="Lister les règles en place")
    parser.add_argument("--reset", action="store_true", help="Réinitialiser toutes les règles INPUT")
    args = parser.parse_args()

    if args.block_ip:
        block_ip(args.block_ip)
    elif args.block_port:
        block_port(args.block_port)
    elif args.list_rules:
        list_rules()
    elif args.reset:
        reset_rules()
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
