## Multiple encryptions

### Scenario

You continue finding logs but this time there are 3 different files, at first glance they look different from each other.
Find out what encryption is used now and try to decode them.

Flag format is `CTFPI{lowercase}` add filters to your cracking software and you will get faster decoding times, you only need to crack the lowercase part
'CTFPI{}' is not part of decoded result

### Requirements

Can be done from your main machine, or on your Pi.

### Prerequisites

Have cloned this repository and are inside the `ctfpi3_1` directory

Open the files ex `log1.txt` and try to crack the code


### **Hints**

Hash analyze all the log.txt files

Decryption could take up to 30 seconds for each file using online tools

These are all well known encryptions.


### Completion

After you think you've found the flag, you may compare your flag with the one on `answers/flag.txt`