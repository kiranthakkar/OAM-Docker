FROM oracle/oam:R2PS3

MAINTAINER Kiran Thakkar <kiran.thakkar@oracle.com>

ENV ORACLE_HOME=/u01/oracle/middleware/Oracle_OAM \
    MIDDLEWARE_HOME=/u01/oracle/middleware \
    DOMAIN_NAME=OAMDomain \
    DOMAIN_DIR=/u01/oracle/middleware/user_projects/domains \
    ADMIN_USERNAME=weblogic \
    ADMIN_PASSWORD=***** \
    DB_HOST=10.0.0.14 \
    DB_PORT=1521 \
    DB_SERVICE=$DB_SERVICE \
    DB_USER=SYS \
    DB_PASSWORD=***** \
    SCHEMA_PREFIX=DockerOAM \
    SCHEMA_PASSWORD=***** \
    RCU_ZIP=ofm_rcu_linux_11.1.1.9.0_64_disk1_1of1.zip \
    RCU_BINARY=/u01/rcuHome/bin/rcu \
    ADMIN_HOST=$ADMIN_HOST \
    ADMIN_PORT=7001 \
    OAM_PORT=14100 \
    OAM_CLUSTER_NAME=oam_cluster \
    WLST_SCRIPT=/u01/oracle/middleware/Oracle_OAM/common/bin/wlst.sh

ENV CONNECTION_STRING=$DB_HOST:$DB_PORT/$DB_SERVICE \
    CONFIG_BINARY=$ORACLE_HOME/common/bin/config.sh
COPY $RCU_ZIP pwd.txt createDomain.py createOAMDomain.py /u01/

RUN cd /u01 && unzip $RCU_ZIP 

RUN $RCU_BINARY -silent -dropRepository -databaseType ORACLE -connectString $CONNECTION_STRING -dbUser sys -dbRole sysdba -selectDependentsForComponents true -schemaPrefix $SCHEMA_PREFIX -component OAM -component OMSM -f < /u01/pwd.txt

RUN $RCU_BINARY -silent -createRepository -databaseType ORACLE -connectString $CONNECTION_STRING -dbUser sys -dbRole sysdba -useSamePasswordForAllSchemaUsers true -selectDependentsForComponents truei -schemaPrefix $SCHEMA_PREFIX -component OAM -component OMSM -f < /u01/pwd.txt

RUN rm -rf /u01/$RCU_ZIP /u01/pwd.txt /u01/rcuHome

#RUN $CONFIG_BINARY -waitforcompletion -silent -jreLoc $JAVA_HOME -invPtrLoc /u01/oraInst.loc 

RUN $WLST_SCRIPT /u01/createDomain.py

RUN $WLST_SCRIPT /u01/createOAMDomain.py

RUN $WLST_SCRIPT $ORACLE_HOME/common/tools/configureSecurityStore.py -d $DOMAIN_DIR/$DOMAIN_NAME -c IAM -p 'QWaszx12##' -m create

RUN rm -rf /u01/createDomain.py /u01/createOAMDomain.py

WORKDIR $ORACLE_HOME

# Define default command to start bash.
CMD ["bash"]
