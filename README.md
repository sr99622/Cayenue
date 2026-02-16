<h3>Quick Installer Download Links</h3>

### [Flatpak](https://github.com/sr99622/Cayenue/releases/download/v1.0.9/Cayenue-1.0.9.flatpak)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Snap](https://github.com/sr99622/Cayenue/releases/download/v1.0.9/cayenue_1.0.9_amd64.snap)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Mac OS](https://github.com/sr99622/Cayenue/releases/download/v1.0.9/Cayenue-1.0.9.dmg)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[Windows](https://github.com/sr99622/Cayenue/releases/download/v1.0.9/Cayenue-installer-1.0.9.exe)

<i>Please refer to the Software Installation section of this document for detailed instructions.</i>

<!---
Cayenue brand colors
background: 1E1F6E
foreground: 939FB9
--->

&nbsp;

<image src="assets/images/cayenue_logo.png">

<h3>IP Camera Interface Software</h3>

View, analyze and store AV streams from a fleet of networked cameras in real time. Quickly set up and manage complex systems with easily understood and intuitive controls. Concurrently review alert events with integrated media player. Distribute streams using proxy service multipliers. Absolute autonomy over data privacy. High performance software with responsive interface and proven stability.

<h3>System Requirements</h3>

ONVIF compliant cameras. Brands known to work with this system: Dahua, Hikvision, Amcrest, Trendnet, Reolink, Axis, Vivotek, Speco.

Computers running Linux, Mac or Windows. Cayenue is a multi-modal system and runs as both the server and the client. Linux and Mac are recommended for the server. To run YOLO inference on camera streams, a capable compute unit is required. Supported GPUs include Intel iGPU, NVIDIA and Mac Silicon. Excellent results are acheived with Intel Xe graphics and Apple M series chips. These compute units offer outstanding power consumption profiles, strong performance and are supported directly by the installers for zero configuration.

<h3>Network Configuration</h3>

Cayenue supports complete camera isolation with proxy services. The cameras are unable to access either your own network or the internet at large. This is a critical feature for privacy that protects your installation and data.

Recordings are stored locally and shareable from the server for access by client computers. Configure the server for SMB protocol and pull video with the integrated file browser from any supported OS.

An integrated HTTP server provides access to live video streams from unconfigured devices such as mobile phone.

<h3>Searchable Video Database</h3>

Events triggered by the YOLO detector are stored as images that can be linked to the Video library. Simply double click the picture to start the timelime playback. Specific time points in video files can be accessed using the search tool. Important functions have associated key bindings for mouseless operation.

<h3>Expand The Horizon</h3>

Open source software written in Python with permissive Apache license affords the ability to craft custom algorithms for advanced usage. 


## Operation

<details>
<summary>Screenshots</summary>

&nbsp;

The app running YOLOX detections on multiple camera streams

<image src="assets/images/screenshot_1.png">

&nbsp;

The file browser can scroll through detection pictures and automatically launch the associated video file at the timepoint of the detection

<image src="assets/images/screenshot_2.png">

&nbsp;

Accurately control camera timestamps

<image src="assets/images/screenshot_3.png">

&nbsp;

Detect audio events with amplitude and frequency analysis

<image src="assets/images/screenshot_4.png">

&nbsp;

Fine grained control over YOLO model parameters

<image src="assets/images/screenshot_5.png">

&nbsp;

</details>

<details>
<summary>Hardware</summary>

&nbsp;

The system installation requires network connected components and appropriate switching hardware. The software is designed to support ONVIF compatible cameras. Please note that not all cameras support ONVIF, and those that do may have non-compliant or incomplete implementations. Cayenue supports a wide range of cameras and is tolerant of non-compliant implementations. Cameras listed in the System Requirements section above can be expected to work. Many other types of cameras are derivative of those listed and should behave in a similar fashion.

