# Project 2 Instructions

## POX Controller commands

```
sudo ./pox.py openflow.of_01 --port=6633 pox.forwarding.l2_learning pox.forwarding.L3Firewall --l2config="l2firewall.config" --l3config="l3firewall.config"
```

```
sudo ./pox.py openflow.of_01 --port=6655 pox.forwarding.l2_learning pox.forwarding.L3Firewall --l2config="l2firewall.config" --l3config="l3firewall.config"
```

## Containernet commands

```
sudo python containernet.py
```

### set IP of containers

```
h1 ifconfig h1-eth0 10.0.2.10
h1 ifconfig h1-eth1 192.168.2.10
h2 ifconfig h2-eth0 10.0.2.20
h3 ifconfig h3-eth0 192.168.2.30
h4 ifconfig h4-eth0 192.168.2.40
```




## Validation commands

### Add new rule to l3config file for blocking ICMP traffic from source IP 10.0.2.10 and destination IP 10.0.2.20.
- h1 ping h2


### Add new rule to l3config file for blocking ICMP traffic from source IP 192.168.2.10 and destination IP 10.0.2.10.
- h2 ping h1


### Add new rule to l3config file for blocking HTTP traffic from source IP 10.0.2.20.

- xterm h1
- curl 10.0.2.20                      % on h1

### Add new rule to l2config file for blocking traffic from MAC address 00:00:00:00:00:03 to destination MAC address 00:00:00:00:00:04.

- xterm h3 h4
- tcpdump                             % on h4
- ping 192.168.2.40                   % on h3

### Add new rule to l3config file for blocking tcp traffic from 192.168.2.10 to 192.168.2.30

- xterm h1 h3
- tcpdump                                             % on h3
- hping3 --scan 1000-2000 -S 192.168.2.40             % on h1

### Add new rule to l3config file for blocking udp traffic from 192.168.2.10 to 192.168.2.40

- xterm h1 h4
- tcpdump                             % on h4
- hping3 --udp 192.168.2.40           % on h1
