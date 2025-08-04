import sys
import struct
import subprocess
import json

# Path to your VPN client script
VPN_CLIENT_CMD = ["sudo", "python3", "vpn_client.py"]

vpn_process = None

def send_message(message):
    encoded = json.dumps(message).encode('utf-8')
    sys.stdout.buffer.write(struct.pack('I', len(encoded)))
    sys.stdout.buffer.write(encoded)
    sys.stdout.flush()

def read_message():
    raw_length = sys.stdin.buffer.read(4)
    if len(raw_length) == 0:
        return None
    message_length = struct.unpack('I', raw_length)[0]
    message = sys.stdin.buffer.read(message_length).decode('utf-8')
    return json.loads(message)

def main():
    global vpn_process
    while True:
        message = read_message()
        if message is None:
            break
        if message.get("action") == "toggle":
            if vpn_process and vpn_process.poll() is None:
                vpn_process.terminate()
                send_message({"status": "VPN stopped"})
                vpn_process = None
            else:
                vpn_process = subprocess.Popen(VPN_CLIENT_CMD)
                send_message({"status": "VPN started"})

if __name__ == '__main__':
    main()
