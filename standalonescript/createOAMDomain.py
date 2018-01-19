import os

DOMAIN_DIR=os.environ.get("OAM_DOMAIN_DIR")
OAM_TEMPLATE=os.environ.get("ORACLE_HOME") + "/common/templates/applications/oracle.oam_ds_mobile_11.1.2.3_template.jar"
DB_PASSWORD=os.environ.get("DB_PASSWORD")
DB_URL=os.environ.get("DB_URL")
DB_DRIVER=os.environ.get("DB_DRIVER")
OAM_SCHEMA=os.environ.get("OAM_SCHEMA_PREFIX") + "_OAM"
MDS_SCHEMA=os.environ.get("OAM_SCHEMA_PREFIX") + "_MDS"
OPSS_SCHEMA=os.environ.get("OAM_SCHEMA_PREFIX") + "_OPSS"
OMSM_SCHEMA=os.environ.get("OAM_SCHEMA_PREFIX") + "_OMSM"

readDomain(DOMAIN_DIR)
addTemplate(OAM_TEMPLATE)

machine='AdminNode'
oamCluster='oam_cluster'
oamServer='oam_server1'
omsmServer='omsm_server1'
policyServer='oam_policy_mgr1'

cd('/')
create(machine, 'Machine')
cd('Machine/' + machine)
create(machine, 'NodeManager')
cd('NodeManager/' + machine)
set('NMType','SSL')
set('ListenAddress','localhost')
set('ListenPort',5658)
cd('/Servers/AdminServer')
set('Machine',machine)

cd('/')
create(oamCluster, 'Cluster')

cd('/')
#create(oamServer, 'Server')
cd('Server/' + oamServer)
set('ListenPort',14100)
set('Machine',machine)
set('Cluster',oamCluster)

cd('/')
#create(omsmServer, 'Server')
cd('Server/' + omsmServer)
set('ListenPort',14180)
set('Machine',machine)

cd('/')
#create(policyServer, 'Server')
cd('Server/' + policyServer)
set('ListenPort',14150)
set('Machine',machine)

cd('/')
#create('mds-oam', 'JDBCSystemResource')
cd('JDBCSystemResource/mds-oam/JdbcResource/mds-oam')
dataSourceParams=create('dataSourceParams','JDBCDataSourceParams')
cd('JDBCDataSourceParams/NO_NAME_0')
print "Setting JNDI Names: "
set('JNDIName','jdbc/mds/oam')
cd('/JDBCSystemResource/mds-oam/JdbcResource/mds-oam')
create('myJdbcDriverParams','JDBCDriverParams')
cd('JDBCDriverParams/NO_NAME_0')
set('DriverName',DB_DRIVER)
set('URL',DB_URL)
set('PasswordEncrypted',DB_PASSWORD)
create('myProps','Properties')
cd('Properties/NO_NAME_0')
#create('user', 'Property')
cd('Property/user')
cmo.setValue(MDS_SCHEMA)

cd('/JDBCSystemResources/mds-oam/JdbcResource/mds-oam/JDBCDriverParams/NO_NAME_0')
create('myProps','Properties')
cd('Properties/NO_NAME_0')
#create('SendStreamAsBlob', 'Property')
cd('Property/SendStreamAsBlob')
cmo.setValue('true')

cd('/JDBCSystemResources/mds-oam/JdbcResource/mds-oam/JDBCDriverParams/NO_NAME_0')
create('myProps','Properties')
cd('Properties/NO_NAME_0')
#create('oracle.net.CONNECT_TIMEOUT', 'Property')
cd('Property/oracle.net.CONNECT_TIMEOUT')
cmo.setValue('10000')

cd('/')
#create('mds-owsm', 'JDBCSystemResource')
cd('JDBCSystemResource/mds-owsm/JdbcResource/mds-owsm')
dataSourceParams=create('dataSourceParams','JDBCDataSourceParams')
cd('JDBCDataSourceParams/NO_NAME_0')
print "Setting JNDI Names: "
set('JNDIName','jdbc/mds/owsm')
cd('/JDBCSystemResource/mds-owsm/JdbcResource/mds-owsm')
create('myJdbcDriverParams','JDBCDriverParams')
cd('JDBCDriverParams/NO_NAME_0')
set('DriverName',DB_DRIVER)
set('URL',DB_URL)
set('PasswordEncrypted',DB_PASSWORD)
create('myProps','Properties')
cd('Properties/NO_NAME_0')
#create('user', 'Property')
cd('Property/user')
cmo.setValue(MDS_SCHEMA)

cd('/JDBCSystemResources/mds-owsm/JdbcResource/mds-owsm/JDBCDriverParams/NO_NAME_0')
create('myProps','Properties')
cd('Properties/NO_NAME_0')
#create('SendStreamAsBlob', 'Property')
cd('Property/SendStreamAsBlob')
cmo.setValue('true')

