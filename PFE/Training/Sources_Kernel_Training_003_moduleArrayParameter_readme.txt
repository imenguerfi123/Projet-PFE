### objective ###
Create a simple module with an array as parameter

### cmd ###

1- Loading the module with an array parameter
	insmod moduleArrayPar.ko array=1,2,3,4,5
2- Modifying the array when module is loaded
	echo "2,1,2,7" >/sys/module/moduleArrayPar/parameters/array

