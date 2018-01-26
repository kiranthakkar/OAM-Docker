#Setup environment,

export VERSION=R2PS3
export ENV=DEV
export JAVA_HOME=/u01/app/Oracle/java/jdk1.7.0_80
export PATH=$JAVA_HOME/bin:$PATH
export INSTALL_ROOT=/u01
export INSTALL_BASE=$INSTALL_ROOT/app
export MW_HOME=$INSTALL_BASE/Oracle/Middleware
export ORACLE_HOME=$MW_HOME/Oracle_OIM
export OUD_HOME=$MW_HOME/Oracle_OUD
export DOMAIN_HOME=$MW_HOME/user_projects/domains
export OAM_DOMAIN=OAMDomain
export OIM_DOMAIN=OIMDomain
export OAM_DOMAIN_DIR=$DOMAIN_HOME/$OAM_DOMAIN
export OIM_DOMAIN_DIR=$DOMAIN_HOME/$OIM_DOMAIN
export DOMAIN_TEMPLATE=$MW_HOME/wlserver_10.3/common/templates/domains/wls.jar
WLST_SCRIPT=$ORACLE_HOME/common/bin/wlst.sh
export DOMAIN_USERNAME=weblogic
export DOMAIN_PASSWORD=Oracle1234

export DB_HOST=10.0.0.14
export DB_PORT=1521
export DB_SERVICE=IDMR2PS3_iad1d2.sub07121717490.test.oraclevcn.com
export DB_CONNECTION_STRING=$DB_HOST:$DB_PORT/$DB_SERVICE
export DB_URL=jdbc:oracle:thin:@$DB_CONNECTION_STRING
export DB_DRIVER=oracle.jdbc.OracleDriver
export DB_USER=SYS
export DB_PASSWORD=QWaszx12##
export OAM_SCHEMA_PREFIX=OAM$VERSION$ENV
export OIM_SCHEMA_PREFIX=OIM$VERSION$ENV
export SCHEMA_PASSWORD=QWaszx12##
