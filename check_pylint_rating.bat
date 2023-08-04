@echo off

:: Install required dependencies
python -m pip install pylint pylint-django Django djangorestframework

:: Run pylint and extract rating
for /f "tokens=7 delims=/ " %%a in ('pylint --rcfile=.pylintrc Backend/*.py ^| findstr "rated at"') do set rating=%%a

:: Print the rating to the terminal
echo Your code has been rated at %rating%/10

:: Check if rating is at least 7 and exit with appropriate status
set rating=%rating:/=%
if %rating% lss 7 (
    echo Commit failed: code rating must be at least 7
    exit /b 1
)

echo Commit succeeded: code rating is above 7
exit /b 0
