@ECHO OFF

set BLENDER_USER_CONFIG=%CD%\config
set BLENDER_USER_SCRIPTS=%CD%\scripts

if not -%1-==-- (
    CALL %BLENDER_INSTALL_DIR%\blender270a.lnk --python %CD%\%1
) ELSE (
    CALL %BLENDER_INSTALL_DIR%\blender270a.lnk
)
