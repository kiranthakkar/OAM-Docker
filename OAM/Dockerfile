FROM oracle/weblogic:11g

MAINTAINER Kiran Thakkar <kiran.thakkar@oracle.com>

ENV ORACLE_HOME=/u01/oracle/middleware/Oracle_OAM \
    MIDDLEWARE_HOME=/u01/oracle/middleware \
    OAM_ZIP1=ofm_iam_generic_11.1.2.3.0_disk1_1of3.zip \
    OAM_ZIP2=ofm_iam_generic_11.1.2.3.0_disk1_2of3.zip \
    OAM_ZIP3=ofm_iam_generic_11.1.2.3.0_disk1_3of3.zip

COPY $OAM_ZIP1 $OAM_ZIP2 $OAM_ZIP3 oraInst.loc responsefile /u01/

USER root

RUN yum -y install unzip oracle-rdbms-server-11gR2-preinstall.x86_64 hostname && \
    rm -rf /var/cache/yum && \
    chown oracle:oracle -R /u01

USER oracle
RUN cd /u01 && unzip $OAM_ZIP1 && unzip $OAM_ZIP2 && unzip $OAM_ZIP3 && cd - && \
    /u01/Disk1/runInstaller -waitforcompletion -silent -jreLoc $JAVA_HOME -responseFile /u01/responsefile -invPtrLoc /u01/oraInst.loc ORACLE_HOME=$ORACLE_HOME

RUN rm -rf /u01/Disk* /u01/$OAM_ZIP1 /u01/$OAM_ZIP2 /u01/$OAM_ZIP3 /u01/oraInst.loc /u01/responsefile

WORKDIR $ORACLE_HOME

# Define default command to start bash. 
CMD ["bash"]
