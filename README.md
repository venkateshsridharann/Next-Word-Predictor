## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/venkateshsridharann/Next-Word-Predictor
```

Create a virtual environment to install dependencies in and activate it:
```sh
#(in case you do not have pipenv installed)
$ pip install pipenv

#install all required packages from pipfile
$ pipenv install
$ pipenv shell
```
 

or if you have already installed the dependencies just activate the shell
```sh

$ pipenv shell
```

Start the Webapp on the local server
```sh
(env)$ cd 'next word predictor\Django WebApp\myproject'
(env)$ python manage.py runserver
```
And navigate to `http://127.0.0.1:8000/`.    

<br />

## Next-word-predictor

This is a web application that uses ML to suggest the next word (along with a probability score) to improve writing efficiency.  

Model options 
![image](https://github.com/venkateshsridharann/Next-Word-Predictor/assets/36308828/28d49bdb-4382-4676-9355-bbedd16b0982)

The Webapp Sample (WIP) with actual predictions (custom model)
![image](https://github.com/venkateshsridharann/Next-Word-Predictor/assets/36308828/03d57fd3-56fe-4cbf-988c-a1afb713b282)


The Webapp Sample (WIP) with dummy predictions  [Add 'custom/sample' to BaseURL of app]  
![image](https://github.com/venkateshsridharann/Next-Word-Predictor/assets/36308828/759965ce-333d-4724-b4ee-0112fcaea922)


The ML output  
![ml predictions](https://github.com/venkateshsridharann/Next-Word-Predictor/assets/36308828/6947ba0c-237f-40cd-8d3a-82d4b04324d5)

  

    
## Still Under Development 

- ML Model  - Custom  
            -   Training on a larger dataset  

  
- ML Model using Langchain  
            -   Context  
            -   Grammatically correct suggestions (suggestions after a/an)     
            -   Improve response speed on LLM model  
            -   clean the generated ouput remove ('\', '()', '!!!', '~' etc.)   
            -   try an implementation of "https://huggingface.co/HuggingFaceH4/zephyr-7b-alpha?text=We"    
            

- Backend/Frontend  
            -  ~~Model Service~~  
            -  ~~Output from ML piped to Frontend~~   
            -  ~~Realtime suggestions~~  
            -  Suggested word gets added to input on click   
            

                    

