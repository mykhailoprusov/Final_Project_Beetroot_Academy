# Final_Project_Beetroot_Academy

### Project Description:
A sport nutrition web application using Python and Django that allows users to receive sport meals suggestions from ChatGPT api. 
It firstly requests the data from chatgpt using openai library. Then passes and formats the data to the template.
It also enables users to navigate through the website and view multiple articles.
There is also a blog, access to which is given only after authorisation.
Users can interact there and share their own food recepies for muscle building.
In addition, the backend part encompasses registration, logout, login, profiles( cretated by the system for each user just after the registration)
User is not able to get access to the blog or profiles via url

### Code Organization:
Django project. Main app - config, blog app - covers everything related to the blog side, users app - covers everything related to the user side ( profile model,
templates for login, logout, registration and profile, views etc. ), Media app - storage for profile icons and logo photos

### Installation and Setup:
You need to have a token file inside the blog app that has ChatGPT token to run the web application. Also you need to have a config_data.json file in the root
directory that has such data:"""
{
    "default": {
        "ENGINE": "",
        "NAME": "",
        "HOST": "",
        "PORT": ,
        "USER": "",
        "PASSWORD": ""
    },

    "SECRET_KEY" :
    

}
"""


