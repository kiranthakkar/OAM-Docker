# Set Environment
export ENV="DEV"
export INSTALL_ROOT="/u01"
export INSTALL_BASE=${INSTALL_ROOT}/app
export OUD_MWHOME=${INSTALL_BASE}/oracle/oud/middleware
export OUD_HOME=${OUD_MWHOME}/Oracle_OUD
export OUD_INSTANCE="${OUD_HOME}/instances/oud1"
export INSTANCE_NAME=../../../../../..${OUD_INSTANCE}
export OUD_ROOTPASSWORD="Oracle123"
export OUD_BASEDN="dc=acme,dc=com"
export OUD_HOSTNAME=`hostname`
