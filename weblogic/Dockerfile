FROM oracle/java:7

MAINTAINER Kiran Thakkar <kiran.thakkar@oracle.com>

ENV ORACLE_HOME=/u01/oracle \
    USER_MEM_ARGS="-Djava.security.egd=file:/dev/./urandom" \
    PATH=$PATH:/usr/java/default/bin:/u01/oracle/oracle_common/common/bin

RUN mkdir -p /u01 && \
    chmod a+xr /u01 && \
    useradd -b /u01 -d /u01/oracle -m -s /bin/bash oracle

ENV WLS_PKG=wls1036_generic.jar

COPY $WLS_PKG silent.xml /u01/
RUN chown oracle:oracle -R /u01

USER oracle
RUN $JAVA_HOME/bin/java -jar /u01/$WLS_PKG -mode=silent -silent_xml=/u01/silent.xml && \
    rm /u01/$WLS_PKG /u01/silent.xml

WORKDIR $ORACLE_HOME

# Define default command to start bash. 
CMD ["bash"]
