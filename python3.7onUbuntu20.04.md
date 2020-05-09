# How to install Python 3.7 on Ubuntu 20.04 

## Motivation
Ubuntu 20.04 comes with Python 3.8
Tensorflow supports only 3.7 for now
Open ai baseline and works only with TF 1.15
So I want to create a virtual env with Python 3.7 and TF 1.15

## Shell command

    mkdir ~/src
    mv Downloads/Python-3.7.7.tgz .
    tar -zxvf Python-3.7.7.tgz 
    cd Python-3.7.7/
    mkdir ~/.localpython
    ./configure --prefix=$HOME/.localpython
    make
    make install
    ~/.localpython/bin/python3.7 -m pip install pip --upgrade
    ~/.localpython/bin/python3.7 -m pip install virtualenv
    virtualenv myenv -p $HOME/.localpython/bin/python3.7
    source myenv/bin/activate
    pip install tensorflow==1.15
