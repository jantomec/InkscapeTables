@echo off
PowerShell -Command "Compress-Archive -Path 'tables.inx', 'tables.py' -DestinationPath 'tables.zip'"
echo Files have been compressed into tables.zip
