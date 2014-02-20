#!/bin/tcsh

setenv BLENDER_USER_CONFIG ./config
setenv BLENDER_USER_SCRIPTS ./scripts

if $1 =~ "*.py" then
    blender270a --debug --python $1
else
    blender270a --debug
endif
