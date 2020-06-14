# crypto-mark2
This is the next version of the already avaliable script. It takes in a 'main_data.txt' file and converts it into a key file which can only be decrypted by the decrypt script given. I shall be adding more functionality to the script and adding master password support for decryption.

# Installation
For this script to work, you will need the atleast Python 3.6 to run it.
To get started download the zip file or use Git.

```sh
$ git clone https://github.com/shabbysinger/crypto-mark2.git
$ cd crypto-mark2
```
# Running the Script
### Encrypting
Make a text file named 'main_data.txt' (without quotes) and put all your passwords or information that you want to keep safe. 
WARNING: The main_data.txt will be destroyed once the script encrypter.py script runs.
```sh
$ cd crypto-mark2
$ python3 encrypter.py
```
A file named 'pass.txt' should be created. (That is your key file, do not lose it!)
### Decrypting
Now to decypt your file make sure you have the 'pass.txt' file in the same folder as the decrypter.py script. 
WARNING: This will destroy the 'pass.txt' file. Under no circumstances the 'pass.txt' is to be messed with.
```sh
$ cd crypto-mark2
$ python3 decrypter.py
```

Now you should have the orignal 'main_data.txt' file with you.
