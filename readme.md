script for generate sessions in securecrt:
1. turn the button "run script" and select python file ImportArbitraryDataFromFileToSecureCRTSessions
2. In the open window select your **to_secure.csv** file

generate **to_secure.csv** file for localhost connections:
1. in command line type "python localhost_telnet.py -start 5001 -stop 5020 -f lab/lab"
2. range of ports: `-start` port telnet connection, `-stop` port telnet connection
3. folder for sessions: `-f` _destfolder/destfolder_, default is root directory