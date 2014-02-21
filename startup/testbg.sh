#!/bin/tcsh

setenv BLENDER_USER_CONFIG ./config
setenv BLENDER_USER_SCRIPTS ./scripts

if $1 =~ "*.py" then
    if $2 =~ 'debug' then
        blender --background --debug --python $1
    else
        blender --background --python $1
    endif
else
    echo "Since we are running in background mode, please specify a python script to run"
endif
