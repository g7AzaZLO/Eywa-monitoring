# Install 
### 1 step
Download bot
```
sudo git clone https://github.com/g7AzaZLO/Eywa-monitoring.git
```
![image](https://github.com/g7AzaZLO/eywa-monitoring/assets/59707245/264673fb-437c-4043-a905-1548affc682d)
### 2 step
Go to settings and insert your token from the Telegram bot
```
cd eywa-monitoring/settings
nano config.py
```
To save the file, press successively<br />
ctrl + x<br />
y<br />
enter<br />
<br />
![image](https://github.com/g7AzaZLO/eywa-monitoring/assets/59707245/c32a19bc-208a-43a6-a541-0494b5c681f5)

### 3 step
Install screen
```
sudo apt install screen
```
Start a new session for the bot
```
screen -S eywa_monitoring
```
Start the bot
```
cd ..
pip3 install -r requirements.txt
python app.py
```
![image](https://github.com/g7AzaZLO/eywa-monitoring/assets/59707245/d641d9af-0f36-4b4e-ba75-dd183ee8cee1)

To leave a session in the background, press successively <br />
ctrl + a<br />
D<br />

### 4 step
Open and /start your bot in Telegram<br />

![image](https://github.com/g7AzaZLO/Eywa-monitoring/assets/59707245/4dc7ffd2-3fd8-4705-8abd-fa5015d10ec2)

# Function
### Check synchronization
Allows you to check node synchronization in real time
![image](https://github.com/g7AzaZLO/eywa-monitoring/assets/59707245/81eef59a-e8f6-4b05-b944-171ad3d43050)
### Check node hits in epochs
Allows you to check which epochs your node has fallen into. If the epoch number is in brackets (15), then your node is in that epoch
![image](https://github.com/g7AzaZLO/eywa-monitoring/assets/59707245/09f526b7-d728-4aed-8042-fc2640eabf01)
### Start monitoring EYWA synchronization
Allows you to start monitoring node synchronization in real time. By standard, monitoring checks synchronization every 60 seconds (TTS parameter in config.py). If the node is not in FULLY_SYNCED status, the bot sends you a notification message
![image](https://github.com/g7AzaZLO/eywa-monitoring/assets/59707245/9d4fd0a7-fd94-4cce-9083-e22904de8e49)
### Stop monitoring EYWA synchronization
Stops node synchronization monitoring
![image](https://github.com/g7AzaZLO/eywa-monitoring/assets/59707245/950aebd4-12f1-4cac-bc26-d7f6020dab55)
### Check current epoch
Allows you to find out what era you are living in and when it began
![image](https://github.com/g7AzaZLO/eywa-monitoring/assets/59707245/e07cdf48-a327-4e20-af33-2193ba243c12)
### Check bridge version
Allows you to find out what version of bridge is installed on your node
![image](https://github.com/g7AzaZLO/eywa-monitoring/assets/59707245/be06828a-ef97-4352-bdc6-2cd2995c4040)

### The bot consumes about 100 megabytes of RAM and less than 1% of the CPU
