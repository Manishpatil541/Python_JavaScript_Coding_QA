#!/usr/bin/sudo bash

sudo systemctl stop hostapd
>/etc/dhcpcd.conf

#source /etc/network/interfaces.d/*
>/etc/network/interfaces
echo 'auto lo' >> /etc/network/interfaces
echo 'iface lo inet loopback' >> /etc/network/interfaces
echo 'auto eth0' >> /etc/network/interfaces
echo 'iface eth0 inet dhcp' >> /etc/network/interfaces
echo 'auto wlan0' >> /etc/network/interfaces
echo 'allow-hotplug wlan0' >> /etc/network/interfaces
echo 'iface wlan0 inet dhcp' >> /etc/network/interfaces
echo '  wpa-conf /etc/wpa_supplicant/wpa_supplicant.conf' >> /etc/network/interfaces





#>/etc/wpa_supplicant/wpa_supplicant.conf
#echo 'ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev' >> /etc/wpa_supplicant/wpa_supplicant.conf
#echo 'update_config=1' >> /etc/wpa_supplicant/wpa_supplicant.conf
#echo 'country=IN' >> /etc/wpa_supplicant/wpa_supplicant.conf

sudo reboot