The software can operate in three modes, Stand-Alone, Server and Client. Stand-Alone mode requires minimal configuration but is considered obsolete. Server mode is recommended, even if there is only one computer being used to view camera streams on the network. Server mode includes a Proxy server [Media MTX](https://github.com/bluenviron/mediamtx) that will provide a buffer between the camera stream and the Server. This has beneficial effects for stability and allows multiple Clients to access camera streams. However, some cameras may not conform properly to RTSP standards expected by the Proxy, in which case Stand-Alone mode may provide better results for a single computer setup. Client mode requires a Server and can be installed and used by any number of computers, limited by the network constraints of the installation.

Operating a Server with dual network interface ports provides the opportunity for subnet isolation of cameras. If the hardware under consideration for the Server only has one ethernet network interface, a dongle can be used to connect a second ethernet cable, although dongled connections can be expected to have lower bandwidth. 

There are many benefits to camera isolation, not the least being enhanced network security that prevents camera network communication with the internet at large, or the internal network. Some cameras have built in hardcoded requests to internet time servers that may be improperly implemented resulting in incorrect timestamps on videos. Denying camera access to internet time servers allows Cayenue to definitively control the timestamp of the camera. Non-compliant protocol implementations by cameras also present a stability threat to the local network that isolation can prevent.

It is possible to use wireless cameras in the system, but this is not recommended. There are situations where wireless cameras may be the only option, in which case stream resolutions and framerates should be reduced in order to avoid stability issues. Wireless routers and access points can be used to build an isolated camera subnet in the same manner as presented here for wired connections.

### Cayenue Network Configuration

<image src="assets/images/net_config.png" width="600">

&nbsp;

When cameras are isolated on a separate subnet, there is a requirement to provide IP address assignment to the cameras. This can be done using static IP addresses, or by using DHCP (Dynamic Host Configuration Protocol). DHCP is the recommended method for assigning camera IP addresses. 

DHCP is configured on Linux by installing a service program that is configured with an edited file. Similarly, Mac OS can be configured to run a DHCP server by editing a configuration file. Although Windows is not recommended for Server configuration, it is possible to use a free program for DHCP address assignment.

One important point to note is that the DHCP server for the camera subnet MUST reside on the proper network interface (on the diagram 10.2.2.0/24). There can only be one DHCP server on a network and the existing DHCP service provided by the internal local network router may experience issues if the Cayenue Server DHCP is run on the wrong network interface (on the diagram 192.168.1.0/24). Your actual network nomenclature may differ from that shown here.

Cayenue is designed to take advantage of advanced [YOLOX](https://github.com/Megvii-BaseDetection/YOLOX) inference detection algorithms for detecting objects of interest. In order to run this inference, there is a requirement that the Server have a capable compute unit. Integrated GPU or NPU hardware is recommended for this task. Discrete GPU may also be used, but at a significantly higher power consumption profile, as well as additional driver installation and configuration. Intel iGPU and Apple Silicon NPU are recommended and are directly supported by the Cayenue installation programs and do not require any additional configuration.

Hardware requirements for Client configuration are more relaxed as the Client can recieve alerts from the server and do not require any additional inference processing capabilties. If the Server is configured to share its Picture and Video directories using SMB protocol (Samba), Clients may access pictures and videos from the Server without the need for local storage. SMB performance is excellent in a local network scenario, and can be expected to provide essentially the same experience as local storage.

</details>

<details>
<summary>Software Installation</summary>

&nbsp;

<i>Select the instructions for your operating system below</i>

<details>
<summary>Linux</summary>

&nbsp;

---

<details>
<summary>Flatpak</summary>

&nbsp;

---

Download the [Flatpak installer](https://github.com/sr99622/Cayenue/releases/download/v1.0.9/Cayenue-1.0.9.flatpak), then open a terminal and navigate to the Downloads folder. Use the following command to install.

```
flatpak install Cayenue-1.0.9.flatpak
```

In some cases, it may be necessary to re-boot the computer in order to see the icon in the Applications menu.

The program can then be launched from the Applications menu. To uninstall use the command.

```
flatpak uninstall io.github.sr99622.Cayenue
```

---

&nbsp;

</details>

<details>

<summary>Snap</summary>

&nbsp;
____

Download the [snap installer](https://github.com/sr99622/Cayenue/releases/download/v1.0.9/cayenue_1.0.9_amd64.snap), then open a terminal and navigate to the Downloads folder. Use the following command to install.

```
sudo snap install cayenue_1.0.9_amd64.snap --dangerous
```

The program can then be launched from the Applications menu. In order to get audio, you need to connect the pulseaudio driver.

```
sudo snap connect cayenue:pulseaudio
```

If you would like to use the NPU on Intel, the driver can be installed as follows.

```
sudo snap install intel-npu-driver
sudo chown root:render /dev/accel/accel0
sudo chmod g+rw /dev/accel/accel0
sudo usermod -a -G render $USER
sudo bash -c "echo 'SUBSYSTEM==\"accel\", KERNEL==\"accel*\", GROUP=\"render\", MODE=\"0660\"' > /etc/udev/rules.d/10-intel-vpu.rules"
sudo udevadm control --reload-rules
sudo udevadm trigger --subsystem-match=accel
sudo reboot now
```

To uninstall.

```
sudo snap remove cayenue
```

</details>

---

&nbsp;

</details>

<details>
<summary>Mac</summary>

&nbsp;

---

An installer is available for Apple Silicon running Mac OS version Sequoia (15).

Download the [installer](https://github.com/sr99622/Cayenue/releases/download/v1.0.9/Cayenue-1.0.9.dmg) and open it. Drag the Cayenue icon into the Applications folder. Once the installation is complete, the program can then be started from the Launchpad. To uninstall the program, use Finder to go to the Applications directory, then right click over the icon and select Move to Trash.

---

&nbsp;

</details>


<details>
<summary>Windows</summary>

&nbsp;

---

An installer is available for Windows.

Download the [installer](https://github.com/sr99622/Cayenue/releases/download/v1.0.9/Cayenue-installer-1.0.9.exe) and double click on it. You will receive a warning message from the Operating System. Follow the prompts on the screen to install the program. It can be launched from the icon found in the Applications menu. To uninstall the program, go to Settings -> Apps -> Installed Apps and find the icon, then use the three dot button on the right to select action.

---

&nbsp;

</details>

<details>
<summary>NVIDIA GPU</summary>

&nbsp;

<i>The installers are pre-configured for YOLO inference on Intel or Apple Silicon iGPU. separate instructions are provided if inference is required on NVIDIA GPU. If inference is not a system requirement, the standard installers are sufficient for operation with NVIDIA GPU.</i>

___

If YOLO operation is desired for systems equipped with NVIDIA GPU, an alternate installation method is required. This is due to the large size of the files required for NVIDIA operation. To use the application with NVIDIA GPU on Linux, create a python virtual environment, then use pip to install.

```
python3 -m venv env
source env/bin/activate
pip install cayenue openvino
```

Then follow the directions at [PyTorch](https://pytorch.org/get-started/locally/) to complete the installation based on your operating system and CUDA version.

To use an icon with this configuration, use the command below. If working on windows, please run `pip install winshell` in the virtual environment prior to running this command.

```
sudo env\bin\Cayenue --icon
```

---

&nbsp;

</details>

<details>
<summary>aarch64 flatpak</summary>

&nbsp;

---

Download the [Flatpak installer](https://github.com/sr99622/Cayenue/releases/download/v1.0.9/Cayenue-1.0.9_aarch64.flatpak), then open a terminal and navigate to the Downloads folder. Use the following command to install.

```
flatpak install Cayenue-1.0.9_aarch64.flatpak
```

Depending on the platform, it may be necessary to add some components to get the application running. The following commands may be helpful.

```
flatpak install flathub org.freedesktop.Platform//25.08
flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo
```

In some cases, it may be necessary to re-boot the computer in order to see the icon in the Applications menu.

The program can then be launched from the Applications menu. To uninstall use the command.

```
flatpak uninstall io.github.sr99622.Cayenue
```

---


</details>

&nbsp;

---

The software runs in three modes, Stand Alone, Server and Client. Stand Alone is a fully featured system that requires minimal configuration, but is considered to be obsolete. Server mode performs all functions and is recommended over Stand Alone. Server mode requires more planning and effort to set up, but offers many benefits over Stand Alone. Client mode is easily configured, but requires access to a Server.

Server mode requires the configuration of two services for network communication, SMB protocol for file sharing with clients and DHCP service for the camera subnet. The instructions for setting up these services will vary by operating system. Instructions are provided for Mac OS and Linux distributions Ubuntu and Fedora. Similar procedures apply to Windows, however, the use of Windows as a Server is discouraged. Windows works well as a client, but is difficult to stabilize in a Server role.

Please refer to the diagram presented in the Hardware section of this document, as it shows the configuration for which these instructions are validated. The Server will require two Network Interfaces. If the hardware has only one ethernet port, a dongle can be used to provide a second network interface.

&nbsp;

<details>
<summary>Building Out The Server</summary>

&nbsp;

<i>Service configuration for SMB and DHCP are recommended prior to software installation for Cayenue on Servers. This reduces the number of variables under consideration during individual steps of the build process. It is recommended to set up and verify SMB first, then set up and verify DHCP, then install Cayenue.</i> 

---

&nbsp;

<b>SMB configuration</b>

The server should have a fixed IP address on the local network for client access. The router for your local network will control the range of addresses available for fixed IP. In most cases, these will be the lowest or highest numbered addresses on the network. Looking at the router configuration will provide definitive answers to this question. It's always a good idea to ping out to the network to verify that the address under consideration is not being used already, as duplicate addresses can cause mysterious undefined behavior. Prior to setting a fixed IP address for the local network, it is recommended to make note of the current configuration and retain the existing Netmask, Gateway and DNS settings so that the IP address is the only parameter undergoing change.

When configuring SMB service, it is recommended to physically connect only the network interface for the local network used by clients and leave the camera subnet disconnected. This will help reduce confusion over network interface designation. If the two interfaces have different bandwidth properties, the higher bandwidth connection should be used for the local network.

<details>
<summary>Linux - Ubuntu</summary>

&nbsp;

---

It is possible for Windows clients to access camera recordings residing on a Linux server on the local network by installing a samba share on the Linux server. There are a few steps needed to set up the server, which are often not well documented for this type of configuration. The following instructions will set up the shared folder on the server, then show how a Windows client can attach to the shared folder as a mapped drive. Please note that this setup is intended for use in a simple private network where all users can be trusted with data. More sophisticated configurations that control data access are possible, but are beyond the scope of these instructions.

* #### Linux Server Configuration

  <h4>Step 1. <b>Set Fixed IP Address</b></h4> The server should have a fixed IP address. This is not completely necessary for system operation, but will prevent mishaps later that can occur if the server address changes. For Ubuntu and similar systems, there is a GUI control dialog that can be used to assign a fixed IP address. The address chosen will depend on the router settings, which will set aside a range of addresses that are available for fixed IP. Usually this will be at the bottom and/or top of the IP range controlled by the router. The router setting that defines these ranges is set by DHCP. Check ahead of time that the desired IP address is not already taken and is available per the router configuration.

  <h4>Step 2. <b>Install and Configure Samba</b></h4> On Ubuntu, the Samba server is installed using the apt command

  ```
  sudo apt install samba
  ```

  The Samba configuration is performed by editing the `/etc/samba/smb.conf` file. The Samba installation will create a default file in this location, which is not a good fit for this type of configuration. It is recommended to move the file to a backup and start with a fresh file for configuration, following the commands

  ```
  cd /etc/samba
  sudo mv smb.conf smb.conf.bak
  sudo nano smb.conf
  ```

  You will now be starting from a clean slate. The following text saved into the `smb.conf` file will create a sharing configuration that is compatible with the application. For this configuration, you will need to know the account under which Cayenue was installed. For example, if you created a user cayenue, and were logged on as that user during the time the application was installed, the default directory for the application will be /home/cayenue. The configuration shown below will share two sub-directories used by the program, namely Videos and Pictures.
  
  ```
  [global]
    workgroup = WORKGROUP

  [Videos]
    comment = Shared Videos Folder
    path = /home/cayenue/Videos
    browasble = yes
    read only = yes

  [Pictures]
    comment = Shared Pictures Folder
    path = /home/cayenue/Pictures
    browsable = yes
    read only = yes

  [Documents]
    comment = Shared Documents Folder
    path = /home/cayenue/Documents
    browsable = yes
    read only = no
  ```

  <h4>Step 3. Re-start the Samba service</h4> After changing the configuration file, it is necessary to re-start the service in order to enact the changes made. This should be done any time changes are made to the smb.conf file.

  ```
  sudo systemctl restart smbd
  ```
  
  <h4>Step 4. <b>Add User and Set Samba Password</b></h4>

  The command to add a user is

  ```
  sudo useradd -m <username>
  ```
  
  The samba access requires a password for the user
    
  ```
  sudo smbpasswd -a <username>
  ```

  The system will prompt you to enter and verify a password.

---

&nbsp;

</details>

<details>
<summary>Linux - Fedora</summary>

&nbsp;

---

PLEASE NOTE: Replace `<username>` in these instructions with the name of the account under which Cayenue is installed

Install samba

```
sudo dnf install samba samba-common samba-client
```

Open firewall

```
sudo firewall-cmd --permanent --add-service=samba
sudo firewall-cmd --reload
```


Initialize the home directory for sharing

```
sudo semanage fcontext --add --type "samba_share_t" "/home/<username>(/.*)?"
sudo restorecon -R /home/<username>

```

Edit configuration file

```
sudo mv /etc/samba/smb.conf /etc/samba/smb.conf.bak
sudo nano /etc/samba/smb.conf
```

Copy and paste the following configuration file content

```
[global]
  workgroup = WORKGROUP
  security = user

[cayenue]
  comment = Cayenue Shared Folders
  path = /home/<username>
  valid users = <username>
  browseable = yes
  writable = no
  guest ok = no
  read only = yes
  public = yes
```

Use ctl+O to save and ctl+X to exit nano

add password

```
sudo smbpasswd -a <username>
```


start and enable

```
sudo systemctl enable smb nmb
sudo systemctl start smb nmb
sudo systemctl status smb
```

A screen displaying configuration should appear and indicate success. The `preset: disabled` is a distribution flag and can be ignored

Reboot 

```
sudo reboot now
```
---

&nbsp;

</details>

<details>
<summary>Mac OS</summary>

&nbsp;

---

Open Sharing Settings: Go to the Apple menu > System Settings > General > Sharing (scroll down if needed).

Enable File Sharing: Turn on the toggle for File Sharing.

Configure SMB: Click the info button (i) or Options next to File Sharing.

Turn on SMB Sharing: Check the box for "Share files and folders using SMB".

Select Users: Under "Windows File Sharing," check the box for each user account that needs access and enter their password.

(Optional) Add Folders: In the main Sharing window, use the "+" button to add specific folders to share and set their permissions (read/write for users). 

---

&nbsp;

</details>

<details>
<summary>Sharing Drives From Windows</summary>

&nbsp;

---

There are a few different paths you can take during this process, so some of the steps below may be redundant. If you click around enough, you should be able to get it working.

The First step is to turn on windows sharing
* Settings -> Network & Internet -> Sharing
* Under Private ensure that both "Turn on Network Discovery: and "Turn on file and printer sharing" are toggled on

Share a folder
* Use the file explorer to find the folder you want to share
* Right click over the folder
* Properties -> Sharing -> Advanced Sharing
* Give access to users with the dropdown box
* You can create a new account from the dropdown

Create an account for the external machines to use when mounting the shared folder
* Settings -> Accounts -> Other Users --> Add Account
* Unfortunately, Microsoft will try to make this a Microsoft account, so you have to click through a couple screens to get to a local account
  * I don't have this person's sign-on information
  * Add a user without a Microsoft Account
* Type in a user name, password and hints, which are required

Add User to Shared Folder
* Use the file explorer and right click over the folder to be shared
* Show More Options -> Give access to -> Specific People
* Select the User name from the dropdown box
* Click Add
* When asked if you want to change folder settings say yes (twice)

You should now be able to sign into the folder from an SMB client with the user credentials

---

&nbsp;

</details>

&nbsp;

Upon completion of the SMB service configuration, a test from a client machine is recommended before continuing.

---

&nbsp;

<b>DHCP Configuration</b>

The ethernet cable for the camera subnet should now be connected. Ensure that the cameras are connected and powered on.
Identify the camera network interface on the Settings -> Network -> Wired Network screen.

The following instructions set a static IP address of `10.2.2.1`. Although very unlikely, please verify that your existing local network does not use this address range. 

From  the Settings -> Network -> Wired Network screen, click on the gear to get details, use the IPv4 tab and click the Manual radio button to enable manual settings. The IP address should be set to `10.2.2.1`, the Subnet Mask to `255.255.255.0` and the Gateway and DNS both set to `10.2.2.1`. 

Follow the directions below for your Operating System to set up the camera subnet DHCP server.

<details>
<summary>Linux - Ubuntu</summary>

&nbsp;

---

The link  [Kea DHCP server](https://ubuntu.com/server/docs/how-to/networking/install-isc-kea/) is recommended reading and contains detailed information not covered here. 

Install the kea server using the following command

```
sudo apt install kea
```

Further configuration will require the name of the network interface intended to provide the DHCP service. On Linux, the command 

```
ip -br addr show
```

will provide a listing of interface properties that will contain the relevant information. The network interface name will look something like `enp1s0` but will be different for each machine. The name will be associated with the ip address (<i>10.2.2.1 as set previously</i>) of the desired interface. Make note of the interface name for use in the next step.

Move the default configuration file to a backup location and open an editor to create the new configuration file

```
sudo mv /etc/kea/kea-dhcp4.conf /etc/kea/kea-dhcp4.conf.bak
sudo nano /etc/kea/kea-dhcp4.conf
```

copy and paste the text below into the file. Replace `<your-interface-name>` with the interface name obtained from the `ip -br addr show` command, retaining the quotation marks.

<b>/etc/kea/kea-dhcp4.conf</b>

```
{
  "Dhcp4": {
    "interfaces-config": {
    "interfaces": [ "<your-interface-name>" ]
    },
    "control-socket": {
        "socket-type": "unix",
        "socket-name": "/run/kea/kea4-ctrl-socket"
    },
    "lease-database": {
        "type": "memfile",
        "lfc-interval": 3600
    },
    "valid-lifetime": 600,
    "max-valid-lifetime": 7200,
    "subnet4": [
    {
        "id": 1,
        "subnet": "10.2.2.0/24",
        "pools": [
        {
            "pool": "10.2.2.64 - 10.2.2.242"
        }
        ],
        "option-data": [
        {
            "name": "routers",
            "data": "10.2.2.1"
        },
        {
            "name": "domain-name-servers",
            "data": "10.2.2.1"
        },
        {
            "name": "domain-name",
            "data": "mydomain.example"
        }
        ]
    }
    ]
  }
}
```

This is a basic configuration that will assign addresses in the range of `10.2.2.64 - 10.2.2.242`, leaving the balance of addresses available for static ip. The router and name server addresses point back to the server, which is a dead end. This means that there is no direct traffic between the cameras and the internet or the rest of the network. All communication with the cameras is proxied by the Cayenue server.

Use the commands shown below to control the service. Be sure to use the enable command to get persistent service operation through reboots.

```
sudo systemctl enable --now kea-dhcp4
```

Check the server status. There should be some indication that the service has started successfully and there is activity with the other devices on the network. It may take a few moments for all devices to complete configuration and there may be stray warning or error messages which are likely transitory. If difficulty is encountered, please refer to the link at the top of this section for troubleshooting information.

```
sudo systemctl status kea-dhcp4
```

---

&nbsp;

</details>

<details>
<summary>Linux - Fedora</summary>

&nbsp;

---

Courtesy of [Server World](https://www.server-world.info/en/note?os=Fedora_43&p=dhcp&f=1). More detailed info there.

Install the DHCP server program. There may be a warning message that appears during the installation of the dhcp-server to the effect `Conflict with earlier configuration for user 'nm-openvpn'`. This is a known issue with the packaging system and does not affect the performance of the dhcp-server.

```
sudo dnf install dhcp-server
```


Edit the configuration file

```
sudo nano /etc/dhcp/dhcpd.conf
```

Add the following content to the conf file

```
default-lease-time 600;
max-lease-time 7200;
authoritative;
subnet 10.2.2.0 netmask 255.255.255.0 {
    range dynamic-bootp 10.2.2.64 10.2.2.224;
    option broadcast-address 10.2.2.255;
    option routers 10.2.2.1;
}
```

Enable the server

```
sudo systemctl enable --now dhcpd 
```

Check the server status. There should be some indication that the service has started successfully and there is activity with the other devices on the network. It may take a few moments for all devices to complete configuration and there may be stray warning or error messages which are likely transitory. If difficulty is encountered, please refer to the link at the top of this section for troubleshooting information.

```
sudo systemctl status dhcpd
```

---

&nbsp;

</details>

<details>
<summary>Mac OS</summary>

&nbsp;

---

On Mac OS, the DHCP service is provided by bootpd. The service is configured with a file named `/etc/bootpd.plist`. A sample configuration file is shown below. 

It is necessary to set the server ethernet interface to a static IP address for this configuration. It is recommended to manually set the Cayenue server ethernet address connecting to the camera network to be `10.2.2.1`. This is a reserved network for private subnets. Although unlikely, please verify that your existing network does not use this address range. To make this configuration, use the Settings -> Network -> Ethernet -> TCP/IP -> Configure IPv4 -> Manually (combo box). The IP address should be set to `10.2.2.1`, the Subnet Mask to `255.255.255.0` and the Router to `10.2.2.1`. If you need internet access, you should have a second network connection to your local router, which is configured separately. Note that you may need to update network priorities in order to use the internet connected interface. Please refer to the section Network Priority on Multi Homed Hosts of this document.

This file is configured to use the interface named `en0`, which in most cases will be the ethernet interface on the Mac computer. Please check the name using the `ifconfig` command to verify that this is the correct information.

### Sample Configuration File

```
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>bootp_enabled</key>
    <false/>
    <key>detect_other_dhcp_server</key>
    <integer>1</integer>
    <key>dhcp_enabled</key>
    <array>
        <string>en0</string>
    </array>
    <key>reply_threshold_seconds</key>
    <integer>0</integer>
    <key>Subnets</key>
    <array>
        <dict>
            <key>allocate</key>
            <true/>
            <key>dhcp_router</key>
            <string>10.2.2.1</string>
            <key>lease_max</key>
            <integer>86400</integer>
            <key>lease_min</key>
            <integer>86400</integer>
            <key>name</key>
            <string>10.2.2</string>
            <key>net_address</key>
            <string>10.2.2.0</string>
            <key>net_mask</key>
            <string>255.255.255.0</string>
            <key>net_range</key>
            <array>
                <string>10.2.2.64</string>
                <string>10.2.2.242</string>
            </array>
        </dict>
    </array>
</dict>
</plist>
```

This is a basic configuration that will assign addresses in the range of `10.2.2.64 - 10.2.2.242`, leaving the balance of addresses available for static ip. The router and name server addresses point back to the server, which is a dead end. This means that there is no direct traffic between the cameras and the internet or the rest of the network. All communication with the cameras is proxied by the Cayenue server.

The service can be set up by copying the sample file to `/etc/bootpd.plist`, replacing the tag `en0` tag in the `dhcp_enabled` key with the appropriate data from the `ifconfig` command if necessary. This can be done using the command `sudo nano /etc/bootpd.plist`, then copying the text above and using ctrl+O, enter, ctrl+X to save and exit.

The service can then be started using the command

```
sudo launchctl load -w /System/Library/LaunchDaemons/bootps.plist
```

The service can be stopped with

```
sudo launchctl unload -w /System/Library/LaunchDaemons/bootps.plist
```

---

&nbsp;

</details>

<details>
<summary>Windows</summary>

&nbsp;

---

[DHCP Server for Windows](https://www.dhcpserver.de/cms/) is made available by third party . Older versions are available for [download](https://www.dhcpserver.de/cms/download/) free of charge. Instructions for installation can be found [here](https://www.dhcpserver.de/cms/running_the_server/). Please consider making a donation to the developer if you find the software useful.

Please note that the installation procedure does not include instructions for setting up a static IP address on the network interface, which is necessary for operation. This should be done before configuring the DHCP service. An exhaustive resource on this topic is available at [How to set a static IP address on Windows 11](https://pureinfotech.com/set-static-ip-address-windows-11/).

---

&nbsp;

</details>

&nbsp;

<b>Additional Server Settings</b>

Check the Power settings for the server and disable Automatic Suspend so the Server will stay on continuously, thereby avoiding undefined behavior when the server goes to sleep. Also check the Host Name in the About settings, this will be the name broadcast over the local network for visibility to the Clients.

---

&nbsp;

<details>
<summary>Mac OS Additional Server Settings</summary>

&nbsp;

For Mac OS the settings for Energy should be adjusted to disable the low power mode for the device during periods of no user interaction. The setting "Prevent automatic sleeping when the display is off" should be set to on. Mac OS will limit the number of file handles that can be open simultaneously. These handles are also associated with network socket creation. This has the effect of limiting the number of clients that can connect to the server. In order to increase the number of handles, the ```ulimit``` command can be used.

```
ulimit -n 8192
```

</details>

&nbsp;

Following the installation of the SMB and DHCP services, Cayenue can be installed on the Server as described in the instructions found above.

&nbsp;

</details>

<details>
<summary>Client Configuration</summary>

&nbsp;

Client configuration consists of two steps. This first is to enter the Server address on the `Settings -> Proxy -> Client -> Connect url from server`. Enter the information from the Server's Proxy tab into the text box. Please make sure to type in the line exactly, including the trailing slash character. Then click the `Update` button to refresh the Client settings. The operation will succeed silently or produce an error message on failure. Clicking the `Discover` button from the Camera panel of the Client should populate the camera list with data retrieved from the Server.

The second step of Client configuration involves the File Browser directory settings for the Pictures and Videos tab. The File Browser is launched from the folder icon on the front Camera panel. In order to set these directories, it is necessary to map the SMB shared drives set up on the Server to locations accessible to the Client.

Mapping remote drives is an Operating System dependent exercise. For Windows servers, setting a mapped network drive is a commmon operation and is not detailed here. Mac OS allows Clients to browse the network from the OS file browser, and is a trivial operation without need for further configuration. Mounting remote SMB drives from Linux, however does require some effort and is detailed below.

<details>
<summary>Mount SMB Drive from Linux Client</summary>

&nbsp;

---

It may be necessary to install cifs-utils on the machine. For example on Manjaro Linux, 

```
sudo pacman -S cifs-utils
```

Create a Mount Point. Please note that if you installed the application by snap or flatpak, you will not have access to the /mnt directory. The installers create a container environment that limits your access to directories on the host. In this case, you should create another mount point that is accessible from within the application container. 

The application containers only allow connection to Videos and Pictures directories on the host. In this case, the easiest option is to create subdirectories in your Videos and Pictures folders. The mounting process will obscure files on the host system in favor of files on the mounted remote. If you have existing files in the Videos or Pictures folders, or if you need to preserve the location for use by other programs, using subdirectories as the mounting points will let you keep using the Videos and Pictures folders without disrupting other programs.

The examples that follow are based on general mounting instructions, and use the generic tag `<mount_point>` to indicate the mount directory. Note that the best practice is to use the full path name of the mount point directory in the following commands.

```
sudo mkdir -p <mount_point>
```

Mount the share, you can get the uid and gid using the command `id $USER`, they are usually both 1000
```
sudo mount -t cifs //<server_ip>/<share_path> <mount_point> -o username=<username>,password=<password>,uid=<user_id>,gid=<group_id>
```

Once you are done testing the mount, you can unmount the remote server before setting it up permanently
```
sudo umount <mount_point>
```

For better security, you should use a credentials file

```
sudo nano /root/.smbcredentials
```

Then add this information to the file
```
username=<username>
password=<password>
domain=<domain> (if applicable)
```

Set the access permisions of the file
```
sudo chmod 600 /root/.smbcredentials
```

If you would like to test the credentials file, you can mount 
```
sudo mount -t cifs //<server_ip>/<share_path> <mount_point> -o credentials=/root/.smbcredentials,uid=<user_id>,gid=<group_id>
```

To make the mount persistent, edit the fstab file
```
sudo nano /etc/fstab
```

Add this content to the file
```
//<server_ip>/<share_path> <mount_point> cifs x-systemd.automount,_netdev,credentials=/root/.smbcredentials,uid=<user_id>,gid=<group_id>,vers=3.1.1,cache=none,actimeo=1  0 0
```

You can test the fstab file
```
sudo systemctl daemon-reload
sudo mount -a
```

Please note that the mount requires the system to wait for the network to be up before running fstab. The part of the fstab entry - `x-systemd.automount,_netdev,` is what does this. It assumes you have systemd in you Linux distribution. If you don't know what systemd is, you probably have it, as most mainstream linux distros use it by default. If you are using a distro that doesn't have it, then you probably already know what to do. The cache and actimeo flags are there to reduce latency as files are added to the server directories.

---

&nbsp;

Once the drives are available to the Client, use the folder button on the front Camera panel to launch the File Browser. At the top of the Picture panel, use the three dot button to open the directory selection dialog and navigate to the appropriate remote location. Do likewise for the Video panel and the Client configuration is complete.

</details>

</details>

---

&nbsp;

</details>

</details>

<details><summary>Firewall Rules</summary>

&nbsp;

---

Cayenue requires network access to communicate with cameras in Stand Alone or Server mode. If the host computer uses a firewall, it may be necessary to enable some communications ports so that cameras can use the WS-Discovery protocol to announce their presence to the program.

Some Distributions come with ```firewalld``` pre-installed and configured. These commands will work with firewalld and present a common operation that other firewalls will implement in a similar fashion.

The firewalld package in some distributions includes pre-defined services for WS-Discovery which might manage this port automatically. If the service definition exists on your system, you can use the simpler command: 

```
sudo firewall-cmd --permanent --zone=public --add-service=ws-discovery-client
sudo firewall-cmd --reload
```

You can check for available WS-Discovery services with:

```
firewall-cmd --get-services | grep ws-discovery
```

To configure the service manually in the event that it is not included in the firewall services package.

To allow inbound traffic with a specific source port (source-port) in firewalld, you must use a rich rule. Standard port rules in firewalld filter traffic based on the destination port, so a more specific rule is needed to inspect the source port. The common use case for source port 3702/UDP is for WS-Discovery (Web Services Dynamic Discovery) protocols. 

Command to Allow Inbound Source Port 3702 

Run the following commands in your terminal to allow inbound UDP traffic from source port 3702 permanently: Add a rich rule to the desired zone (e.g., public) that accepts traffic where the source port is 3702.


```
sudo firewall-cmd --permanent --zone=public --add-rich-rule='rule family="ipv4" source-port port="3702" protocol="udp" accept'
sudo firewall-cmd --reload
```

```
sudo firewall-cmd --zone=public --list-rich-rules
```

The output should include the rule you just added. 

Cayenue in server configuration also requires ports to be opened for ONVIF, RTSP and HTTP servers. The following commands should achieve this

```
sudo firewall-cmd --permanent --add-port=8554/tcp
sudo firewall-cmd --permanent --add-port=8550/tcp
sudo firewall-cmd --permanent --add-port=8800/tcp
sudo firewall-cmd --reload
```

For client configuration to be able to listen for alarms from the server, open port 8080 on the multicast address 239.255.255.247 using rich rule

```
sudo firewall-cmd --permanent --zone=public --add-rich-rule='rule family="ipv4" destination address="239.255.255.247" port port="8080" protocol="udp" accept'
sudo firewall-cmd --reload
```

---

&nbsp;

</details>

<details>
<summary>Getting Started</summary>

&nbsp;

<image src="cayenue/resources/discover.png">

Discover

To get started, click the Discover button. A login screen will appear for each camera as it is found. The Settings tab may be used to set a default login that can be used to automatically submit login credentials to cameras. There is also an Auto Discover check box on the Settings panel.

Initially, cameras will populate the list using the default name provided by the manufacturer. To change the camera name, use the F2 key, or the right click context menu over the camera list.

<image src="cayenue/resources/play.png">

Play

Upon completion of discovery, the camera list will be populated. A single click on a camera in the list will display the camera parameters in the lower part of the tab. Double clicking will start the camera output stream. The camera stream may also be started by clicking the play button or by typing the enter key while a camera is highlighted in the list.

Multiple cameras can stream simultaneously. The application will add camera output to the display for each camera as it is started. The controls for camera operations apply to the current camera, which is the highlighted camera in the list on the camera panel. The current camera will have a thin white border around it in the display.

Network conditions, compute load or internal camera issues may cause buffer overflow in the application pipeline. The result may be that packets are dropped, which can degrade the quality of the stream. If packets are being dropped, the camera display will show a yellow border.

<image src="cayenue/resources/play_all.png">

Play All

The play action can be applied to all cameras simultaneously. There is a keyboard shortcut for this command `Ctl+A` if there are no cameras currently streaming.

<image src="cayenue/resources/stop.png">

Stop

When the camera stream is running, the play button for that camera will change appearance to the stop icon. Clicking the button will stop the stream.  The stream for the highlighted camera can also be stopped by typing the enter key, or selecting from the right click pop menu.

<image src="cayenue/resources/stop_all.png">

Stop All

The stop action can be applied to all cameras simultaneously. There is a keyboard shortcut for this command `Ctl+A` if there are any cameras currently streaming.

<image src="cayenue/resources/record.png">

Record

Recording can be initiated manually by clicking the record button. The file name is generated automatically and is based on the start time of the recording in date format as YYYYMMDDmmSS.mp4. The `Settings -> Storage -> Archive Directory` setting will determine the location of the file. A subdirectory is created for each camera to help organize files within the archive.

During manually initiated recording, a rotating red colored tick mark will show in the lower right corner of the stream display. The Record Button on the Camera Panel will show red during all recording operations. Note that recording initiated automatically during Alarm conditions or Record Always will disable the Record Button. 

Files created by the application are limited in length to the setting on `Settings -> Storage -> Max File Duration`, which is by default 15 minutes. Recordings that require a longer time will be broken up into several parts that are each that length of time (15 minutes e.g.) long. There will be a slight overlap between files broken up this way corresponding to the length of the Pre Record Buffer setting, which can be found at `Settings -> Alarm -> Pre-Alarm Buffer Size`.

<image src="cayenue/resources/history.png">

File Operations

Picture and Video files generated by the system can be viewed and managed with a built in file browser. See the File Operations section of this document for more details.

<image src="cayenue/resources/snapshot.png">

Snapshot

A snapshot of the currently selected camera cna be saved as jpg file. The snapshot will be named by the system using YYYYMMMDDHHmmSS.jpg format, unless otherwise specified in the file save dialog. The file save dialog can be suppressed using the checkbox labeled "Snapshot File Dlg" on the `Settings->General` tab. There are two modes under which files may be saved, Local and Remote. The Local mode will use the stream currently displayed and convert that to a picture format. This mode will preserve the aspect ratio of the stream and any artifacts such as AI boxes drawn on the image. The Remote mode will address the camera directly through the network and request a snapshot of the Record Profile for the camera. This will generally be a higher resolution image and may be subject to latency or camera network errors. In the event that the camera fails to deliver the image, the Local mode will be used as a fallback.

<image src="cayenue/resources/apply.png">

Apply

Camera parameters are available on Cameras panel tabs on the lower right side of the application. Initially, the Apply button will be disabled with a dimmed icon. Once a parameter has been changed, the Apply button will be enabled, which can be used to commit the change to the camera. The camera may re-start the stream in order to make the changes.

<image src="cayenue/resources/full_screen.png">

Full Screen

Toggle the application between full screen and normal mode. This feature is also available from the F12 key.

<image src="cayenue/resources/audio.png">

Mute

Camera audio can be controlled from the panel. The mute button can be clicked to mute the audio. The mute button appearance indicates the state of the audio. The volume slider can be used to control the volume. Note that the mute and volume controls are applied to each camera individually.

<image src="cayenue/resources/help.png">

Help

Opens the system web browser to this page.

<h2>Keyboard Bindings</h2>

Many of the above functions can be executed without using the mouse via keyboard bindings. Below is a list of the bindings

<b>Enter</b>

This will start the currently selected camera. If the camera is already running, the Focus window will show with the high resolution camera stream. Please note that the first time the Focus window launches, the application focus will transfer to that window.

<b>Escape</b>

If the Focus window is visible, the Escape key will hide it. If Focus window is not visible, the camera stream is stopped.

<b>Ctl+D</b>

Start Discovery

<b>Ctl+A</b>

Start/Stop all cameras

<b>Ctl+F</b>

Open the File Browser

<b>Ctl+S</b>

Take a snapshot for the currently selected camera if running

<b>Ctl+R</b>

Toggle recording for the currently selected camera if running

<b>F1</b>

Show stream information for a running camera

<b>F2</b>

Rename the currently selected camera

<b>Delete</b>

Remove the currently selected camera from the list. This will remove the camera from the Cached Addresses for discovery. Use broadcast discovery to re-enlist the camera.



---
&nbsp;
</details>

<details>
<summary>Camera Parameters</summary>
&nbsp;

<i>Changes are committed to the camera by using the Apply button, if necessary.</i>

---

<details>
<summary>Media</summary>

&nbsp;

<image src="assets/images/media_tab.png" width="400"/>

&nbsp;

* ### W x H (Resolution)

    Camera resolution is adjusted using the combo box which has available settings. To change the camera resolution, make a selection from the combo box and then click the apply button. The camera may re-start the video stream in order to effect the change.

* ### Aspect

    When using substreams, the aspect ratio may be distorted. Changing the aspect ratio by using the combo box can restore the correct appearance of the video. If the aspect ratio has been changed this way, the label of the box will have a * appended. This setting is not native to the camera, so it is not necessary to click the apply button for this change.

* ### FPS

    Frame rate of the camera can be adjusted using the spin box. The change is made on the camera when the apply button is clicked. Higher frame rates will have a better appearance with smoother motion at the expense of increased compute load.

* ### GOP

    Keyframe interval of the video stream. Keyframes are a full frame encoding, whereas intermediate frames are differential representations of the changes between frames.  Keyframes are larger and require more computing power to process. Higher GOP intervals mean fewer keyframes and as a  result, less accurate representation of the video.  Lower GOP rates increase the accuracy of the  video at the expense of higher bandwidth and compute load. It is necessary to click the Apply button to enact these changes on the camera.

    Note that some cameras may have an option for Dynamic GOP or Adaptive Framerate, or some other name for a process that reduces the GOP automatically based on the lack of motion in the camera view. It is advised to turn this feature off when using Cayenue. To access the feature, use the camera web application from the `Cameras -> System -> Browser` button.

* ### Bitrate

    The bitrate of the video stream. Higher bitrates increase the quality of the video appearance at the expense of larger file sizes. This is most relevant when maintaining recordings of videos on the host file system. Bitrates are generally expressed in kbps by cameras, but may be inaccurate or scaled differently.  Use the Apply button after changing this setting to enact the change on the camera. Please note that generally, the bitrates of the Display and Record Profiles are independent. To adjust the bitrate of a profile, it must be made the Display profile in order to change the value.

* ### Profile

    Most cameras are capable of producing multiple media streams. This feature can be useful when running many cameras on the same computer or if a compute intensive task is being run on a stream. The default stream of the camera is called the Main Stream. A secondary stream running at lower settings is called the Sub Stream. The application uses the terms Display Profile and Record Profile to describe these settings.

    Initially, the Main Stream is selected by default as both the Display Profile and the Record Profile. By changing the selection to a secondary profile on the Media Tab, a lower order Sub Stream can be displayed. The term lower order implies that the Sub Stream has lower resolution, lower frame rate and lower bitrate than the Main Stream. Note that the application may be processing both streams, but only the Display Profile selected on the Video Tab is displayed. The other stream, referred to as the Record Stream, is not decoded, but its packets are collected for writing to disk storage.

    The display will update automatically when the Video Tab Profile combo box is changed, so it is not necessary to click the Apply button when changing this setting.

    In order to set parameters for a given profile, it must be made the Display profile in order to make any changes, after which it can be set back to the Record profile if desired.

* ### No Audio

    Audio can be disabled by selecting this check box. This is different than mute in the sense that under mute, the audio stream is decoded, but not played on the computer speakers. If the No Audio check box is selected, the audio stream is discarded. If the No Audio checkbox is deselected, the stream will restart in order to initialize the audio. The Apply button is not clicked when changing this parameter. This checkbox is selected by default.

    <b>** Please Note **</b> If the audio is enabled by deselecting this check box, and there is no physical audio device connected to the computer, there may be issues with stream processing. If an Audio Driver is specified on the `Settings -> General` panel such as pulseaudio, there should be a physical audio device such as headphones, speakers or HDMI connected to the host computer. Without a physical device, it may be possible in some cases for the audio driver to enter an undefined state which may cause the camera stream to stutter or freeze and may lead to lengthy timeouts when closing the camera stream. If there is no physical device available, the Audio Driver can be changed to dummy in order to avoid this problem. This condition applies only to camera streams which are displayed to the user interface. The Record Stream, if different than the Display Stream, is hidden and is not affected by this condition.

* ### Audio

    The audio encoder used by the profile is set here.  If the camera does not have audio capability, the audio section will be disabled. Note that some cameras may have audio capability, but the stream is not available due to configuration issues or lack of hardware accessories.  Available audio encoders will be shown in the combo box and may be set by the user. Changes to the audio parameter require that the Apply button is clicked to enact the change on the camera.
    
    AAC encoding is a higher quality stream and is recommended for recording. G711 style encoders are good for low latency playback if real time operation is important. Streams using AAC encoding map to mp4 file format and G711 uses mov. Note that some cameras have incorrect implementations for encoders and the audio may not be usable in the stream recording to disk. Please be aware that currently Cayenue is unable to process G726.

* ### Samples

    Available sample sizes are shown in the combo box. Use the Apply button to enact the change on the profile.  Higher sample sizes increase the quality of the audio at the expense of higher bandwidth and disk space when recording. Lower sample sizes correlate to lower latency. The audio bitrate is implied by the sample size based on encoder parameters.

* ### Video Alarm

    This check box enables video analytic processing for alarm generation. See the section on Video Panel for reference to video alarm functions.  Note that the Video Alarm check box must be selected in order to enable the Video Panel for that camera. The Apply button is not used for this setting. During Alarm condition, a solid red circle will show in the stream display if not recording, or a blinking red circle if the stream is being recorded.

* ### Audio Alarm
 
    This check box enables audio analytic processing for alarm generation. See the section on Audio Panel for reference to audio alarm functions.  Note that the Audio Alarm check box must be selected in order to enable the Audio Panel for that camera. The Apply button is not used for this box. During Alarm condition, a solid red circle will show in the stream display if not recording, or a blinking red circle if the stream is being recorded.


</details>

<details>
<summary>Image</summary>

&nbsp;

<image src="assets/images/image_tab.png" width="400"/>

&nbsp;

The sliders control various parameters of the video quality.  The Apply button must be clicked after changing the setting to enact the change on the camera.

</details>

<details>
<summary>Network</summary>

&nbsp;

<image src="assets/images/network_tab.png" width="400"/>

&nbsp;

If the DHCP is enabled, all fields are set by the server, if DHCP is disabled, other network settings may be completed manually. Note that IP setting changes may cause the camera to be inaccessible if using cached addresses. Use the Discover button to find the camera, or enter the new address manually from the settings panel.

Take care when changing these settings, the program does not check for errors and it maybe possible to set the camera into an unreachable configuration. 

The Apply button must be clicked to enact any of these changes on the camera.

---

</details>

<details>
<summary>PTZ</summary>

&nbsp;

<image src="assets/images/ptz_tab.png" width="400"/>

&nbsp;

Settings pertain to preset selections or current camera position. The arrow buttons, Zoom In (+) and Zoom Out (-) control the position and zoom. The numbered buttons on the left correspond to preset positions. Clicking one of the numbered buttons will send the camera to the corresponding preset position. To set a preset, position the camera, then check Set Preset, then click the numbered preset button. It is not necessary to use the Apply button with any of the settings on this panel.

---

</details>

<details>
<summary>System</summary>

&nbsp;

<image src="assets/images/system_tab.png" width="400"/>

&nbsp;

* ### Recording

    The check box at the top of the Record group box will enable automatic recording of camera streams when selected. The Record Profile combo box below will select the camera profile to be recorded.
    
    If the Record Alarms radio button is selected, the application will record automatically during alarm condition. While the stream is being recorded during alarm condition, there will be a blinking red circle in the lower right corner of the stream display. File sizes are limited by default to 15 minute lengths, so multiple files will be created if the alarm condition lasts longer than this limit. The limit may be adjusted.

    Selecting the Record Always radio button will cause the application to record the camera at all times that it is streaming. The files are written to disk in 15 minute file lengths, and are named in a time format representing the start time of the recording. Unlike other recording modes, the Record Always condition does not display an indicator in the stream display.

    It not necessary to use the Apply button for any of the settings on this panel.

* ### Alarm Sounds

    The check box at the top of the Sounds group box will enable alarm sounds on the computer speaker when checked.  If the Loop radio button is selected, the sound will play continuously during an alarm condition.  Selection of the Once radio button will cause the application to play the alarm sound once per alarm condition.

* ### Record Profile

    The drop down box can be used to the select the camera profile that will be recorded to disk. The Record Profile can be different than the Display Profile shown in the application. This setting can be used most effectively when the application is configured to show the low resolution substream profile in the display, and use the high resolution main profile as the recording source. This enables the application to maintain real time display status, especially with multiple streams, while preserving high resolution accuracy in the recorded stream. Because the recorded stream in not decoded, but rather is piped directly from the camera to disk, the high resolution recording presents very little compute load on the host. Note that is changes to the parameters of the profile settings are required, the profile must be made the current Display profile.

* ### Record Audio

    In many cases, the audio of the Display Profile will be disabled. By default, audio is disabled for camera streams. This is particularly relevant when displaying multiple streams, as the audio from multiple cameras playing simultaneously may cause confusion. This checkbox allows the display audio to be disabled while preserving audio on the recorded stream.  

* ### Remote Snapshot Image

  By default, this option is disabled, which means that the system will use the currently playing camera Display stream as the source for snapshot images. If the display stream is a low resolution stream, the snapshot will also be the same low resolution. If the YOLO detector is running and the Show Alarms on Display is enabled from `Settings -> Alarms`, detection boxes shown on the stream will be present on the snapshot image. This may be useful behavior when initially configuring the system when false positive detections are occurring, as the detection boxes will show the origin of the alarm.

  If a high resolution snapshot image is desired, this might be possible depending on the camera capabilities. Most, but not all cameras will expose a high resolution still image source available over the network. Some cameras will provide this capability in the spec, but in practice the image may not be usable. Experimentation is required to determine if the camera output is acceptable. In the event that the camera fails to deliver the image during runtime, the system will fall back to stream image capture. 

* ### Reboot

    Click to reboot the camera.

* ### Browser

    This will launch the web browser and connect to the camera.  Cameras will have a web interface that can be used to set parameters that are not available to the application.

* ### Sync Time

    Clicking the Sync Time button will bring up a dialog box with time settings options for the camera.

    &nbsp;

    <image src="assets/images/sync_time.png" width="640">

    &nbsp;

    At the top of the dialog are boxes showing the current settings for computer time and camera time respectively. The camera time is calculated based on the time offset parameter used by the computer for authentication. This time should, but may not necessarily, closely match the time displayed by the camera in the video stream. Variations in how cameras compute time may result in an offset mismatch between the time displayed in the camera video stream and the computed time shown on the dialog.

    The Time Zone and Daylight Savings Time fields can be edited by the user and set in the camera for configuration. 
    
    The Time Zone format can vary and different cameras will accept different formats. The long format shown in the example resembles POSIX standard and is the most comprehensive format which includes time offset from UTC and DST offset with DST start and finish parameters. Most cameras do not conform entirely to this standard, but may accept the string while selectively ignoring portions of the configuration. The most widely accepted form is UTC format or alternately, GMT format both of which have an optional +/- sign and hour plus optional minute offsets delimited by colon. Examples might be UTC0 or UTC-04:00. The GMT format is the same, but note that the polarity of the sign is reversed e.g. GMT0 or GMT+04:00. Other formats may possibly work e.g. EST5EDT, which may be worth trying.

    The Daylight Savings Time checkbox can be edited by the user, or it may be set automatically by the camera depending on the camera abilities. Not all cameras support DST, and some may save the DST flag but not act on the information when computing time.

    The Time Sync Method group box selects the time adjustment strategy used by the application.

    NTP Time setting will enable the NTP server box to allow editing. There are three types of server configuration. From DHCP will instruct the camera to use the NTP server data from the most recent DHCP configuration. This may or may not be the server data from the DHCP. In many cases, this will be a hardcoded address in the camera firmware. IPv4 address will use a numeric style IP address for the NTP server. A failure of this parameter configuration may or may not produce an error message from the camera. A Domain Name style server configuration will use a dot notation server name similar to a web address and will require proper DNS configuration for resolution. Once configured, the camera will use the Time Zone and DST information it has stored in its settings to deduce its time from the NTP server response to the camera query. In all cases, if the NTP server address is located on the internet the camera will require internet access in order to contact the server.

    Manual Time Setting will use the computer hosting the application to derive the time sent to the camera. The computer will send a UTC time to the camera and the camera will calculate its time based on the Time Zone and DST information that it has in its settings.

    UTC as Local setting is a specific type of manual setting that will force the camera into displaying the same time as the computer host. This is done by setting the camera Time Zone to UTC0 and setting the time on the camera to match the application computer host time. As UTC time is not dependent on DST, issues associated with DST can be ignored. If the computer time is accurate and regularly updated, this can be a good strategy for many cameras, as it circumvents a lot of ambiguity in time setting configurations which may be inaccurate or outdated. Note that some cameras, if connected to the internet, may eventually resort to hidden NTP settings that will reset the camera time (often incorrectly) if this strategy is employed. If a camera is using this type of NTP access, it is advisable to isolate it from the internet as a security precaution. If this is not practical or desired, the time zone and DST settings can be used such that the camera perhaps might display the correct time.

    Ultimately, there are many variations and inconsistencies when dealing with camera times. In most cases, UTC as Local with cameras isolated from the internet will provide the best results. Camera algorithms for time setting are often opaque and in many cases incomplete or incorrect. Cameras with proper time setting implementations can be set using the Time Zone and DST settings, but should be verified for accuracy and completeness, especially regarding DST. NTP use is discouraged, as cameras should be isolated from the internet as a security precaution. Using an NTP server on the internal network does not provide any advantage over Manual time setting via the application host computer.

</details>

---

&nbsp;
</details>

<details>
<summary>File Operations</summary>
&nbsp;

<i>Camera recordings can be viewed from within the application. Files can be searched for a particular moment in time. A server can share recordings using Samba so that Windows, Mac and Linux clients can view previously recorded streams from the server.</i>

<i>Snapshots generated by YOLO alarms or taken manually by the user are automatically linked to existing Video files such that activating play from the Picture panel will show the associated Video file starting at the time at which the snapshot was taken.</i>

<i>Keyboard bindings make file review effortless and responsive so that pictures and relevant videos can be searched and viewed quickly and easily.</i>

---

&nbsp;

The application maintains folders for the storage of camera snapshots and recordings. The folder locations by default are the OS picture and video storage locations, and can be changed using the directory setting at the top of the panel. There is a subfolder for each camera that has previously made pictures or recordings in the application. If you are using Cayenue as a client, and the server is configured to share files using Samba, you can use the server shared folder to access recordings made on the server. 

Inside the camera folders are the individual picture or video files recorded by the camera. The files are named using a datetime convention which represents the time that the snapshot images was taken or the start time of the video recording. Video recordings are prepended by a time interval specified on the `Settings -> Alarm -> Pre-Alarm Buffer Size`. This insures that the moments immediately prior to the beginning of the recording are captured.

&nbsp;

<image src="assets/images/picture_panel.png" width="500">

&nbsp;

<image src="assets/images/file_panel.png" width="500">

&nbsp;

Double clicking on a picture file will start the associated video playing at the time stamp of the picture. The same action can be started using the Enter key when a picture file is highlighted. In the event that there is not video coverage for the picture timestamp, the playback will fail silently. While a video is playing, using the Escape key will return operation to picture browse mode. Using the up and down arrow keys will traverse the picture directory contents, showing each picture as the selection changes. Folders can be opened and closed using the Enter key. Right clicking over the file will bring up a context menu with various options.

File playback is configured such that one file is played at a time. Keyboard shortcuts are available for faster navigation. Video playback controls are available on either the Picture or Videos panel.

<h3>File Playback Controls For Mouse</h3>

<image src="cayenue/resources/search.png"> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <image src="cayenue/resources/refresh.png"> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <image src="cayenue/resources/snapshot.png">

Search&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Refresh&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Snapshot

<image src="cayenue/resources/play.png"> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <image src="cayenue/resources/pause.png"> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <image src="cayenue/resources/stop.png"> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <image src="cayenue/resources/previous.png"> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <image src="cayenue/resources/next.png"> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <image src="cayenue/resources/audio.png">

Play&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Pause&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Stop&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Prev&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Next&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Mute

---

### Keyboard Shortcuts

Keyboard shortcuts are available when the file list of either the Picture Panel or the Video Panel has the application focus. A single click on any file or folder in the list will achieve this focus. Keyboard operations may be significantly faster than using the mouse when browsing through files.

* <h3>Enter</h3>

  The Enter key can be used to Play the file. Note that if another file is currently playing, it will be stopped before the new file starts.

* <h3>Space</h3>

  The space bar can be used to Pause the current file playing.
    
* <h3>Escape</h3>

  The Escape key can be used to stop the current file playing.
    
* <h3>Delete</h3>

  Files may be deleted by typing the Delete key.

* <h3>F1</h3>

  The F1 key will show a dialog with file properties.
    
* <h3>F2</h3>

  Files can be renamed using the F2 key.
    
* <h3>Right Arrow</h3>

  The Right Arrow will fast forward the file playing by 10 seconds.
    
* <h3>Left Arrow</h3>

  The Left Arrow will rewind the file playing by 10 seconds.

* <h3>Up Arrow</h3>

  The Up Arrow will move to the previous file without stopping the current file. Use the Enter key to start playing the newly highlighted file.

* <h3>Down Arrow</h3>

  The Down Arrow will move to the next file without stopping the current file. Use the Enter key to start playing the newly highlighted file.

### Progress / Seek Indicator

Both File Panels have a progress bar that will show the state of the playback. The total duration of the file is shown on the right hand side of the progress bar, and the left hand side will show the current file position which is indicated by the progress bar handle. If the mouse hovers over the bar, the position within the file will be shown above. The seek function will set the file position to the mouse location if the mouse is clicked on the progress bar. Sliding operation is not supported. Note that the seek function depends on the GOP size, so an extremely long GOP will reduce the number of seek points available in the video.

### Pop Up Menu

Right clicking over the file will bring up a context menu that can be used to perform file operations.

### File Searching by Time

The application has the ability to search the files by camera for a particular moment in time.

&nbsp;

<image src="assets/images/file_search.png">

&nbsp;

The search dialog is launched by clicking the search icon on the File panel. Use the dialog box to select a Camera, Date and Time and the application will search the files for that particular moment. If found, a confirmation box will pop up and the file can be played directly. The application will automatically highlight the file in the list and forward the playback to a moment near the selected time. There may be a slight offset corresponding roughly to the Pre-Alarm Buffer Size from the Settings -> Alarm panel.

If the application was not able to find the exact match, a pop up box will ask if you want to play the closest file in time. Note that the application will highlight this closest match in the file list, so you could use that as a starting point for navigating through the files.

### Refresh File View

The files listed in the panel my not be updated automatically. Use the refresh icon to get a current listing of the files available for view.

---

&nbsp;

</details>

<details>
<summary>Application Settings</summary>
&nbsp;

---

## General Settings

&nbsp;

<image src="assets/images/general.png" width="400">

&nbsp;

### Common Username and Password

Default camera login credentials. If there is a camera on the list that does not share these credentials, a pop up login box will appear during discovery. It is possible to add these alternate credentials into the stored profile of the camera by right clicking over the camera in the list and selecting the password option, which will silently add the credentials to the stored settings so that the camera can be discovered without having to type in the credentials.

### Hardware Decoder

A hardware decoder may be selected for the application. Multicore CPUs with more than a few cores will handle the decoding just as easily as a hardware decoder. Smaller CPUs with a small number of cores may benefit from hardware decoding. VAAPI and VDPAU pertain to Linux systems and DXVA2 and D3D11VA are for Windows. CUDA decoding is platform independent and requires NVIDIA GPU. For most Linux installations, this selection will not be implemented. NVIDIA GPU configuration on Linux will work if configured properly, and Windows hardware acceleration is also implemented generally.

### Start Full Screen

Selecting this check box will cause the application to start in full screen mode. The full screen mode can be canceled with the Escape key. The F12 key will also toggle full screen mode.

### Auto Time Sync

This selection will send a time sync message to each of the cameras once an hour. The camera time is set according to the parameters defined in the Sync Time dialog box described in Camera Parameters shown above.

### Snapshot File Dlg

When selected, a dialog box will appear when a snapshot is requested so that the picture file name can be changed for saving. Deselecting this checkbox will cause the system to automatically accept the generated file name without showing the dialog. Please note that the system uses the automatically generated filename to determine the snapshot time when searching video files, so changing the filename will disable the search functionality.

### Display Refresh Interval

Performance on some lower powered systems may be improved by increasing the display refresh interval.

### Open New Window

Manage profiles for secondary windows used to display a camera or a group of cameras separately from the main application window.

The default 'Reader' profile is a reserved profile that launches a specialized secondary File panel browser that can operate with it's own configuration for viewing files. The secondary File panel can be used during camera operation without interfering with the main program.

The default 'Focus' profile is a reserved profile that is integrated into application logic. The Focus Window can be launched by double clicking on a camera stream in the main display and can show that camera at higher resolution and frame rate for a more detailed view. The Focus Window will show only one camera at a time. The application will automatically configure the Focus settings for proxy type and auto discovery.

Additional profiles can be added using the three dot button to the right of the drop down box that will launch a configuration dialog box.

&nbsp;

<image src="assets/images/profile.png" width="360">

&nbsp;

New Windows can be configured to show specific groups of cameras, which can be useful if the host computer is driving several monitors such that different groups of cameras are shown on different monitors. The Open button will launch a window with the profile selected in the drop down box. Each profile will have a separate configuration that is set by the user.

It may be useful to create a profile exclusively for viewing camera recordings from the File tab. This way the window can be configured with a larger navigation panel showing more complete file information. Additionally, the camera panel can be hidden in this profile so that the window opens directly to the file list.

### Show Logs

This button will show the logs of the application. Many events and errors encountered will be documented here. The log rolls over at 1 MB. The older logs can be managed using the Archive button on the logs display dialog.

### Help

Shows this file.

### Hide Display

If running Cayenue in server configuration, it may be desirable to run in headless mode. If this is the case, hiding the display will significantly reduce compute load by bypassing the rendering routines. In this configuration, the compute load will be similar to that of a console application. Once the display is hidden, the text of the button will change to Show Display with appropriate functionality.

### Clear All Settings

This will clear all settings for the application, including the File Reader settings.

## Discover Settings

&nbsp;

<image src="assets/images/discover.png" width="400">

&nbsp;

### Discovery Options

* Discovery Broadcast

  This option will broadcast a discovery packet to find cameras on the local network. If the host computer is attached to multiple networks it is possible to broadcast across all networks or only one selected network. Cameras discovered will have their data entered into the address cache so that they may be found without discovery later.

* Cached Addresses

  This option will cause the application to find cameras based on the cache data rather than the discovery broadcast. Note that cameras may be deleted from the cache by using the Delete key or the right click context menu on the camera list. This can be useful if a subset of cameras on the network is going to be streamed. Note that some cameras may respond with incomplete data when using a cached address.

* Add Camera

  It is possible to add a camera manually to the address cache by using the Add Camera button. The IP address and ONVIF port are required to connect.  The ONVIF port by default is 80. If successful, the camera will be added silently to the camera list. If a camera is added manually using this method, it will not persist in the interface unless the Cached Addresses option is selected.

### Auto Discovery

When selected, this option will cause the application to discover cameras automatically when it starts. This holds true whether the application is using Broadcast Discovery or Cached Addresses.  Note that if this option is selected and the Broadcast Discovery Option is also selected, the application will poll the network once per minute to find missing or new cameras.

### Auto Start

When selected in combination with the Auto Discovery check box, cameras shown in the list will start automatically when the application starts. This feature will work with either Discovery Broadcast or Cached Addresses.

## Storage Settings

&nbsp;

<image src="assets/images/storage.png" width="400">

&nbsp;

### Disk Usage

The application has the ability to manage the disk space used by the recorded media files. This setting is recommended as the files can overwhelm the computer and cause the application to crash. Allocating a directory for the camera recordings is done by assigning a directory using the Archive Dir selection widget. The default setting for the Archive Dir is the user's Video directory. It is advised to change this setting if the host computer employs the user's Video directory for other applications.

* Current Disk Usage

  When the application starts, or a new file is created for a camera recording, the approximate amount of disk space used by the application is displayed. This number is not exact, but can give a general idea of the amount of disk space used.

* Auto Manage Checkbox

  Select this check box to enable disk management.  A warning dialog will inform the user of the risk of the loss of files within the directory. Note that the application will only delete files that conform to the date style file naming convention that it uses. It is a good idea to use a directory that can be dedicated exclusively to the application.

  The maximum available disk space that could be allocated to the application based on the Archive Dir setting will be displayed next to the checkbox.

  The spin box can be used to limit the application disk usage in GB. Note that the application is conservative in it's estimate of required file size and the actual space occupied by the media files will be a few GB less than the allocated space.

* Archive Directory

  This widget sets the storage location for Video files generated by the system. Note that the location here is independent from the Videos panel of the File browser.

* Picture Directory

  This widget sets the storage location for Picture files generated by the system. Note that the location here is independent from the Pictures panel of the File browser.

### Max File Duration

  Video file duration is limited to this length. This is done so that Video files do not become excessively large. Video files will be padded at the start by the duration configured on the Settings -> Alarm tab Pre-Alarm buffer size, which by default is ten seconds. This insures some overlap between adjacent files so that information is not lost when files are truncated.

### File Write Buffer Size

  File management will remove oldest files based on the total size limit set in the Auto Management field. Because the calculation used by the manager is not exact, an additional buffer space is allocated for safety. The default value should be sufficient, but can be adjusted based on conditions if warranted.

## Proxy Settings

&nbsp;

<image src="assets/images/proxy.png" width="400">

&nbsp;

## Proxy Type

* Stand Alone

  Default setting, implements a single instance of the program that connects to the cameras directly.

* Client

  The application will act as a client to the proxy server using a connection string corresponding to one displayed by the server in the url box. If the connection string is changed, the Update button must be clicked to enact the changes. If the server is capable of generating detections, they can be received or ignored by the client using the 'Get alarm events from server' checkbox. If the server detections are not enabled, the client may generate detections locally if desired.

  If the server detections are enabled, the application will look for the interface that matches the subnet of the server. If the server address has been entered incorrectly, this condition will prompt an error message and the event listener will not be instantiated.

* Server
  
  The application will host a proxy server and allow other instances of the application configured as clients to connect over the local network to the cameras proxied by the server. The server backend is provided by [Media MTX](https://github.com/bluenviron/mediamtx). The application will download the appropriate binary executable file from the developer github page and copy it to the python environment bin folder. If you prefer to use your own Media MTX binary, the location can be set with the directory control.

  Diagnostic messages from the MediaMTX server may be visible in the terminal if the application is started from the command line. The Log Level selector can be used to tailor the verbosity of the messages.

* HTTP Server

  The application can host links to Video streams that can be accessed using a Web browser. The port number 8800.

* Alarm Broadcasting

  Alarm broadcasting by the server can be controlled using the 'Alarm Broadcasting' group box. This function will broadcast a single UDP packet containing the alarm states for all cameras on the server at an interval of once per second. The UDP packet can be received by any machine on the broadcast network.
  
  For server hosts running Windows, broadcasting is limited to the network with the highest priority. The Network combo box in this case will have only one entry which corresponds to the highest priority network. Please see the section in Notes -> Network Priority on Multi Homed Hosts to view instructions on how to set network priority. Linux and Mac OS hosts are able to select the network on which to broadcast alarms.

## Alarm Settings

&nbsp;

<image src="assets/images/alarm.png" width="400">

&nbsp;

### Pre-Alarm Buffer Size

When a camera is recording, this length of media is prepended to the file so that the moments prior to the alarm are preserved. If always recording, or the file length is limited by the system, this feature will insure that there is a small overlap between adjacent files.

### Post-Alarm Lag Time

In the case where a camera is configured to record during alarms, this length of time must pass after the cessation of the alarm before the file recording is turned off.  This helps to prevent excessive file creation. Alarm display and alarm sound functions are affected by this setting as well.

### Alarm Sounds

A few default alarm sounds for selection.  A system wide volume setting for the alarm volume can be made with the slider.

### Show Alarms on Display

When selected (default is yes) a red filled circle will be displayed on the camera stream during alarm conditions. The circle will blink if the stream is being recorded during an alarm. De-selecting this checkbox will show the camera stream without any alarm markings.

### Save Picture for Alarms

When selected (default is yes) a picture will be saved to the Pictures directory each time an alarm is triggered. The pictures are used to populate the Event Browser accessible from the File panel which can be used to view videos at the time point of the alarm.

---
&nbsp;
</details>

<details>
<summary>Video Panel</summary>
&nbsp;

<i>Video streams cam be analyzed to generate alarms.</i>

---

The Video Panel has multiple modes of operation. The default setting is for motion, which can be used without further configuration and will run easily on a CPU only computer. YOLOX requires the installation of additional python packages, namely pytorch and openvino. YOLOX will perform well on recent Apple Silicon M chips, NVIDIA GPU, and Intel Xe, UHD or ARC Graphics.

In order for the panel to be enabled, either a camera or a file must be selected. If a camera is selected, the Video Alarm check box must also be selected on the Media Tab of the Camera Panel. If a file is selected, the Enable File check box on the Video Panel must be selected.

Parameters set on the panel are applied to files globally, and to cameras individually.

If the analysis produces an alarm, record and alarm sound actions are taken based on the settings made on the System Tab of the Camera Panel. Files are not connected to alarm processing.

<details>
<summary><b>Motion Detection</b></summary>
&nbsp;

<i>Motion detection is useful in lower powered systems without AI processing capabilities</i>

---

&nbsp;

<image src="assets/images/motion.png" width="640">

&nbsp;

The motion detector measures the difference between two consecutive frames by calculating the percentage of pixels that have changed. If that result is over a threshold value, an alarm is triggered. The Diff check box will show a visualization of the differential pixel map that is used by the calculation. The status bar will light green to red as the value of the algorithm result increases. The Gain slider can amplify or attenuate the result to adjust the sensitivity of the detector. Higher Gain slider values increase the sensitivity of the detector.

Motion detection systems are prone to false alarms due to the indiscriminate nature of the analysis. They can be useful in settings where motion is limited, such as a controlled indoor environment. They are not recommended for general use, especially in outdoor settings.

---
&nbsp;
</details>


<details>
<summary><b>YOLOX</b></summary>
&nbsp;

<i>YOLOX is an AI powered analysis for detecting specific types of objects</i>

---

&nbsp;

<image src="assets/images/yolox.png" width="640">

&nbsp;

<b>Prerequisites</b>

YOLOX will run with hardware acceleration on Apple Silicon, NVIDIA GPU and Intel iGPU, NPU, or ARC Graphics.

<b>Installation Requirements</b>

<b>Please Note:</b>The installation scripts for Linux and Mac OS install the necessary python libraries automatically. The Linux installation scripts will install iGPU drivers on Intel chips automatically. If using NVIDIA GPU, those drivers are usually installed by default on modern Linux distros, but some may require manual installation. Windows users will need to install drivers and python libraries manually for the time being.

<b>Configuration</b>

The upper portion of the yolox panel has a model configuration box. Model parameters are system wide, as there will be one model running that is shared by all cameras. The Name combo box selects the model, which is named according to the size of the number of parameters in the model. Larger models may produce more accurate results at the cost of increased compute load. The Size combo box sets the resolution to which the video is scaled for model input. Larger sizes may increase accuracy at the cost of increased compute load. It is possible to change the backend API of the yolo detector by using the API combo box. The Device combo box will populate automatically with available hardware.

The model is initialized automatically by starting a camera stream with the Camera tab Video Alarm checked. By default the application is configured to download a model automatically when a stream is started for the first time. There may be a delay while the model is downloaded, during which time a wait box is shown. Subsequent stream launches will run the model with less delay.

A model may be specified manually by de-selecting the Automatically download model checkbox and populating the Model file name box. Note that if a model is manually specified, it is still necessary to assign the correct Name corresponding to the model parameter size.

The lower portion of the panel has settings for detector configuration. Parameters on this section are assigned to each camera individually.

Skip Frames spin box sets the number of frames to skip between model analysis runs. If the Skip Frames value is set to zero, every frame produced by stream is set through the detector. If the Skip Frames value is set to one, every other frame is sent through the detector, and so on. This setting can be used to reduce computational burden on the system.

The yolox detector samples a number of frames as set by the Samples setting. The number of frames with positive detections required to trigger an alarm is set by the Limit slider. For example, if the Sample Size is 4 and the Limit slider is set to 2, at least two of the last four frames observed must have positive detections in order to trigger the alarm.

There is also a Confidence slider that applies to the yolox model output. Higher confidence settings require stricter conformance to model expectations to qualify a positive detection. Lower confidence settings will increase the number of detections at the risk of false detections.

It is necessary to assign at least one target to the panel in order to observe detections. The + button will launch a dialog box with a list of the available targets. Targets may be removed by using the - button or the delete key while the target is highlighted in the list.

---
&nbsp;
</details>


---

&nbsp;
</details>

<details>
<summary>Audio Panel</summary>
&nbsp;

<i>AAC Audio streams can be analyzed to generate alarms.</i>

---

The audio panel can analyze streams in both amplitude and frequency domains. Note that frequency analysis requires slightly more computing power than amplitude analysis. Please note that only AAC encoded audio is supported at this time.

In order for the panel to be enabled, either a camera or a file must be selected. If a camera is selected, the Video Alarm check box must also be selected on the Media Tab of the Camera Panel. If a file is selected, the Enable File check box on the Video Panel must also be selected.

Parameters set on the panel are applied to files globally, and to cameras individually.

If the analysis produces an alarm, record and alarm sound actions are taken based on the settings made on the System Tab of the Camera Panel. Files are not connected to alarm processing.


&nbsp;

<image src="assets/images/audio_panel.png" width="400">

&nbsp;

* ### Amplitude

The amplitude is measured by calculating the Root Mean Square (rms) value of the audio waveform. If the rms exceeds threshold, an alarm condition is triggered. The Gain slider can be used to amplify or attenuate the value of the signal in order to adjust the sensitivity of the detector.

* ### Frequency

The frequency spectrum is measured by the integrated area under the spectrum curve normalized. The spectrum may be filtered to eliminate undesired frequencies. Lower frequencies are often common background sounds that do not warrant an alarm condition, whereas higher frequency sounds are often associated with a sudden, sharp noise such as breaking glass.

There are filter bars that can be adjusted using the cursor handles. Frequencies excluded by the filter are depicted in gray. The Gain slider can be used to amplify or attenuate the value of the signal in order to adjust the sensitivity of the detector.

---

&nbsp;

</details>

<details>
<summary>Full Screen</summary>
&nbsp;

---

The application windows can be configured to run in full screen mode. The F12 key is used to toggle full screen. If the application is running full screen, the Escape key can be used to return to windowed operation.

The control tab on the right of the application window may be toggled using the F11 key. On Mac, it is necessary to use the command key + F11 combination to override the default workspace action. The size of the control tab can be changed by dragging the left hand edge of the tab. Reducing the size of the tab beyond it's minimum will hide the tab. If there is at least one stream in the display and the control tab is hidden, clicking on the stream display area will restore the control tab.

---

&nbsp;

</details>


</details>


<details>
<summary>Notes</summary>

&nbsp;

<details>
<summary>Project Maintenance</summary>

&nbsp;

<details>
<summary>Updating the Repository</summary>

&nbsp;

Use the ```python -m build``` command to build the Cayenue python package and upload with twine. The official instructions for this process can be found on the [Python web site](https://packaging.python.org/en/latest/tutorials/packaging-projects/).

There are scripts for each operating system that will build the installers for Cayenue. The scripts are intended to be run on virtual machines and are designed to run on a freshly installed vm such that no configuration of the vm is required other than installation.

Version control is critical in the update process and requires edits in several locations that should be coordinated carefully.

<h3>cayenue</h3>

  * pyproject.toml (Including the cayenue version <u>AND</u> the dependencies section)
  * setup.py
  * main.py

<h3>flatpak</h3>

<i>Note that the flatpak YML configuration file uses the PyPi server location for the cayenue package, and needs to be updated for both x86 and aarch in addition to the XML file version designator.</i>

  * io.github.sr99622.Cayenue.yml (cayenue whl from pypi)
  * io.github.sr99622.Cayenue.metainfo.xml (release version)

<h3>snap</h3>

  * snapcraft.yaml

<h3>mac</h3>

  * Info.plist section of build_app

<h3>windows</h3>

  * cayenue.nsi (!VERSIONMAJOR  !VERSIONMINOR  !VERSIONBUILD)

&nbsp;

The build scripts can be found in the Cayenue source tree at assets/scripts. ```linux_build```, ```mac_build```, and ```windows_build.bat``` are the names of the scripts. The scripts are intended to be run on virtual machines. For Linux and Windows, QEMU will create the proper vm. Mac OS vms can be built with UTM virtual machine manager on Apple Silicon. Put the appropriate script in the home directory for each platform and execute. The script will pull the latest version of the source code and build the python binary installs. The linux_build script should be run on a vm with Linux Mint 21 installed using the vm_ scripts. The binary installs produced will work with any Linux kernel greater than 5.4. The mac_build script can be run on the Mac OS Sequoia or later. A Windows vm is most easily built using Windows 11 and the windows_build.bat will produce binary installs that will work for most modern Windows versions. 

&nbsp;

---

</details>

<details>
<summary>App Installer on Mac OS</summary>

&nbsp;

---

TLDR;

Use Finder to move existing /Applications/Cayenue to the trash, then run

```
cd $HOME/Cayenue
git pull
assets/scripts/components/mac/build_app
```

When finished, launch DMG Canvas and open the Cayenue.dmg file from Recent Files. Start by clicking the hammer icon. The installer file will be

```
$HOME/assets/scripts/mac/Cayenue.dmg
```

Rename it to Cayenue-x.y.z.dmg where x.y.z is the version number.

----------

Background Info

The script build_app in the assets/scripts/mac folder is used to build the MacOS installer DMG. The script relies on homebrew and will install it as the first action along with a few tools needed for compilation. The basic theory behind the installer is that a python virtual environment is built within the /Applications/Cayenue.app folder under the premise that this will be the location for any arbitrary installation. This is a critical assumption, as the location of the cayenue executable script is required for launching. Any exisiting Cayenue folder in the Applications folder should be removed prior to starting the build.

Once the app has been assembled in situ, the [DMG Canvas application](https://www.araelium.com/dmgcanvas) is used to build the DMG file and notarize it on the Apple Developer site. A valid developer subscription and certificate are required for this operation. It may also be necessary to have an app-specific password in the Keychain for the developer machine, although it is unclear if this is actually required. It is important to note that the app should not be launched from the build location after compile but prior to notarization, as artifacts created in the folder will invalidate the codesign. It has also been observed that running the DMG Canvas application twice in a row will fail the notarization the second time. A reboot has been found to avoid this problem.

 A good resource for understanding the app building process can be found at this [link](https://blog.xojo.com/2024/08/22/macos-apps-from-sandboxing-to-notarization-the-basics/)

---

&nbsp;

</details>

<details>
<summary>App Installer for Flatpak</summary>

&nbsp;

---

The script to build a flatpak can be found in the assets/scripts/components/flatpak folder. There is code for building the flatpak using either onvif-gui from PyPi or from a local file. If a local file is selected, you need to build it first using `python -m build` from the libonvif/onvif-gui folder then copy the whl file from the dist subdirectory to the flatpak folder.

To install flatpak-builder

```
sudo dnf install flatpak-builder
```

Flatpak needs to know the location of the Flathub repository. Because the flatpak will be built using the --user flag, you must also apply this flag when adding the remote repository.

```
flatpak remote-add --user --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo
```

You can list available remotes.

```
flatpak remotes
```

The flatpak can be built and installed using the following command. To build without installing, remove the `--install` flag.

```
flatpak-builder --force-clean --user --install-deps-from=flathub --repo=repo --install builddir $HOME/Cayenue/assets/scripts/flatpak/io.github.sr99622.Cayenue.yml
```

While the application is installed, a command prompt can run the container environment.

```
flatpak run --command=sh io.github.sr99622.Cayenue
```

To uninstall the application, use the command.

```
flatpak uninstall io.github.sr99622.Cayenue
```

To build a single file flatpak installer, run the command (this will take a while to run).

```
flatpak build-bundle repo Cayenue.flatpak io.github.sr99622.Cayenue
```

This can then be used to install the application.

```
sudo flatpak install Cayenue.flatpak
```

---

&nbsp;

</details>

<details>
<summary>App Installer for snap</summary>

&nbsp;

---

The script for building a snap is in the libonvif/assets/scripts/components/linux/snap folder. The commands to build the snap should be run from the parent of the snap folder i.e. libonvif/assets/scripts/components/linux. 

The first thing you need to do is to install snapcraft

```
sudo snap install snapcraft --classic
```

Then you have to [install and configure LXD](https://documentation.ubuntu.com/lxd/latest/tutorial/first_steps/#first-steps), permissions should do it. A reboot is needed to complete.

```
sudo snap install lxd
sudo usermod -aG lxd "$USER"
newgrp lxd
lxd init --minimal
sudo reboot now
```

To build the package, use the command from the directory which is the parent of the snap directory containing snapcraft.yaml

```
snapcraft
```

There will be a large volume of error messages and such. Most can be ignored, but some may be relavant. If it doesn't work, then you can comb through the messages and look for things. If it does work, it's fine. You can run the command as `snapcraft --debug` flag to drop into a shell if the process fails.

Sometimes, the system will cache parts of the build that can cause actual errors, to clean the cache

```
snapcraft clean
```

To install the package

```
sudo snap install cayenue*snap --dangerous
```

To get audio working, you should be on pulse audio (which is the default). From the terminal, run the command

```
sudo snap connect cayenue:pulseaudio
```

To uninstall

```
sudo snap remove cayenue
```


The yaml configuration file includes code for installing the NPU driver, which requires separate installation. 

```
sudo snap install intel-npu-driver
sudo chown root:render /dev/accel/accel0
sudo chmod g+rw /dev/accel/accel0
sudo usermod -a -G render $USER
sudo bash -c "echo 'SUBSYSTEM==\"accel\", KERNEL==\"accel*\", GROUP=\"render\", MODE=\"0660\"' > /etc/udev/rules.d/10-intel-vpu.rules"
sudo udevadm control --reload-rules
sudo udevadm trigger --subsystem-match=accel
sudo reboot now
```

If it's not working, you can start a shell prompt to look around

```
snap run --shell cayenue
```

---

&nbsp;

</details>

<details>
<summary>App Installer for Windows</summary>

&nbsp;

---

There is a script that will handle most of the work for a windows installer build. ** Note ** the installer must be run from a command prompt with Administrator Privilege. The installer uses the NSIS program to build and the script will check if that is installed on the machine and download it if necessary. The basic concept for the installer is similar MacOS, in that the cayenue-env virtual environment is created in a known location that will be common across machines, in this case, C:\Program Files (x86).

The cayenue.nsi file is fed into the NSIS script reader. There is some prep work to do before the script is run, edit the cayenue.nsi file at the top to set the current version number. The script will set up a directory at %HOMEPATH%\installer and copy some configuration files and run from there. To run the script

```
%HOMEPATH%\Cayenue\assets\scripts\windows\installer\build_installer.bat
```

The result is an executable file in the %HOMEPATH%\installer directory named Cayenue-installer-x.x.x.exe, where x.x.x is the version triplet. Just double click to install. There will be a warning sign that the developer is unkown. To uninstall, go to the settings panel and look through the installed apps.

---

&nbsp;

</details>

&nbsp;

</details>

<details>
<summary>Network Priority on Multi Homed Hosts</summary>

&nbsp;

---

When connecting a host computer to multiple networks, it may be difficult to reach remote computers if one of the connected networks does not have internet access. This can happen if the host computer uses the wired ethernet interface to isolate cameras on a network without internet access and the host intends to use the wireless connection to communicate with the internet. In this situation, the host operating system may attempt to use the wired ethernet connection to communicate with the internet which can result in lengthy delays or the inability to access the internet altogether.

The issue can be addressed by assigning priorities to network adapters. Most Linux distributions seem to be able to handle this situation on their own, so the issue is mostly associated with Windows and MacOS. The basic concept is to set the priority of the connection with the ability to access the internet a higher value than interfaces which are not connected to the internet.

### Windows

Open a powershell in Administrator mode and use the following command to show interface priorities

```
Get-NetIPInterface
```

This will show a table of the network interfaces and their associated priority. Interfaces are tagged with an identifier referred to as InterfaceIndex. The priority of the interface is referred to as InterfaceMetric where lower numbers have higher priority. The priority of an interface is set using the command

```
Set-NetIPInterface -InterfaceIndex <idx> -InterfaceMetric <metric>
```

Where `<idx>` is the network identifier number and `<metric>` is the priority

### MacOS

Click the Apple icon in the upper left corner of the screen and select System Settings -> Network. On the right on the dialog should be a drop down shown as `...v` with a question mark to the right. Click the drop down and select Set Service Order. You can then drag and drop the interface names to set the priority.

---

</details>

<details>
<summary>Running Multiple Cameras</summary>

&nbsp;

Performance in a multi camera configuration can be improved by using substreams. Most cameras are capable of running two streams simultaneously which are configured independently. The default stream is called the Main Stream and has higher resolution, bitrate and frame rate. The Sub Stream is an alternate stream and will have lower resolution, bitrate and frame rate. The Sub Stream is more easily decoded, processed and displayed and can be thought of as a view finder for the Main Stream. 

The application uses the generic terms Display Profile and Record Profile for streams that are processed. The Display Profile is shown to the user in the application and is set on the Media tab for the camera. Note that the default Display Profile will be the higher resolution Main Stream. The Record Profile is used by the application for saving the camera output to disk and is selected on the camera System tab. The Record Profile is not decoded so it places very little compute load on the application and can be used to record high resolution streams without affecting system performance. If the Display Profile and Record Profile are matched, only that one stream is processed by the application.

When running multiple cameras through the system, it is recommended to use the camera sub streams at a low resolution and frame rate to be the Display Profiles. If a more detailed view of the camera stream is needed, the application has a feature that will allow users to view the higher resolution stream by double clicking on the camera stream of interest in the display. This feature will pop out a new window showing the stream.

Stream analytics are performed on the Display stream. The amount of compute load placed on the system during analysis is directly related to Display stream resolution and frame rate, so substreams are strongly recommended if running analytics. 

Many camera substreams will have a distorted aspect ratio, which can be corrected by using the Aspect combo box of the Camera Panel Media Tab.

&nbsp;

---

</details>

<details>
<summary>Performance Tuning</summary>

&nbsp;

As the number of cameras and stream analytics added to the system increases, the host may become overwhelmed, causing cache buffer overflow resulting in dropped frames. If a camera stream is dropping frames, a yellow border will be displayed over the camera output. The load placed on the system by the cameras can be reduced by lowering frame rates and resolutions.

Compute load may also be reduced by increasing the Display Refresh Interval on the General Tab of the Settings section. Camera video streams are buffered and stitched together to form the composite display which is shown once per the interval as set by a timer. Depending on the frame rate of the cameras, this setting can be increased without significant data loss if the Display Refresh Interval is smaller than the inverse of the camera frame rate. This effect is most prominently observed on Windows.

The load on the computer can be observed using a system monitoring tool such as Task Manager on Windows. This tool can be launched by right clicking over the task bar. Linux has a nice monitoring tool named [Mission Center](https://flathub.org/apps/io.missioncenter.MissionCenter) that has an appearance very similar to Task Manager. Apple Macs have the Activity Monitor with pop out windows for CPU and GPU history that can be accessed from the Mac toolbar.

When setting up the computer for Cayenue, it can be helpful to observe the effects of different operations on the system load using the appropriate monitoring tool. Pushing the computer too hard will reduce reliability over time and may lead to crashing. It is a good idea to observe the loads on individual cores in the CPU and try to avoid bottlenecks caused when a single core becomes saturated and is flat lined at 100% usage. GPUs likewise will start to misbehave if pushed too hard. It is a good idea to leave some headroom in the performance metrics to allow for system operations that are performed periodically by the computer in the background.

Lower powered CPUs with a small number of cores or systems running a large number of streams may benefit from hardware decoding. More powerful CPUs with a large core count will work as well as a hardware decoder for smaller numbers of streams.

Stream analysis can potentially place significant burden on system resources. A GPU or iGPU is recommended for YOLO analysis, as a CPU only system will be able to process maybe one or two streams at the most. NVIDIA graphics cards provide the highest performance, and Intel Xe Graphics or later is recommended for iGPU. Modern Macs with Apple Silicon M series chips are capable of performing YOLO analysis. Using Skip Frames during YOLO analysis can also greatly reduce compute load. Using substreams for analysis is recommended, ideally matching the model size parameter to the stream resolution, which by default is 640.

Software developments in this field are constantly advancing, so it may be worthwhile to research new versions of libraries such as pytorch, openvino and associated graphics hardware drivers to see if new performance improvements are available.

&nbsp;

---

</details>

<details>
<summary>Camera Compliance With Standards</summary>

&nbsp;

Camera compliance with the ONVIF standard is often incomplete and in some cases incorrect. Success may be limited in many cases. Cameras made by Hikvision or Dahua will have the greatest level of compatibility. Note that some third party OEM vendors who sell branded versions of these cameras might significantly alter the functionality of the camera software.

Camera settings on the Media tab are most likely to work. Other tabs may have limited success. If Cayenue is able to determine that the camera settings for a particular function are unavailable, it will disable the controls for that function.

If the camera DHCP setting is properly ONVIF compliant, the IP address may be reliably set. Some cameras may not respond to the DHCP setting requested by Cayenue due to non compliance. Note that the camera may reboot automatically under some conditions if the DHCP setting is changed from off to on. DHCP must be turned off before setting a static IP address.

If there is an issue with a particular setting, it is recommended to connect to the camera with a web browser, as most cameras will have a web interface that will allow you to make the changes reliably. Cayenue has a button on the Camera Panel System Tab that will launch the web browser connection with the camera.

---

&nbsp;

</details>

&nbsp;

</details>

<details>
<summary>Acknowledegments</summary>

&nbsp;

<details>
<summary>Media MTX</summary>

---

<a href="https://github.com/bluenviron/mediamtx">
<image src="assets/images/media_mtx_logo.png">
</a>

MIT License

Copyright (c) 2019 aler9

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

---

&nbsp;

</details>

<details>
<summary>YOLOX</summary>

---

<a href="https://github.com/Megvii-BaseDetection/YOLOX">
<image src = "assets/images/yolox_logo.png">
</a>

&nbsp;

Copyright (c) 2021-2022 Megvii Inc. All rights reserved.

License: Apache

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

## Cite YOLOX
If you use YOLOX in your research, please cite our work by using the following BibTeX entry:

```latex
 @article{yolox2021,
  title={YOLOX: Exceeding YOLO Series in 2021},
  author={Ge, Zheng and Liu, Songtao and Wang, Feng and Li, Zeming and Sun, Jian},
  journal={arXiv preprint arXiv:2107.08430},
  year={2021}
}
```
## In memory of Dr. Jian Sun
Without the guidance of [Dr. Sun Jian](http://www.jiansun.org/), YOLOX would not have been released and open sourced to the community.
The passing away of Dr. Sun Jian is a great loss to the Computer Vision field. We have added this section here to express our remembrance and condolences to our captain Dr. Sun.
It is hoped that every AI practitioner in the world will stick to the concept of "continuous innovation to expand cognitive boundaries, and extraordinary technology to achieve product value" and move forward all the way.

<div align="center"><image src="assets/images/sunjian.png" width="200"></div>
没有孙剑博士的指导，YOLOX也不会问世并开源给社区使用。
孙剑博士的离去是CV领域的一大损失，我们在此特别添加了这个部分来表达对我们的“船长”孙老师的纪念和哀思。
希望世界上的每个AI从业者秉持着“持续创新拓展认知边界，非凡科技成就产品价值”的观念，一路向前。

---

</details>

</details>
