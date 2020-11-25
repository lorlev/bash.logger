#!/bin/sh

cd ../server.logs

echo "<div class='file-list'>"
echo "<div style='padding: 20px;'>"
echo "<h5>Log Files</h5>"
echo "<div class='row'>"

for log_file in *.log; do

echo "<div class='col-sm-2'>"
echo "<a href='$URL/get_log_file/$log_file'>"
echo "<div class='card'>"
echo "<div class='card-header bg-transparent'>"
echo "<img src='$URL/img/log.jpg' class='mx-auto d-block' style='max-width: 75px;'>"
echo "</div>"
echo "<div class='card-body' style='padding: 10px 14px;'>"
echo "<h7 class='card-title font-weight-bold'>"
echo "<h7 class='card-title font-weight-bold'>${log_file}</h7>"
echo "<p class='card-text text-muted' style='font-size: 12px;'>`du -h $log_file | cut -f -1`</p>"
echo "</div>"
echo "<div class='card-footer' style='padding: 5px 14px;'>"
echo "<small class='text-muted'>`date -r $log_file '+%m-%d-%Y %H:%M:%S'`</small>"
echo "</div>"
echo "</a>"
echo "</div>"
echo "</div>"

done;

echo "</div>"
echo "</div>"
echo "</div>"