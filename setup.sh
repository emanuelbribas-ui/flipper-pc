echo "Configurando antena..."
sudo ip link set wlan0 down
sudo iw dev wlan0 set type monitor
sudo ip link set wlan0 up
echo "Modo monitor ativado em wlan0."
