
git merge master
make html
xcopy /y /s _build\html\* ..\
del ..\.buildinfo
rmdir /s /q ..\_modules
rmdir /s /q ..\_sources
git add ..\
git commit -am "update docs"
git push origin gh-pages

