#!/bin/bash
#!/usr/bin/env python

DAEMONS="\
    mysqld \
    cloudera-quickstart-init"

if [ -e /var/lib/cloudera-quickstart/.kerberos ]; then
    DAEMONS="${DAEMONS} \
        krb5kdc \
        kadmin"
fi

if [ -e /var/lib/cloudera-quickstart/.cloudera-manager ]; then
    DAEMONS="${DAEMONS} \
        cloudera-scm-server-db \
        cloudera-scb-server \
        cloudera-scm-server-db"
else
    DAEMONS="${DAEMONS} \
        zookeeper-server \
        hadoop-hdfs-datanode \
        hadoop-hdfs-journalnode \
        hadoop-hdfs-namenode \
        hadoop-hdfs-secondarynamenode \
        hadoop-httpfs \
        hadoop-mapreduce-historyserver \
        hadoop-yarn-nodemanager \
        hadoop-yarn-resourcemanager \
        sqoop2-server \
"
fi

for daemon in ${DAEMONS}; do
    sudo service ${daemon} start
done


echo "***** Start twitterstream  *****"
python twitterstream.py $TIME $ACCESS_TOKEN_KEY $ACCESS_TOKEN_SECRET $CONSUMER_KEY $CONSUMER_SECRET > twitts.json
hdfs dfs -put twitts.json /user/cloudera/twitts.json
yarn jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar -files mapper_final.py,reducer_final.py,State.tsv,AFINN-111.txt -mapper mapper_final.py -reducer reducer_final.py -input hdfs:///user/cloudera/twitts.json -output hdfs:///user/cloudera/output

echo "***** Exporting to db  *****"
sqoop export --connect jdbc:mysql://172.28.0.2:3306/resultados --username root --password admin --table tweets -m 1 --export-dir /user/cloudera/output/ --input-lines-terminated-by '\t'

echo "***** End of twitterstream  *****"

echo "Start Terminal"
bash