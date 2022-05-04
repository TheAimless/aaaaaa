@echo off
..\venv\Scripts\activate
set TESTLINK_API_PYTHON_SERVER_URL=http://hieunmtestlink.hopto.org/testlink/lib/api/xmlrpc/v1/xmlrpc.php
set TESTLINK_API_PYTHON_DEVKEY=ecc58154addc68e25b0a9164bba06489
echo now
python ./init.py %*
pause