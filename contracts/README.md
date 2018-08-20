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

https://github.com/blws/eosfactory/tree/master/templates/contracts

Use:
``` 
source ~/.profile
python3 generate.py -name -template
```
generates skeleton template if no template

Example:
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

Build:
```
contract.build()
```

Run without exit:
```
python3 -i script.py
```
Comment out node.stop()


Ctrl + D to exit
