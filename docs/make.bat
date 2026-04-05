@ECHO OFF

set SPHINXBUILD=python -m sphinx
set SOURCEDIR=source
set BUILDDIR=build

if "%1" == "" goto help

%SPHINXBUILD% -M %1 %SOURCEDIR% %BUILDDIR%
goto end

:help
echo.Usage: make.bat [html^|clean]
:end
