# Email Automation
## Randomised Spam email sender for pranks
The script is written in python and automatically sends pre-written randomised 
emails to a list of people being pranked.

The message is randomised through the `random` module and chosen randomly in a
file of messages.

This script uses `smtplib` library to send emails. Now major email service providers
are phasing out smtp connections to 3rd party apps, so I had to change out many emails for that XD.

<details>
<summary> click here </summary>
P.S. use outlook or hotmail, they still support 3rd party smtp connections.
</details>

A general look of the email is as follows : 
```
Dear Bakra,

        Today is day 1 of expressing my love to you.

        In your eyes, I find the warmth of a thousand suns, and in your smile, the joy of a lifetime.
        With you, every heartbeat whispers the sweet melody of love.

        Yours truly, ❤
```

This is a very fun project with pranking potential with friends.
Maybe not so fun as most people don't really check their inbox and with more anti-spam
technology, the emails may be flagged as spam.