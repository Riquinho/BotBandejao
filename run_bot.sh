#!/bin/bash
LOG='/home/joao/scripts/bandejao/bot.log'
echo "" >> ${LOG}
echo "" >> ${LOG}
echo "######################################################################" >> ${LOG}
echo "Starting bot at $(date --rfc-3339=seconds)" >> ${LOG}
export PATH='/home/joao/bin:/home/joao/.local/bin:/opt/java/jdk/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games'
echo "Going to the script folder" >> ${LOG}
cd /home/joao/scripts/bandejao
echo "Scheduling your lunch!" >> ${LOG}
/usr/bin/python bot.py >> ${LOG}
echo "Scheduled. Have a nice meal!" >> ${LOG}
echo "######################################################################" >> ${LOG}
