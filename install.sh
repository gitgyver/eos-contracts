#!/bin/bash
bwd=$(pwd)
fwd="$bwd/eosfactory"
cwd="$bwd/contracts"
ewd="$bwd/eos"

git submodule update --init --recursive

cd eos
./eosio_build.sh
cd build
sudo make install
cd ..
nodeos --extract-genesis-json genesis.json

cd ..

cd $fwd

./build.sh -e $ewd -w $cwd
#./build.sh -e $ewd
#./build.sh -e
source ~/.profile
