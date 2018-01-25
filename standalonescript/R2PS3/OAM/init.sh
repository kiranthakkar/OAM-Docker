#This script will create setup directories and fetch OAM Middleware home from OCI bucket.

source setenv.sh
sudo mkdir -p "$INSTALL_BASE"
sudo chown -R opc:opc "$INSTALL_ROOT"

cd $INSTALL_BASE
wget https://objectstorage.us-ashburn-1.oraclecloud.com/p/sGFXObVCkBY5cRmU42JOw0wvE8PrdIVHklBqbyXaTW8/n/intvravipati/b/OAMR2PS3/o/RCU.tar.gz 
wget https://objectstorage.us-ashburn-1.oraclecloud.com/p/tif6AkxyXiXPZ-F5dUtTGctVdUeFWGS1xwb1pLPjvUI/n/intvravipati/b/OAMR2PS3/o/OAM.tar.gz
tar -xvf OAM.tar.gz
tar -xvf RCU.tar.gz
