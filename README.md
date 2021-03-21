Overview:
```
This Program runs on python BDD . Demo is for NHS site 
User Story
As a person from England 
I need to know what help I can get with my NHS costs
So that I can get the treatment I need
```



First of all on terminal type:
```
pip install -r requirements.txt
```


### How to run with different browsers?
``` behave -D browser=browsername ```

Example:
 ```
  behave -D browser=firefox
  behave -D browser=chrome
  ....
  
 ```
In our automation suite, the default browser is Chrome so if you don't define any browser name 
it will start with the Chrome browser.

### How to run various browsers in headless mode?
``` behave -D headless=true --tags='tagname' ```
```behave -D headless=true --tags='@best' -D browser='name_of_browser' ```


### How to run test with specific tag names?
Example:``` behave --tags='tagname' ```