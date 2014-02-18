@ECHO OFF

if EXIST config RD /S /Q config
if EXIST scripts RMDIR /S /Q scripts

mkdir config
mkdir scripts

set BLENDER_USER_CONFIG=%CD%\config
set BLENDER_USER_SCRIPTS=%CD%\scripts

CALL %BLENDER_INSTALL_DIR%\blender270a.lnk --debug --background --python %CD%\myprefs.py
