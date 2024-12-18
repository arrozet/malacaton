@echo off
setlocal

:: Definir la cadena a buscar y la cadena de reemplazo
set "FIND=http://jajerje.fun/"
set "REPLACE=https://dajer.netlify.app"


:: Buscar y reemplazar en los archivos html, txt, css, js, xml dentro de la carpeta actual y subcarpetas
for /r %%f in (*.html *.txt *.css *.js *.xml) do (
    if exist "%%f" (
        echo Modificando "%%f"
        powershell -Command "(Get-Content -Path '%%f') -replace '%FIND%', '%REPLACE%' | Set-Content -Path '%%f'"
    )
)

echo Reemplazo completado.
