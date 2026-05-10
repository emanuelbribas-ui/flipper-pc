Step 1: System PrerequisitesBefore running the Python script, you need the system-level tools that handle the heavy lifting.On Arch Linux:Bashsudo pacman -S git python-pip macchanger mdk4 aircrack-ng bluez bluez-utils
On Kali Linux:Bashsudo apt update
sudo apt install git python3-pip macchanger mdk4 aircrack-ng bluez bluez-utils
Step 2: Clone and Setup EnvironmentOpen your terminal and run these commands to prepare your folder:
Bash# Clone
git clone https://github.com/emanuelbribas-ui/flipper-pc/
cd nebula-flipper

# Give execution permission to the setup script
chmod +x setup.sh

# Install Python dependencies
pip install -r requirements.txt --break-system-packages
Step 3: Hardware Initialization
Your Realtek antenna needs to be in Monitor Mode to sniff and inject packets. Run your setup script:Bashsudo ./setup.sh
Note: If you don't have a setup.sh yet, use: sudo airmon-ng start wlan0Step 4: Launching the ToolSince the tool interacts directly with the Network Interface Card (NIC) and Bluetooth stack, it must be run with root privileges.Bashsudo python flipper.py
3. Usage Best Practices for "Mysthic-Fox"FeatureRequirementTipWiFi DeauthMonitor ModeUse airodump-ng first to find the target's MAC.BT L2PingBluetooth ServiceRun sudo systemctl start bluetooth before attacking.Stealth ModemacchangerUse option [3] in the menu to randomize your MAC frequently.LogsPersistent StorageCheck nebula_ghost.log to see your past successful "raids".4. Updating the ToolWhenever you add more functions or thousands of lines of code to your repo, update your local machine using:Bashgit pull origin main
