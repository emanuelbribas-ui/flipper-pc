
### 1. Overview
This project transforms a PC equipped with a **Realtek RTL8192CU** antenna (like the TP-Link WN8200ND) into a powerful hardware auditing device, similar to a Flipper Zero, but with superior processing power and range.
### 2. Key Features
 * **WiFi Raider:** Full spectrum scanning (2.4GHz) to identify hidden SSIDs and signal strength (PWR).
 * **WiFi Deauth:** Disconnects specific devices (like loud smart speakers) from the network using logic injection.
 * **Bluetooth Flooder:** Overloads Bluetooth stacks (L2CAP) to interrupt unstable or noisy audio connections.
 * **Arch/Kali Optimized:** Custom drivers and scripts designed for high-performance Linux distros.
### 3. Quick Setup Guide
#### **For Arch Linux (Native)**
```bash
# 1. Install dependencies
sudo pacman -S git python-scapy aircrack-ng dkms linux-headers

# 2. Install Realtek Monitor Mode drivers (AUR)
yay -S 8192cu-dkms

# 3. Setup Interface
chmod +x setup.sh
./setup.sh

```
#### **For Kali Linux (Windows/WSL2)**
 1. **On Windows:** Use usbipd to attach the Realtek USB antenna to the WSL2 instance.
 2. **In Kali:**
   ```bash
   sudo apt update && sudo apt install python3-scapy aircrack-ng
   sudo airmon-ng check kill
   
   ```
### 4. Project Structure
 * flipper.py: The main Python engine (No-nonsense code).
 * setup.sh: Automated monitor mode toggle.
 * requirements.txt: Necessary Python libraries (scapy, flask, etc.).
 * README.md: Project documentation and usage.
### 5. Deployment (GitHub)
```bash
git init
git add .
git commit -m "Nebula Studios: Flipper Core deployed"
git branch -M main
git remote add origin https://github.com/emanuelbribas-ui/flipper-pc
git push -u origin main

```
> **Notice:** This tool is for educational purposes and authorized security auditing only.


