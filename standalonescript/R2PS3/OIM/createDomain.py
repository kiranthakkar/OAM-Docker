import os

print os.environ.get("DOMAIN_TEMPLATE")
DOMAIN_TEMPLATE=os.environ.get("DOMAIN_TEMPLATE")
DOMAIN_DIR=os.environ.get("OAM_DOMAIN_DIR")
readTemplate(DOMAIN_TEMPLATE)

cd('Servers/AdminServer')
set('ListenAddress','')
set('ListenPort', 7001)

create('AdminServer','SSL')
cd('SSL/AdminServer')
set('Enabled', 'True')
set('ListenPort', 7002)


cd('/')
cd('Security/base_domain/User/weblogic')
cmo.setPassword(os.environ.get("DOMAIN_PASSWORD"))
# Please set password here before using this script, e.g. cmo.setPassword('value')


setOption('OverwriteDomain', 'true')
writeDomain(DOMAIN_DIR)
closeTemplate()
exit()

