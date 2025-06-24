README - Mini pare-feu Python (iptables)

Ce projet est un mini pare-feu personnel développé en Python. Il permet d'interagir avec iptables, l'outil de filtrage réseau sous Linux, afin de :

Bloquer des adresses IP indésirables

Bloquer des ports TCP sensibles

Lister les règles de filtrage en place

Réinitialiser toutes les règles INPUT

Ce script est conçu pour l'apprentissage de la cybersécurité, de l'’administration réseau et des bases de la défense périmétrique.

🔧 Exécution

Ce script nécessite les droits administrateur (sudo) :

➕ Ajouter une règle de blocage d’IP :

sudo python3 firewall.py --block-ip 1.2.3.4

➕ Ajouter une règle de blocage de port TCP :

sudo python3 firewall.py --block-port 22

📋 Lister les règles de filtrage :

sudo python3 firewall.py --list-rules

🛉 Réinitialiser les règles INPUT (tout supprimer) :

sudo python3 firewall.py --reset

🎓 Compétence acquise 

Utiliser iptables pour filtrer le trafic réseau

Interagir avec des outils système via Python (subprocess)

Comprendre la logique de défense host-based firewall

Automatiser des tâches d’administration réseau

💻 Pré-requis

Linux (avec iptables installé)

Python 3

Accès root (utilisation de sudo requise)

📌 À propos

Ce mini-projet a été réalisé par Lyes HADBI, étudiant passionné par la cybersécurité et l’infrastructure réseau.