
# Replica-watch Forum Thread Data Scraper

This script based on property data scrap from https://forum.replica-watch.info/


## What you will get:

- All data in in a CSV file.
- Data points are- Name, User Title, Post Time, Profile Image, Job Title, Joined, Message Count, Reaction Count, Points Count, Posts, Location, Message Content.


## Requirement

- Language: Python
- Libraries: datetime, pandas, selenium, webdriver_manager, uc, Bs4, lxml, os


## Documentation

- Install python on your OS. You can install latest version of python.
- Now open your cmd/terminal from the script folder and run this command:
```bash
  pip install -r requirements.txt
```
- Now we can run the script using this command from that folder terminal/cmd:
```bash
python replica-watch.py
```
- After run the script it will ask you to input a thread link. You need to input a thread link and hit enter:
  Ex: https://forum.replica-watch.info/threads/bad-gateway-502-does-anyone-see-the-same.10981213/
- After input that link it will ask you how many pages do you want to scrap. You need to input your expected last page number and hit enter.
  Ex: 65
- After that It will automaticaly go through all of your pages and scrap the data. Save the data in a CSV file.


## 🔗 Social Links

📧 mr.amitc55@gmail.com

✅ [@amitchakraborty123](https://www.github.com/amitchakraborty123)

✅ [Linkedin](https://www.linkedin.com/in/mrchamit/)
## 🚀 About Me
I'm a Data Analyst.


## License

[MIT License](https://choosealicense.com/licenses/mit/)
