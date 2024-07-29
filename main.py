
import psutil
from win10toast import ToastNotifier

battery = psutil.sensors_battery()
percent = battery.percent
toaster= ToastNotifier()
toaster.show_toast("Battery Percent",str(percent) + "% Battery remain!!",icon_path="...ico", duration = 5, threaded = True)
