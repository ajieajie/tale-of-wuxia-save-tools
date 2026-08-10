@echo off
chcp 65001 >nul
echo 侠客风云传前传 - 存档恢复工具
echo.
echo 可用的备份:
dir /B "D:\steam_jie\userdata\1187465257\650760\remote\Save19.Save.backup_*" 2>nul
echo.
set /p backup="输入要恢复的备份文件名（完整文件名）: "
if exist "D:\steam_jie\userdata\1187465257\650760\remote\%backup%" (
    copy /Y "D:\steam_jie\userdata\1187465257\650760\remote\%backup%" "D:\steam_jie\userdata\1187465257\650760\remote\Save19.Save"
    echo 恢复完成!
) else (
    echo 文件不存在!
)
pause
