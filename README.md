# Communication-Networks-Project-G2
Project for the Communication Networks course 2022-2023

TOR NETWORK<br />
Requirements<br />
  Libraries needed:<br />
    termcolor : can be downloaded using pip install termcolor in the terminal<br />
    pycryptodome: can be downloaded using pip install pycryptodome in the terminal<br />
How to test the encryption and decryption<br />
Run files : node1,node2,node3,client,destination,genesis node<br />
    NB: you can create whatever <br />
  Genesis node will only link all the node instances together <br />
  The decryption path will be as follows : client ->node1 ->node2 ->node3 ->destination<br />
 Remark: You can create as many nodes as you want! Just copy paste one of the nodes and change the port numbe<br />
  Press enter on each files in order for each node to be aware of the others.(Genesis node will broadcast all the address of the all the nodes)<br />
  On client, enter your secret message when it asks you to... It will cipher it and send it to node 1 <br />
  Then go on node 1 and press enter for it to show it receives the message,decipher it, extract the port number of the next node and send it to th 
  next node.<br />
  Then go on node 2, do the same.<br />
  Then go on node 3,do the same.<br />
  Finally, go on destination, press a enter and you will see the deciphered message.<br />
  
  
