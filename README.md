# Python Automation
## List of contents
+ Exam results website scraping
+ Randomised Spam email sender for pranks

### 1. Exam results website scraping
The script is written in python and automatically logins to the students page and 
extracts data such as sgpa, cgpa, name and such.

This auto login is possible because no password such as DOB is required and only
a simple CAPTCHA is required to be solved.
Thus, we can automate constructing the USN and login.

Selenium as the python library is chosen as it is interacting with the website to 
login i.e. dynamic pages. beautifulsoup can be used for static pages.

In the current form, a csv file is generated that is structured like : 

|   name   | usn  | sgpa | cgpa | 
|:--------:|:----:|:----:|:----:|
| John Doe | 1234 |  10  |  10  |

The script can be run in headless mode and everything can be done behind the scenes.
but the actual browser being controlled is so much fun.

### IMPORTANT

<pre>
To run the script, we need to install the chrome driver which uses the WebDriver API.
Install it from <a href = "https://googlechromelabs.github.io/chrome-for-testing/"> googleChromeLabs </a>
More drivers for other browsers are also available.
</pre>
```
branchCodeDict = {'CI': 143, 'CS': 229, 'CY': 75, 'IS': 160}

You need to manually check the last USN in each branch. one of the disadvantages of 
this script.
Also make sure that you don't run the script for a large number of people at the 
same time, it can be interpreted as a DoS attack.
```
```
The CAPTCHA must be solved manually in 10 seconds so the script can take over.
```
<details>
<summary> "Features" of the website that are exploited </summary>
  
* The CAPTCHA isn't reloaded after we return back to the login page.
thus, solving the CAPTCHA is needed only once.
* No password like DOB is needed to access the results.

</details>

### 2. Randomised Spam email sender for pranks
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
