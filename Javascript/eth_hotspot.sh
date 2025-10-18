#!/usr/bin/sudo bash


>/etc/wpa_supplicant/wpa_supplicant.conf
echo 'ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev' >> /etc/wpa_supplicant/wpa_supplicant.conf
echo 'update_config=1' >> /etc/wpa_supplicant/wpa_supplicant.conf
echo 'country=IN' >> /etc/wpa_supplicant/wpa_supplicant.conf

>/etc/network/interfaces
echo 'source /etc/network/interfaces.d/*' >> /etc/network/interfaces


sudo apt install dnsmasq hostapd
sudo apt-get update
sudo apt install --fix-missing
sudo apt install dnsmasq hostapd
sudo systemctl stop dnsmasq
sudo systemctl stop hostapd



>/etc/dhcpcd.conf
echo 'hostname' >> /etc/dhcpcd.conf
echo 'clientid' >> /etc/dhcpcd.conf
echo 'persistent' >> /etc/dhcpcd.conf
echo 'option rapid_commit' >> /etc/dhcpcd.conf
echo 'option domain_name_servers, domain_name, domain_search, host_name' >> /etc/dhcpcd.conf
echo 'option classless_static_routes' >> /etc/dhcpcd.conf
echo 'option interface_mtu' >> /etc/dhcpcd.conf
echo 'require dhcp_server_identifier' >> /etc/dhcpcd.conf
echo 'slaac private' >> /etc/dhcpcd.conf



echo 'interface wlan0' >> /etc/dhcpcd.conf
echo '  static ip_address=192.168.4.1/24' >> /etc/dhcpcd.conf
echo '  nohook wpa_supplicant' >> /etc/dhcpcd.conf
sudo service dhcpcd restart
sudo mv /etc/dnsmasq.conf /etc/dnsmasq.conf.orig


> /etc/dnsmasq.conf
echo 'interface=wlan0' >> /etc/dnsmasq.conf
echo 'dhcp-range=192.168.4.2,192.168.4.20,255.255.255.0,24h' >> /etc/dnsmasq.conf

sudo systemctl start dnsmasq

>/etc/hostapd/hostapd.conf
echo 'country_code=US' >> /etc/hostapd/hostapd.conf
echo 'interface=wlan0' >> /etc/hostapd/hostapd.conf
echo 'ssid=HUSSMANN1' >> /etc/hostapd/hostapd.conf
echo 'channel=9' >> /etc/hostapd/hostapd.conf
echo 'auth_algs=1' >> /etc/hostapd/hostapd.conf
echo 'wpa=2' >> /etc/hostapd/hostapd.conf
echo 'wpa_passphrase=hussmann,123' >> /etc/hostapd/hostapd.conf
echo 'wpa_key_mgmt=WPA-PSK' >> /etc/hostapd/hostapd.conf
echo 'wpa_pairwise=TKIP CCMP' >> /etc/hostapd/hostapd.conf
echo 'rsn_pairwise=CCMP' >> /etc/hostapd/hostapd.conf

echo 'DAEMON_CONF="/etc/hostapd/hostapd.conf"' >> /etc/default/hostapd

sudo systemctl unmask hostapd
sudo systemctl enable hostapd
sudo systemctl start hostapd

echo 'net.ipv4.ip_forward=1' >> /etc/sysctl.conf

sudo apt install iptables
sudo iptables -t nat -A  POSTROUTING -o eth0 -j MASQUERADE

sudo apt install netfilter-persistent
sudo netfilter-persistent save


sudo iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE  
sudo iptables -A FORWARD -i eth0 -o wlan0 -m state --state RELATED,ESTABLISHED -j ACCEPT
sudo iptables -A FORWARD -i wlan0 -o eth0 -j ACCEPT
sudo sh -c "iptables-save > /etc/iptables.ipv4.nat"


>/etc/rc.local

echo "#!/bin/sh -e" >> /etc/rc.local

echo '_IP=$(hostname -I) || true' >> /etc/rc.local
echo 'if [ "$_IP" ]; then' >> /etc/rc.local
echo '  printf "My IP address is %s\n" "$_IP"' >> /etc/rc.local
echo 'fi' >> /etc/rc.local
echo 'iptables-restore < /etc/iptables.ipv4.nat ' >> /etc/rc.local
echo 'exit 0' >> /etc/rc.local

sudo reboot



