# Communication-Networks-Project-G2
Project for the Communication Networks course 2022-2023

TOR NETWORK
Requirements
  Libraries needed:
    termcolor : can be downloaded using pip install termcolor in the terminal
    pycryptodome: can be downloaded using pip install pycryptodome in the terminal
How to test the encryption and decryption
Run files : node1,node2,node3,client,destination,genesis node
    NB: you can create whatever 
  Genesis node will only link all the node instances together 
  The decryption path will be as follows : client ->node1 ->node2 ->node3 ->destination
 Remark: You can create as many nodes as you want! Just copy paste one of the nodes and change the port numbe;r
  Press enter on each files in order for each node to be aware of the others.(Genesis node will broadcast all the address of the all the nodes)
  On client, enter your secret message when it asks you to... It will cipher it and send it to node 1 
  Then go on node 1 and press enter for it to show it receives the message,decipher it, extract the port number of the next node and send it to th 
  next node.
  Then go on node 2, do the same.
  Then go on node 3,do the same.
  Finally, go on destination, press a enter and you will see the deciphered message.
  
  
