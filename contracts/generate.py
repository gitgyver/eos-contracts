
import sys
import eosf
#print ('Number of arguments:', len(sys.argv), 'arguments.')
#print ('Argument List:', str(sys.argv))
l = len(sys.argv)
if(l<2): 
    print('nothing to generate')
elif (l==2):
    contract = eosf.ContractBuilderFromTemplate(sys.argv[1],template="skeleton")
    contract.build()
    #add script.py
elif (l==3):
    contract = eosf.ContractBuilderFromTemplate(sys.argv[1],template=sys.argv[2])
    contract.build()
else:
    passprint('too many arguments')