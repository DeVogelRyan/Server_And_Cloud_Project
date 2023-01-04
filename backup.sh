#!bin/bash

MYSQL_POD=`kubectl get pods --no-headers -o custom-columns=":metadata.name" | grep mysql`
echo $MYSQL_POD

YEAR=`date +%Y`
MONTH=`date +%m`
DAY=`date +%d`
HOUR=`date +%H`

mkdir -p $YEAR/$MONTH/$DAY/$HOUR

kubectl exec $MYSQL_POD -- mysqldump -u root -proot mydata > $YEAR/$MONTH/$DAY/$HOUR/backup.sql