echo"Enter your desired Port number"
read PORTNUM
if [ ${PORTNUM} -gt 0 ] && [ ${PORTNUM} -lt 65536 ]
then
	echo " Port number entered accepted"
else
	echo "  Port number entered not accepted out of Range"
fi