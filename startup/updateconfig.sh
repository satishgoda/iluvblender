#!/bin/tcsh

setenv BLENDER_USER_CONFIG ./config
setenv BLENDER_USER_SCRIPTS ./scripts

if (-d $BLENDER_USER_CONFIG && -d $BLENDER_USER_SCRIPTS) then
    blender --background --python handleAddons.py
else
    echo "CONFIG/SCRIPTS are missing"
endif
