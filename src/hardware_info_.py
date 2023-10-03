import psutil


def get_hardware_info():
    # CPU info
    cpu_logical = psutil.cpu_count(logical=True)
    cpu_physical = psutil.cpu_count(logical=False)

    # RAM info
    ram_info = psutil.virtual_memory()
    total_ram = ram_info.total // (1024**3)  # Convert to GB
    available_ram = ram_info.available // (1024**3)  # Convert to GB

    # Disk info
    disk_info = psutil.disk_usage("/")
    total_disk = disk_info.total // (1024**3)  # Convert to GB
    free_disk = disk_info.free // (1024**3)  # Convert to GB

    hardware_info = {
        "CPU Logical Cores": cpu_logical,
        "CPU Physical Cores": cpu_physical,
        "Total RAM (GB)": total_ram,
        "Available RAM (GB)": available_ram,
        "Total Disk (GB)": total_disk,
        "Free Disk (GB)": free_disk,
    }

    return hardware_info


# Get hardware info
hardware_info = get_hardware_info()
hardware_info
print(f"#### Hardware info scan finished")