#This script will create the domain.

source setenv.sh

WLST_SCRIPT=$ORACLE_HOME/common/bin/wlst.sh

$WLST_SCRIPT createDomain.py
