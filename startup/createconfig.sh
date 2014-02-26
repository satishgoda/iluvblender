#!/bin/tcsh

setenv BLENDER_USER_CONFIG ./config
setenv BLENDER_USER_SCRIPTS ./scripts

if (-d $BLENDER_USER_CONFIG) then
    if (-f $BLENDER_USER_CONFIG/startup.blend) then
        rm -fv $BLENDER_USER_CONFIG/startup.blend
    endif
    if (-f $BLENDER_USER_CONFIG/userpref.blend) then
        rm -fv $BLENDER_USER_CONFIG/userpref.blend
    endif
endif

#if (-d scripts) then
#    rm -rfv scripts
#endif

#mkdir config -v && blender270 --debug --background --python myprefs.py
#mkdir config -v && blender270 --background --python myprefs.py

blender270 --background --python myprefs.py

tree --dirsfirst --noreport -C

