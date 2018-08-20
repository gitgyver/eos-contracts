#Hello world example

#Generate cotract:
#cd ..
#python3 generate.py yourcontractname 

#Run:
# source ~/.profile
# python3 script.py

#Run without exit:
# comment out node.stop()
# python3 -i script.py


#create user
#load hello.world and yourcontractname contract
#deploy
###############################################
import node
import sess
import eosf

node.reset()
sess.init()

john = eosf.account(sess.eosio, name="john")
sess.wallet.import_key(john)

#change hello.world to yourcontractname
contract = eosf.Contract(john, "hello.world")
contract.build()
contract.code()
contract.deploy()
contract.code()

contract.push_action("hi", '["world"]')

#contract = eosf.Contract(john, "yourcontractname")
#contract.code()
#contract.deploy()
#contract.code()

node.stop()
