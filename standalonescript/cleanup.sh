source setenv.sh

RCU_SCRIPT=$INSTALL_BASE/Oracle/RCU/rcuHome/bin/rcu

#Creating password file
echo $DB_PASSWORD > pwd.txt
echo $SCHEMA_PASSWORD >> pwd.txt

If the script failed and if you are running it again, we need to delete the schema first. Uncheck below script execution if you need to delete the schema.
./rcu -silent -dropRepository -databaseType ORACLE -connectString $CONNECTION_STRING -dbUser sys -dbRole sysdba -selectDependentsForComponents true -schemaPrefix $SCHEMA_PREFIX -component OAM -component OMSM -f < /u01/pwd.txt

rm -f pwd.txt

sudo rm -rf /u01
