import node
import eosf

# Start node
node.reset()

# Local wallet
wallet = eosf.Wallet()

eosio = eosf.AccountMaster()

wallet.import_key(eosio)

# Account eosiotoken
eosiotoken = eosf.account(eosio, "eosio.token")

# Necessary accounts for eosio.system contract

bpay = eosf.account(eosio,name="eosio.bpay")
names = eosf.account(eosio,name="eosio.names")
ram = eosf.account(eosio,name="eosio.ram")
ramfee = eosf.account(eosio,name="eosio.ramfee")
saving = eosf.account(eosio,name="eosio.saving")
stake = eosf.account(eosio,name="eosio.stake")
vpay = eosf.account(eosio,name="eosio.vpay")

wallet.import_key(eosiotoken)
wallet.import_key(bpay)
wallet.import_key(names)
wallet.import_key(ram)
wallet.import_key(ramfee)
wallet.import_key(saving)
wallet.import_key(stake)
wallet.import_key(vpay)

# Load contract (eos/build/contracts/eosio.token) on eosio.token account

token = eosf.Contract(eosiotoken, "eosio.token")
token.deploy()

#Create token

token.push_action(
    "create",
    '{"issuer":"'+ eosio.name + '", ' +
    '"maximum_supply":"10000000000.0000 SYS"}',
    eosiotoken)

#Issue to accountMaster eosio

token.push_action(
    "issue",
    '{"to":"' + eosio.name + '", '+
    '"quantity":"1000000000.0000 SYS", '+
    '"memo":"memo"}',
    eosio)

# Load contract (eos/build/contracts/eosio.system) on eosio (Master) account

system = eosf.Contract(eosio, "eosio.system")
system.deploy()

# Create player 1

alice = eosf.account(eosio, 
    "alice",
    stake_net="1 SYS",
    stake_cpu="1 SYS",
    buy_ram_kbytes="8",
    permission="eosio",
    transfer=True
)
wallet.import_key(alice)

# Create player 2

bob = eosf.account(eosio, 
    "bob",
    stake_net="1 SYS",
    stake_cpu="1 SYS",
    buy_ram_kbytes="8",
    permission="eosio",
    transfer=True
)
wallet.import_key(bob)

#Create tictactoe account

tictactoe = eosf.account(
    eosio,
    "tic.tac.toe",
    stake_net="100 SYS",
    stake_cpu="100 SYS",
    buy_ram_kbytes="5000",
    permission="eosio",
    transfer=True
)
wallet.import_key(tictactoe)

#Load contract (eos/build/contracts/tic_tac_toe) on tic.tac.toe account

tttContract = eosf.Contract(tictactoe, "tic_tac_toe")
tttContract.deploy()

# Create game

tttContract.push_action(
    "create",
    '{"challenger":"'+ bob.name +
    '", "host":"'+ alice.name +'"}',
    alice)

# Move

tttContract.push_action(
    "move",
    '{"challenger":"'+ bob.name +
    '", "host":"'+ alice.name +
    '", "by":"'+ alice.name
    +'", "mvt":{"row":0, "column":0} }',
    alice)

# Print table games

tttContract.table("games",alice)

# Stop node
node.stop()