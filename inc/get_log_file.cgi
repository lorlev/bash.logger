#!/bin/sh

cd ../server.logs

echo "<div class='log-viewer'>"
echo "<pre id='code'>"

LogBody=$( tail -n 200 $LOG_FILE_NAME )

LogBody=$(echo "${LogBody//$'\n'/</code><code>}") #Replace /n to <code> tag
LogBody=$(echo "${LogBody//$'[32m'/<span style='color: #00A000;' />}") #Green
LogBody=$(echo "${LogBody//$'[36m'/<span style='color: #009E9E;' />}") #Blue
LogBody=$(echo "${LogBody//$'[35m'/<span style='color: #A000A0;' />}") #Purple
LogBody=$(echo "${LogBody//$'[0;39m'/</span />}") #End of tag

echo "<code>$LogBody</code>"
echo "</pre>"
echo "</div>"