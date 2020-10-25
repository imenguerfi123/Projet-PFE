### objective ###
Create a simple module with an int parameter

### cmd ###

1- Loading the module with an array parameter
	insmod modulePar.ko parameter=5
2- Modifying the parameter when the module is loaded
	echo "7" >/sys/module/modulePar/parameters/parameter
3- View changes
	cat /sys/module/modulePar/parameters/parameter

