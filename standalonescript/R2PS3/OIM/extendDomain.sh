#This script will extend the domain.

source setenv.sh

WLST_SCRIPT=$ORACLE_HOME/common/bin/wlst.sh

$WLST_SCRIPT createBIPDomain.py
$WLST_SCRIPT createSOADomain.py
$WLST_SCRIPT createOIMDomain.py

$WLST_SCRIPT $ORACLE_HOME/common/tools/configureSecurityStore.py -d $OIM_DOMAIN_DIR -c IAM -p $DB_PASSWORD -m create
