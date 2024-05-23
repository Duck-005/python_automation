# Web Scraping
## Exam results website scraping
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


