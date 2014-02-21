@ECHO OFF

set BLENDER_USER_CONFIG=%CD%\config
set BLENDER_USER_SCRIPTS=%CD%\scripts

if not -%1-==-- (
    if not -%2-==-- (
	    CALL %BLENDER_INSTALL_DIR%\blender270.lnk --debug --background --python %CD%\%1
    ) ELSE (
	    CALL %BLENDER_INSTALL_DIR%\blender270.lnk --background --python %CD%\%1
    )
) ELSE (
    @ECHO "You must specify a python script since blender will be running in background mode"
)
