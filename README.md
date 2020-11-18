# booleanNetworks
This is pygame interpretation of the boolean networks. It gives a great view into how the networks work. 
Parameters (in the Params class):

size -> The size of the single rectagle representing the state of the network element


rules -> Dictionary of the rules created randomly by the method CreateRules(numCon). If you want to create rules on your own provide them in the form of {"001":1} dictionary. The key to the dictionary is the state of the connected elements (every combination must be in the rules set) and the value is the 0 or 1 accordingly.


numCon -> Maximal number of connections for the single element in the network. Set it via the CreateRules(numCon) method.
