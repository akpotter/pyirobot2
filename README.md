# Pyirobot2
Unoffical API about irobot Roomba 980 since firmware v2.0.0-34

## Installation
TODO: 

Not yet.
Need more reverse.

## Usage
1. **Get The ROBOT_ID AND ROOMBA IP FROM LAN :**

```bash
python irobotmcs_from_lan.py
```
   
   Result might be :  

```bash
    Looking for robots...
    
    {"ver":"2","hostname":"Roomba-XXXXXXXXXXXXXXXX","robotname":"MyRoomba","ip":"192.168.1.2","mac":"XX:XX:XX:XX:XX:XX","sw":"v2.0.0-34","sku":"R98XXXX","nc":0,"proto":"mqtt"}
```
hostname will be your ROBOT_ID. 
(You can also check your ROBOT_ID from your phone app)

## History
2017/02 create repository.

## License
MIT
