sudo mn --topo=single,4 --controller=remote,port=6655 -i 192.168.2.10 --switch=ovsk --mac


h1 ifconfig h1-eth0 10.0.2.10
h2 ifconfig h2-eth0 10.0.2.20
h3 ifconfig h3-eth0 10.0.2.30
h4 ifconfig h4-eth0 10.0.2.40


h1 ifconfig h1-eth0 192.168.2.10
h2 ifconfig h2-eth0 192.168.2.20
h3 ifconfig h3-eth0 192.168.2.30
h4 ifconfig h4-eth0 192.168.2.40

sudo ./pox.py openflow.of_01 --port=6655 pox.forwarding.l3_learning pox.forwarding.L3Firewall --l2config="l2firewall.config" --l3config="l3firewall.config"


hping3 -S 10.0.2.40 -a 10.0.10.1 -c 3
hping3 10.0.2.40 -c 10000 -S --flood --rand-source -V