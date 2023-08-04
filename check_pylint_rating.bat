@echo off

:: Install required dependencies
python -m pip install pylint pylint-django Django djangorestframework

:: Run pylint and extract rating
for /f "tokens=7 delims=/ " %%a in ('pylint --rcfile=.pylintrc Backend/*.py ^| findstr "rated at"') do set rating=%%a

:: Check if rating is at least 7 and exit with appropriate status
set rating=%rating:/=%
if %rating% lss 7 (
    exit /b 1
)

exit /b 0
