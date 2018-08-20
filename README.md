# eos-contracts
EOSIO smart contract development with EOSFactory framework

Setup for smart contract development on Linux OS

## Requirements

- Linux OS (should work on Mac and Windows)

- installed clang-4-0 lldb-4.0
```
sudo apt-get install clang-4.0 lldb-4.0
sudo update-alternatives --install /usr/bin/clang clang /usr/bin/clang-4.0 40 --slave /usr/bin/clang++ clang++ /usr/bin/clang++-4.0
sudo apt-get install clang-4.0 clang++-4.0
update cmake
```
https://askubuntu.com/questions/859256/how-to-install-gcc-7-or-clang-4-0

- installed python3-pip
- installed termcolor
```
sudo apt install python3-pip
python3 -m pip install termcolor
```
- visual studio code
- plugins for studio code:
    - C/C++ IntelliSense, debugging and code browsing.
    - CMake Tools
    - Python


#### [template/contracts](https://github.com/gitgyver/eosfactory/tree/master/templates/contracts)


## Clone
```
git clone https://github.com/gitgyver/eos-contracts --recursive
```
# Install and build
```
sudo ./install.sh
```


cd eosfactory
./build.sh ~/your_install_path/eos ~/your_install_path/contracts
source ~/.profile
```


## Test EOSFactory
```
cd eosfactory
source ~/.profile
python3 ./tests/unittest1.py
python3 ./tests/unittest2.py
python3 ./tests/unittest3.py
cd ..
``` 
## Generate contract from template

https://github.com/gitgyver/eosfactory/tree/master/templates/contracts

Use:
``` 
source ~/.profile
python3 generate.py -name -template
```
generates skeleton template if no template

Examples:
```
cd contracts
python3 generate.py hello.world hello
```

## Hello World example
Open contracts/hello.world contract with visual studio code

Build with Ctrl + Shift + B

Run script:
```
python3 script.py
```


Run without exit:
```
python3 -i script.py
```
Comment out node.stop()


