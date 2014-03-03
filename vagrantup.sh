#! /bin/bash
echo I am provisioning...

export SUBLIME_TEXT_VERSION=$1
export PACKAGE="$2"
export STP=/home/vagrant/.config/sublime-text-$SUBLIME_TEXT_VERSION/Packages

if [ -z $(which subl) ]; then
    echo apt-get installing
    if [ $SUBLIME_TEXT_VERSION -eq 2 ]; then
        echo installing sublime 2
        sudo add-apt-repository ppa:webupd8team/sublime-text-2 -y
        sudo apt-get update
        sudo apt-get install python-software-properties -y
        sudo apt-get install sublime-text -y
    elif [ $SUBLIME_TEXT_VERSION -eq 3 ]; then
        echo installing sublime 3
        sudo add-apt-repository ppa:webupd8team/sublime-text-3 -y
        sudo apt-get update
        sudo apt-get install python-software-properties -y
        sudo apt-get install sublime-text-installer -y
    fi
    sudo apt-get install git -y
    sudo apt-get install curl -y
    sudo apt-get install xvfb libgtk2.0-0 -y
    # curl https://raw.github.com/pypa/pip/master/contrib/get-pip.py | sudo python
fi

if [ ! -d $STP ]; then
    mkdir -p $STP
fi

if [ ! -d $STP/$PACKAGE ]; then
    ln -s /vagrant $STP/$PACKAGE
fi

if [ ! -d $STP/UnitTesting ]; then
    git clone https://github.com/randy3k/UnitTesting $STP/UnitTesting
fi

if [ ! -f /etc/init.d/xvfb ]; then
    echo installing xvfb controller
    curl https://gist.githubusercontent.com/randy3k/9225319/raw/dee3521ed340bcb99ad721ae9f36e6c4b0a225de/xvfb | sudo tee /etc/init.d/xvfb > /dev/null
    chmod +x /etc/init.d/xvfb
fi
sudo /etc/init.d/xvfb start