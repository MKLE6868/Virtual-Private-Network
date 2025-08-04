document.getElementById('toggleVPN').addEventListener('click', () => {
  chrome.runtime.sendNativeMessage(
    'com.yourcompany.vpncontrol',
    { action: "toggle" },
    (response) => {
      document.getElementById('status').innerText = response ? response.status : "No response";
    }
  );
});
