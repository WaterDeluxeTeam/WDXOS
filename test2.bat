@echo off
chmod +x test2.bat

title Snake Game

setlocal EnableDelayedExpansion

REM Define game settings
set WIDTH=20
set HEIGHT=10
set "SNAKE_BODY_CHAR=O"
set "FRUIT_CHAR=*"
set "EMPTY_CHAR=."

REM Initialize game state
set "snake=2 2 1 2 0 2"
set "dir=right"
set "fruit=5 5"
set "score=0"
set "gameOver=0"

REM Clear the screen
cls

:gameLoop
REM Draw the game board
for /l %%y in (0,1,%HEIGHT%) do (
    for /l %%x in (0,1,%WIDTH%) do (
        set "cell=%%x %%y"
        set "isSnake=0"
        set "isFruit=0"
        for %%s in (%snake%) do (
            if "!cell!"=="%%s" (
                set "isSnake=1"
            )
        )
        if "!cell!"=="%fruit%" (
            set "isFruit=1"
        )
        if !isSnake! equ 1 (
            echo|set /p=!SNAKE_BODY_CHAR!
        ) else if !isFruit! equ 1 (
            echo|set /p=!FRUIT_CHAR!
        ) else (
            echo|set /p=!EMPTY_CHAR!
        )
    )
    echo.
)

REM Check for user input
choice /c:wasdx /n /t 0.1 /d w >nul
set "input=%errorlevel%"
if %input% equ 1 (
    set "dir=up"
) else if %input% equ 2 (
    set "dir=down"
) else if %input% equ 3 (
    set "dir=left"
) else if %input% equ 4 (
    set "dir=right"
)

REM Update the snake's position
for %%i in (%snake%) do (
    set /a "x=%%i %% WIDTH"
    set /a "y=%%i / WIDTH"
    set "pos[!x! !y!]=1"
)

if "%dir%"=="up" (
    set /a "y=snake[1]-1"
    set /a "x=snake[0]"
) else if "%dir%"=="down" (
    set /a "y=snake[1]+1"
    set /a "x=snake[0]"
) else if "%dir%"=="left" (
    set /a "x=snake[0]-1"
    set /a "y=snake[1]"
) else if "%dir%"=="right" (
    set /a "x=snake[0]+1"
    set /a "y=snake[1]"
)

REM Check for collision
if defined pos[%x% %y%] (
    set "gameOver=1"
)

REM Move the snake
if %gameOver% equ 0 (
    set "snake=%x% %y% %snake%"
    set "pos[%x% %y%]=1"
    if %x% equ %fruit:~0,1% if %y% equ %fruit:~2,1% (
        set /a "score+=1"
        call :generateFruit
    ) else (
        for %%i in (!snake!) do (
            set "pos[%%i]="
        )
        set "snake=%x% %y%"
    )
)

REM Check for game over
if %x% lss 0 if %y% lss 0 if %x% gtr %WIDTH% if %y% gtr %HEIGHT% (
    set "gameOver=1"
)

if %gameOver% equ 1 (
    echo Game Over!
    echo Your Score: %score%
    pause >nul
    exit /b
)

REM Delay before next frame
timeout /t 0.1 >nul

REM Clear the screen
cls

goto :gameLoop

:generateFruit
set /a "fruitX=%random% %% WIDTH"
set /a "fruitY=%random% %% HEIGHT"
set "fruit=%fruitX% %fruitY%"
if defined pos[%fruitX% %fruitY%] (
    call :generateFruit
)
exit /b
