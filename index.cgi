#!/bin/sh

printf "Content-Type: text/html"
echo

printf "Status: 200 OK"
echo
echo

#Web Params
SCRIPT=$(readlink -f "$0")
ROOT=$(dirname "$SCRIPT")
URL="$REQUEST_SCHEME://$SERVER_NAME/log.viewer"

GET=$(echo "${QUERY_STRING//$'url=log.viewer/'}")
GET=(${GET//// })

echo "<!DOCTYPE html>"
echo "<html>"
echo "<head>"

echo "<title>Logger</title>"
echo "<script src='https://ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js'></script>"
echo "<link rel='stylesheet' href='https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css'>"
echo "<link rel='stylesheet' type='text/css' href='$URL/css/style.css'>"

echo "</head>"
echo "<body>"

if [[ ${GET[0]} = "get_log_file" ]]; then
	LOG_FILE_NAME=${GET[1]}
	source "$ROOT/inc/get_log_file.cgi"
else
	source "$ROOT/inc/main.cgi"
fi

echo "<script type='text/javascript' src='$URL/js/script.js'></script>"
echo "</body>"
echo "</html>"

exit 0