#This script will create setup directories and fetch OAM Middleware home from OCI bucket.

source setenv.sh
sudo mkdir -p "$INSTALL_BASE"
sudo chown -R opc:opc "$INSTALL_ROOT"

cd $INSTALL_BASE
wget https://objectstorage.us-ashburn-1.oraclecloud.com/p/48noO3Jib5mtvFTOPP0hqzy6khatjbaXIoWVux9k7wg/n/intvravipati/b/OAMR2PS3/o/OAM.zip
unzip OAM.zip 
