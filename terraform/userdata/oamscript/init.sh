sudo mkdir -p "$INSTALL_BASE"
sudo chown -R opc:opc "$INSTALL_ROOT"

cd $INSTALL_BASE
wget https://objectstorage.us-ashburn-1.oraclecloud.com/p/DNtmL1-reuj69ecQkyxbmeLVeNA6S8CmhZVj6GTKRTs/n/intvravipati/b/OAMR2PS3/o/RCU.tar.gz 
wget https://objectstorage.us-ashburn-1.oraclecloud.com/p/zA_dx9VFURL4z5Qf7FWe7es_vbDn-wJ1CKm5W-K1xfk/n/intvravipati/b/OAMR2PS3/o/OAM.tar.gz
tar -xvf OAM.tar.gz
tar -xvf RCU.tar.gz
