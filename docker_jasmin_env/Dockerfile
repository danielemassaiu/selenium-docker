FROM ubuntu:trusty

RUN echo "deb http://ppa.launchpad.net/mozillateam/firefox-next/ubuntu trusty main" > /etc/apt/sources.list.d//mozillateam-firefox-next-trusty.list

RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys CE49EC21

RUN apt-get update

RUN apt-get install -y firefox xvfb python-pip wget

ADD requirements.txt /tmp

RUN pip install -r /tmp/requirements.txt

ADD xvfb.init /etc/init.d/xvfb

RUN chmod +x /etc/init.d/xvfb

RUN update-rc.d xvfb defaults

RUN wget https://github.com/mozilla/geckodriver/releases/download/v0.16.0/geckodriver-v0.16.0-linux64.tar.gz -O /tmp/geckodriver.tar.gz && tar -C /opt -xzf /tmp/geckodriver.tar.gz && chmod 755 /opt/geckodriver && ln -fs /opt/geckodriver /usr/bin/geckodriver && ln -fs /opt/geckodriver /usr/local/bin/geckodriver

ENTRYPOINT ["/bin/bash"]