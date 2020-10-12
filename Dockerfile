FROM ubuntu:bionic

ARG DEBIAN_FRONTEND=noninteractive

ENV LC_ALL C.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US.UTF-8

RUN apt-get update && apt-get clean && apt-get install -y \
    x11vnc \
    xvfb \
    wmctrl \
    wget \
    python \
    chromium-browser \
    xdotool \
    maim \
    python3-pip \
    python3-numpy \
    nano \
    curl

RUN apt-get install -y python3-tk scrot

RUN apt-get install -y dbus-x11
RUN apt-get install -y proxychains4

WORKDIR /home/
RUN wget -O - https://github.com/novnc/noVNC/archive/v1.1.0.tar.gz | tar -xzv -C /home/ && mv /home/noVNC-1.1.0 /home/novnc && ln -s /home/novnc/vnc_lite.html /home/novnc/index.html
RUN wget -O - https://github.com/novnc/websockify/archive/v0.9.0.tar.gz | tar -xzv -C /home/ && mv /home/websockify-0.9.0 /home/novnc/utils/websockify

EXPOSE 8080

RUN wget https://launchpad.net/ubuntu/+archive/primary/+files/megatools_1.10.3-1_amd64.deb
RUN apt install -y ./megatools_1.10.3-1_amd64.deb

RUN pip3 install --upgrade pip
RUN python3 -m pip install requests opencv-python more-itertools pyautogui pynput pyscreenshot xlib pyvirtualdisplay
RUN python3 -m pip install pyotp pyperclip

ENV TINI_VERSION v0.19.0
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini /tini
RUN chmod +x /tini

WORKDIR /home/bezmouse
COPY bezmouse /home/bezmouse
RUN python3 -m pip install -U /home/bezmouse/
RUN python3 /home/bezmouse/setup.py install
RUN mkdir -p /usr/local/lib/python3.6/dist-packages/bezmouse/tmp

WORKDIR /home/
RUN apt-get install -y unzip xclip
RUN wget https://github.com/odwyersoftware/mega.py/archive/master.zip && unzip master.zip 
WORKDIR /home/mega.py-master
RUN python3 setup.py install
WORKDIR /home/

COPY download.py /home/
COPY listen.py /home/
COPY terminal_open.py /home/
COPY upload.py /home/
COPY ping.py /home/

COPY bootstrap.sh /

CMD ["/tini", "/bootstrap.sh"]
