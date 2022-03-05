# Settings

This page provides infomation about the Firebrick values in the `settings.py` file. 


## Accounts App

These are all settings relating to the accounts app genarated by Firebrick

#### USERNAME_LENGTH_MIN

`type`: `int`

As the name suggests this is the minimum length a username can by for the User model.


#### USERNAME_LENGTH_MAX

`type`: `int`

Like [`USERNAME_LENGTH_MIN`](commands.md#username_length_min) but for max length.


#### USERNAME_VALID_CHARS

`type`: `str`

All charcters that can be used in a username in the User model. Can use Regex.