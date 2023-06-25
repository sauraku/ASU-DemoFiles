sudo mn --topo=single,4 --controller=remote,port=6655 -i 192.168.2.0/24 --switch=ovsk --mac


py h1.setIP('10.0.1.10/16')
py h2.setIP('10.0.2.20/16')
py h3.setIP('10.0.3.30/16')
py h4.setIP('10.0.4.40/16')


sudo ./pox.py openflow.of_01 --port=6655 pox.forwarding.l3_learning pox.forwarding.L3Firewall --l2config="l2firewall.config" --l3config="l3firewall.config"


hping3 10.0.4.40 -c 10000 -S --flood -a 10.0.10.1
ovs-ofctl dump-flows s1

