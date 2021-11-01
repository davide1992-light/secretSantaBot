# secretSantaBot
just a stupid Python3 script to organize a secret santa with your friends

Mr. Santa Bot will send you and your friends an email with the name of the lucky person who will receive a gift from you! 
After the mail has been sent, Mr. Santa Bot is smart enough to go to the email box, and delete the sent emails.

Mr. Santa Bot decides randomly assign to each person another person to whom they are gonna buy a gift. 
Not every possible situation is deemed valid, we only select permutations which follow these rules. 
Let A and B be two participants to the secret santa:
1. A cannot give a gift to themselves;
2. if A must give a gift to B, then B cannot give a gift to A.
3. if B is the previousSanta of A, that is A gave a gift to B last year, than this year A cannot give a gift to B.

# Getting Started 

Requires python3, and the library dotenv which can be installed using
```pip install python-dotenv```

In alternative, one can use the file requirements.txt in the main folder and create a virtual environment.

Finally, one must set a proper .env file with the necessary environment variables:
* ```SANTA_MAIL```: the email that will be used by Mr. Santa Bot
* ```SANTA_PASSWORD```: the password necessary to access the above mail box 
* ```IMAP_SERVER```: the IMAP server used by the provider of the SANTA_MAIL account
* ```SMTP_SERVER```: the SMTP server used by the provider of the SANTA_MAIL account
* ```SMTP_PORT```: the port to use for the SMTP service

an example of .env file can be found in example_data/example_env

**NOTE** that you probably have to enable IMAP/SMTP clients manually from your mail provider.

# Usage

you need two input files: 
1. a "peoplefile" which specifies the partecipants to the secret santa;
2. a "messagefile" which describes the template of the email sent by Mr. Santa Bot 
3. (optional) an "--address" flag to add if you want to include the address of the gift receiver.

After you've created the two files, you use the script simply by typing 

```python3 my_little_santabot.py /path/to/peoplefile /path/to/messagefile```

or if you also wish to have addresses in the mails:

```python3 my_little_santabot.py /path/to/peoplefile /path/to/messagefile  --address```

You can also get these informations, by typing:

```python3 my_little_santabot.py --help```

Below, you can find how to set the peoplefile and the messagefile 

# User Input Data 

The peoplefile must be a valid JSON file, where each entry must correspond to a user of the secret santa. To each user must be associated 
a "mail" property (required) which gets back the email of the user, and a "previousSanta" property (optional) which tells you the previousSanta of the user.

_IF_ the "--address" flag has been used, then also an "address" property is required.

_An example file is present in example_data/example_people.json_

_Another example, with addresses, is present in example_data/example_people_address.json_

If no previousSanta is specified for a user, than it is assumed that there is no previousSanta and it will be ignored when generating the random permutation.

# Message Input Data 

Just a normal text file that is going to be the template for your santabot emails. Just write the normal email, and whenever you would write the name of 
the santa put the string "{sender}", while whenever you would put the name of the receiver of the gift put the string "{receiver}".

_IF_ the "--address" flag has been used, then also an "{address}"  string must be present in the template file, as it will tell secret santa bot, where to 
insert the receiver's address.

_An example file is present in example_data/example_message.txt_