cd('/JDBCSystemResources/mds-owsm/JdbcResource/mds-owsm/JDBCDriverParams/NO_NAME_0')
create('myProps','Properties')
cd('Properties/NO_NAME_0')
#create('oracle.net.CONNECT_TIMEOUT', 'Property')
cd('Property/oracle.net.CONNECT_TIMEOUT')
cmo.setValue('10000')

cd('/')
#create('oamDS', 'JDBCSystemResource')
cd('JDBCSystemResource/oamDS/JdbcResource/oamDS')
dataSourceParams=create('dataSourceParams','JDBCDataSourceParams')
cd('JDBCDataSourceParams/NO_NAME_0')
print "Setting JNDI Names: "
set('JNDIName','jdbc/oamds')
cd('/JDBCSystemResource/oamDS/JdbcResource/oamDS')
create('myJdbcDriverParams','JDBCDriverParams')
cd('JDBCDriverParams/NO_NAME_0')
set('DriverName',DB_DRIVER)
set('URL',DB_URL)
set('PasswordEncrypted',DB_PASSWORD)
create('myProps','Properties')
cd('Properties/NO_NAME_0')
#create('user', 'Property')
cd('Property/user')
cmo.setValue(OAM_SCHEMA)

cd('/JDBCSystemResources/oamDS/JdbcResource/oamDS/JDBCDriverParams/NO_NAME_0')
create('myProps','Properties')
cd('Properties/NO_NAME_0')
create('SendStreamAsBlob', 'Property')
cd('Property/SendStreamAsBlob')
cmo.setValue('true')

cd('/JDBCSystemResources/oamDS/JdbcResource/oamDS/JDBCDriverParams/NO_NAME_0')
create('myProps','Properties')
cd('Properties/NO_NAME_0')
#create('oracle.net.CONNECT_TIMEOUT', 'Property')
cd('Property/oracle.net.CONNECT_TIMEOUT')
cmo.setValue('10000')

cd('/')
#create('omsm-ds', 'JDBCSystemResource')
cd('JDBCSystemResource/omsm-ds/JdbcResource/omsm-ds')
dataSourceParams=create('dataSourceParams','JDBCDataSourceParams')
cd('JDBCDataSourceParams/NO_NAME_0')
print "Setting JNDI Names: "
set('JNDIName','jdbc/omsm-ds')
cd('/JDBCSystemResource/omsm-ds/JdbcResource/omsm-ds')
create('myJdbcDriverParams','JDBCDriverParams')
cd('JDBCDriverParams/NO_NAME_0')
set('DriverName',DB_DRIVER)
set('URL',DB_URL)
set('PasswordEncrypted',DB_PASSWORD)
create('myProps','Properties')
cd('Properties/NO_NAME_0')
#create('user', 'Property')
cd('Property/user')
cmo.setValue(OMSM_SCHEMA)

cd('/JDBCSystemResources/omsm-ds/JdbcResource/omsm-ds/JDBCDriverParams/NO_NAME_0')
create('myProps','Properties')
cd('Properties/NO_NAME_0')
#create('oracle.net.CONNECT_TIMEOUT', 'Property')
cd('Property/oracle.net.CONNECT_TIMEOUT')
cmo.setValue('10000')

cd('/')
#create('opss-DBDS', 'JDBCSystemResource')
cd('JDBCSystemResource/opss-DBDS/JdbcResource/opss-DBDS')
dataSourceParams=create('dataSourceParams','JDBCDataSourceParams')
cd('JDBCDataSourceParams/NO_NAME_0')
print "Setting JNDI Names: "
set('JNDIName','jdbc/OPSSDBDS')
cd('/JDBCSystemResource/opss-DBDS/JdbcResource/opss-DBDS')
create('myJdbcDriverParams','JDBCDriverParams')
cd('JDBCDriverParams/NO_NAME_0')
set('DriverName',DB_DRIVER)
set('URL',DB_URL)
set('PasswordEncrypted',DB_PASSWORD)
create('myProps','Properties')
cd('Properties/NO_NAME_0')
#create('user', 'Property')
cd('Property/user')
cmo.setValue(OPSS_SCHEMA)

cd('/')
assign('JDBCSystemResource', 'mds-oam', 'Target', policyServer)

assign('JDBCSystemResource', 'mds-owsm', 'Target', omsmServer)

assign('JDBCSystemResource', 'oamDS', 'Target', 'AdminServer')
assign('JDBCSystemResource', 'oamDS', 'Target', oamCluster)
assign('JDBCSystemResource', 'oamDS', 'Target', policyServer)

assign('JDBCSystemResource', 'omsm-ds', 'Target', omsmServer)
assign('JDBCSystemResource', 'omsm-ds', 'Target', policyServer)

assign('JDBCSystemResource', 'opss-DBDS', 'Target', 'AdminServer')
assign('JDBCSystemResource', 'opss-DBDS', 'Target', oamCluster)
assign('JDBCSystemResource', 'opss-DBDS', 'Target', policyServer)
assign('JDBCSystemResource', 'opss-DBDS', 'Target', omsmServer)

updateDomain()

exit()

