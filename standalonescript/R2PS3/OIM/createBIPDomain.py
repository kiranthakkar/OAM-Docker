import os

DOMAIN_DIR=os.environ.get("OIM_DOMAIN_DIR")
BIP_TEMPLATE=os.environ.get("MW_HOME") + r'/oracle_bip/common/templates/applications/oracle.bipublisher_template_11.1.1.jar'

print 'Extending Domain for BIP...'

readDomain(DOMAIN_DIR)
cd('/')
setOption('AppDir', DOMAIN_DIR+r'/applications')
addTemplate(BIP_TEMPLATE)



updateDomain()
closeDomain()
exit()

