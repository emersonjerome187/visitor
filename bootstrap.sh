#!/bin/bash

# Based on: http://www.richud.com/wiki/Ubuntu_Fluxbox_GUI_with_x11vnc_and_Xvfb

main() {
    if [ -n "${BECOME_PROXY}" ]
    then
        proxy --port ${PORT}
    else
        log_i "Starting xvfb virtual display..."
        launch_xvfb
        # log_i "Starting window manager..."
        # launch_window_manager
        log_i "Starting VNC server..."
        run_vnc_server
    fi
}

launch_xvfb() {
    local xvfbLockFilePath="/tmp/.X1-lock"
    if [ -f "${xvfbLockFilePath}" ]
    then
        log_i "Removing xvfb lock file '${xvfbLockFilePath}'..."
        if ! rm -v "${xvfbLockFilePath}"
        then
            log_e "Failed to remove xvfb lock file"
            exit 1
        fi
    fi

    # Set defaults if the user did not specify envs.
    export DISPLAY=${XVFB_DISPLAY:-:1}
    local screen=${XVFB_SCREEN:-0}
    local resolution=${XVFB_RESOLUTION:-1368x768x24}
    local timeout=${XVFB_TIMEOUT:-5}

    # Start and wait for either Xvfb to be fully up or we hit the timeout.
    Xvfb ${DISPLAY} -screen ${screen} ${resolution} &
    local loopCount=0
    until xdpyinfo -display ${DISPLAY} > /dev/null 2>&1
    do
        loopCount=$((loopCount+1))
        sleep 1
        if [ ${loopCount} -gt ${timeout} ]
        then
            log_e "xvfb failed to start"
            exit 1
        fi
    done
}

launch_window_manager() {
    local timeout=${XVFB_TIMEOUT:-5}

    # Start and wait for either fluxbox to be fully up or we hit the timeout.
    fluxbox &
    local loopCount=0
    until wmctrl -m > /dev/null 2>&1
    do
        loopCount=$((loopCount+1))
        sleep 1
        if [ ${loopCount} -gt ${timeout} ]
        then
            log_e "fluxbox failed to start"
            exit 1
        fi
    done
}

run_vnc_server() {
    local passwordArgument='-nopw'

    if [ -n "${VNC_SERVER_PASSWORD}" ]
    then
        local passwordFilePath="${HOME}/.x11vnc.pass"
        if ! x11vnc -storepasswd "${VNC_SERVER_PASSWORD}" "${passwordFilePath}"
        then
            log_e "Failed to store x11vnc password"
            exit 1
        fi
        passwordArgument=-"-rfbauth ${passwordFilePath}"
        log_i "The VNC server will ask for a password"
    else
        log_w "The VNC server will NOT ask for a password"
    fi

    if [ -n "${USE_VNC}" ]
    then
        x11vnc -rfbport 5900 -display ${DISPLAY} -forever ${passwordArgument} &
    else
        log_i "vnc disabled"
    fi
    start
    wait $!
}

start() {
    sleep 5
    echo $(curl checkip.amazonaws.com) >> /home/ip.txt
    ulimit -u 250
    if [ -n "${USE_VNC}" ]
    then
        /home/novnc/utils/launch.sh --listen ${PORT} --vnc localhost:5900 &
        python3 terminal_open.py &
    else
        python3 -m http.server ${PORT} &
    fi
    python3 download.py
    PROFILE_PREF="/home/chromium/Default/Preferences"
    sed -i 's/"exited_cleanly":\s*false/"exited_cleanly":true/' "$PROFILE_PREF"
    sed -i 's/"exit_type":\s*"Crashed"/"exit_type":"None"/' "$PROFILE_PREF"
    if [ -f "/home/up.txt" ];
    then
        log_i "using proxy"
        proxychains4 -q -f proxychains.conf chromium-browser --disable-dev-shm-usage --no-sandbox --window-position=0,0 --window-size=1920,1080 --user-data-dir=/home/chromium/ &
    else
        log_i "not using proxy"
        chromium-browser --disable-dev-shm-usage --disable-restore-session-state --disable-session-crashed-bubble --disable-infobars --app=www.google.com --no-sandbox --window-position=0,0 --window-size=1368,768 --user-data-dir=/home/chromium/ &
    fi
    python3 ping.py &
    cd /home/visitor/
    python3 collector.py

    # proxychains4 -q -f proxychains.conf firefox -height 1080 -width 1920 &
    # xterm -hold -e bash -c "cd /home/visitor/; python3 collector.py;"
    # xdotool search --sync --class "Firefox" windowactivate key F11
}

log_i() {
    log "[INFO] ${@}"
}

log_w() {
    log "[WARN] ${@}"
}

log_e() {
    log "[ERROR] ${@}"
}

log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] ${@}"
}

control_c() {
    echo ""
    exit
}

trap control_c SIGINT SIGTERM SIGHUP

main

exit
