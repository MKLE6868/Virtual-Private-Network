# Python VPN & Chrome Extension Controller

This project is a demonstration of building a simple VPN using Python and controlling it via a Google Chrome Extension. It is meant for educational purposes and as a foundation for further development.

## Features

- **Python VPN (Client & Server):**
  - Basic tunneling using TUN devices and sockets.
  - Multi-client support (server).
  - Simple echo for demonstration (expand to real VPN logic as needed).

- **Chrome Extension Add-On:**
  - Lets users start/stop the VPN client from the browser.
  - Uses Chrome Native Messaging to communicate with the Python process.

## Quick Start

### 1. Python VPN

#### Server
```bash
sudo python3 vpn_server.py
```

#### Client
```bash
sudo python3 vpn_client.py
```
> Update `SERVER_IP` in `vpn_client.py` to point to your VPN server.

### 2. Chrome Extension

1. Load the `chrome-extension` directory as an unpacked extension in Chrome.
2. Register the native messaging host by placing the host manifest file in the correct location and updating `"path"` and `"allowed_origins"`.

### 3. Native Messaging Host

- Run `vpn_host.py` as your native messaging host.
- The Chrome extension will communicate with this script to start/stop the VPN client.

## Security Notice

This is a basic, educational VPN. For any real-world use, you must implement:
- Strong authentication (passwords/keys)
- Encryption (SSL/TLS)
- Proper error handling and resource management

## Requirements

- Python 3.x
- Administrator/root privileges (to create TUN interface)
- Linux (for TUN example; TAP/Windows support can be added)
- Google Chrome

## License

MIT License

## Credits

- Inspired by open-source networking and browser extension tutorials.
