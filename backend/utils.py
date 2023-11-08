import subprocess


def get_device_id():
    my_device = subprocess.Popen(
        ["cat", "/etc/machine-id"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT
    )
    stdout, stderr = my_device.communicate()
    list_id = str(stdout).split("'")
    return list_id[1].strip("\\n")
