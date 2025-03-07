from apscheduler.schedulers.background import BackgroundScheduler

def monitor_devices():
    devices = Device.query.all()
    for device in devices:
        info = get_system_info(device.ip, device.snmp_user, device.snmp_auth_pass, device.snmp_enc_pass)
        if 'error' in info:
            send_telegram_alert(f'Device {device.name} is down!')

scheduler = BackgroundScheduler()
scheduler.add_job(monitor_devices, 'interval', minutes=5)
scheduler.start()