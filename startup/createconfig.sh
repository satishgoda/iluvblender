#!/bin/tcsh

setenv BLENDER_USER_CONFIG ./config
setenv BLENDER_USER_SCRIPTS ./scripts

if (-d config) then
    rm -rfv config
endif

if (-d scripts) then
    rm -rfv scripts
endif

mkdir config scripts -v && blender270a --debug --background --python myprefs.py

tree --dirsfirst --noreport -C
