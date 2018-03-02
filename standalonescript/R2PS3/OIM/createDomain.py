import os

print os.environ.get("DOMAIN_TEMPLATE")
DOMAIN_TEMPLATE=os.environ.get("DOMAIN_TEMPLATE")
DOMAIN_DIR=os.environ.get("OIM_DOMAIN_DIR")
MW_HOME=os.environ.get("MW_HOME")
OPSS_TEMPLATE=os.environ.get("ORACLE_HOME") + r'/common/templates/applications/oracle.opss_11.1.1.3.0_template.jar'
JRF_TEMPLATE=os.environ.get("MW_HOME") + r'/oracle_common/common/templates/applications/jrf_template_11.1.1.jar'
OPSS_SCHEMA=os.environ.get("OIM_SCHEMA_PREFIX") + "_OPSS"

machine='AdminNode'


readTemplate(DOMAIN_TEMPLATE)
cd('Security/base_domain/User/weblogic')
cmo.setPassword(os.environ.get("DOMAIN_PASSWORD"))
# Please set password here before using this script, e.g. cmo.setPassword('value')


cd('/')
set("ProductionModeEnabled", "true")

cd('Servers/AdminServer')
set('ListenAddress','')
set('ListenPort', 7001)

create('AdminServer','SSL')
cd('SSL/AdminServer')
set('Enabled', 'True')
set('ListenPort', 7002)

## Create Machine
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





setOption('OverwriteDomain', 'true')
writeDomain(DOMAIN_DIR)
closeTemplate()





readDomain(DOMAIN_DIR)
print 'Applying JRF Extension Template...'
cd('/')
setOption('AppDir',DOMAIN_DIR)
addTemplate(JRF_TEMPLATE)
applyJRF('AdminServer',DOMAIN_DIR, true)
updateDomain()
closeDomain()

#opss Data Source
readDomain(DOMAIN_DIR)
print 'Applying OPSS Template...'
addTemplate(OPSS_TEMPLATE)
cd('/JDBCConnectionPool/opss-DBDS')
set("Properties", "user="+OPSS_SCHEMA)
cd('/JDBCSystemResource/opss-DBDS/JdbcResource/opss-DBDS/JDBCDriverParams/NO_NAME_0')
cmo.setDriverName('oracle.jdbc.OracleDriver')
cmo.setPasswordEncrypted(os.environ.get("DOMAIN_PASSWORD"))
cmo.setUrl(os.environ.get("DB_URL"))

updateDomain()
closeDomain()










exit()

