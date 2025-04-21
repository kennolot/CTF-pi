## CTF-pi - Multiple encryptions - Difficulty: ★★☆☆☆

### Scenario

You continue finding logs but this time there are 3 different files, at first glance they look different from each other.
Find out what encryption is used now and try to decode them.

Flag format is `CTFPI{lowercase}` add filters to your cracking software and you will get faster decoding times, you only need to crack the lowercase part, 'CTFPI{}' is not part of decoded result.

### Prerequisites

Your Raspberry Pi has remote connection set up via Raspberry Pi Connect or VNC.

Have cloned this `CTF-pi` repository and are inside the `ctfpi2_1` directory.

### Objective

Open the files `log1.txt` , `log2.txt`, `log3.txt` and try to crack the code.

Each one is required to get the entire flag.


### **Hints**

Hash analyze all the log.txt files

Decryption could take up to 30 seconds for each file using online tools

These are all well known encryptions.
