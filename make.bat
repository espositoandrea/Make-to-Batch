@echo off


IF /I "%1"=="all" GOTO all
IF /I "%1"=="docs" GOTO docs
IF /I "%1"=="dist" GOTO dist
IF /I "%1"=="" GOTO all
GOTO error

:all
	CALL make.bat docs
	GOTO :EOF

:docs
	pdoc --html ./make_to_batch --output-dir ./docs/ --force
	GOTO :EOF

:dist
	py -3 setup.py sdist
	twine upload dist/* --skip-existing
	GOTO :EOF

:error
    IF "%1"=="" (
        ECHO make: *** No targets specified and no makefile found.  Stop.
    ) ELSE (
        ECHO make: *** No rule to make target '%1%'. Stop.
    )
    GOTO :EOF
