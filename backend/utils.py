import subprocess, requests
from backend.settings import BACKEND_PHP_SERVER

def get_device_id():
    my_device = subprocess.Popen(
        ["cat", "/etc/machine-id"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT
    )
    stdout, stderr = my_device.communicate()
    list_id = str(stdout).split("'")
    return list_id[1].strip("\\n")


def sync_devices():
    payload = {"machine_id": get_device_id()}
    response = requests.post(f"{BACKEND_PHP_SERVER}/sync_devices/",payload).json()
    data = response.data
    
