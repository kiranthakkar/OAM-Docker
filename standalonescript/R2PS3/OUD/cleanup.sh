#!/bin/bash
source setEnv.sh
${OUD_INSTANCE}/OUD/bin/stop-ds
rm -rf ${OUD_INSTANCE}
