@echo off
REM Author: Adam Lincoln
REM Date: 2/8/2011
REM Purpose: Run solution.py
echo Python Runner
echo ===
echo Runs solution.py
echo ---
python solution.py --limit=1000 --denominators=3,5
python solution.py -l=1000 -d=3,5
pause