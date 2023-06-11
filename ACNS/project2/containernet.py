from mininet.net import Mininet
from mininet.node import OVSSwitch, RemoteController
from mininet.cli import CLI
from mininet.log import info, setLogLevel
setLogLevel("info")


net = Mininet(controller=RemoteController, switch=OVSSwitch, waitConnected=True)

c1 = net.addController( 'c1', port=6633)
c2 = net.addController( 'c2', port=6655)

s1 = net.addSwitch( 's1' )
s2 = net.addSwitch( 's2' )

h1 = net.addHost('h1', mac='00:00:00:00:00:01')
h2 = net.addHost('h2', mac='00:00:00:00:00:02')
h3 = net.addHost('h3', mac='00:00:00:00:00:03')
h4 = net.addHost('h4', mac='00:00:00:00:00:04')

net.addLink(s1, h1)
net.addLink(s1, h2)
net.addLink(s2, h3)
net.addLink(s2, h4)
net.addLink(s2, h1)

net.build()

c1.start()
c2.start()
s1.start([c1])
s2.start([c2])


CLI(net)