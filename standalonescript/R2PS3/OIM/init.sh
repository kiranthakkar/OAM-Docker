#This script will create setup directories and fetch OIM Middleware home from OCI bucket.

source setenv.sh
#sudo mkdir -p "$INSTALL_BASE"
#sudo chown -R opc:opc "$INSTALL_ROOT"

cd $INSTALL_BASE
wget https://objectstorage.us-ashburn-1.oraclecloud.com/p/sGFXObVCkBY5cRmU42JOw0wvE8PrdIVHklBqbyXaTW8/n/intvravipati/b/OAMR2PS3/o/RCU.tar.gz
cd $MW_HOME
#wget https://objectstorage.us-ashburn-1.oraclecloud.com/p/tif6AkxyXiXPZ-F5dUtTGctVdUeFWGS1xwb1pLPjvUI/n/intvravipati/b/OAMR2PS3/o/OIM.tar.gz
#tar -xvf OIM.tar.gz
tar -xvf RCU.tar.gz
