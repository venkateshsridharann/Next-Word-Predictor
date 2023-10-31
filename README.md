## Setup

The first thing to do is make sure we have git and install Git Large File Storage (model files are too large for git repo to track)
```sh
$ git lfs install
```
Next, we clone the repository:
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

<br />

### Model options 
![image](https://github.com/venkateshsridharann/Next-Word-Predictor/assets/36308828/28d49bdb-4382-4676-9355-bbedd16b0982)

<br />

### The Web app with a custom-trained model with actual predictions
![image](https://github.com/venkateshsridharann/Next-Word-Predictor/assets/36308828/1aae75ae-d30f-4aa7-984c-02f83aa8734c)

<br />

### The Webapp using GPT2-based pre-trained model with actual predictions - Better Contextual Suggestions
![image](https://github.com/venkateshsridharann/Next-Word-Predictor/assets/36308828/03bb3938-11f6-4f5e-ab0a-57b3dca53a44)


<br />

The Custom ML output  
![ml predictions](https://github.com/venkateshsridharann/Next-Word-Predictor/assets/36308828/6947ba0c-237f-40cd-8d3a-82d4b04324d5)

  

    
## Still Under Development 

- ML Model  - Custom  
            -   ~~Trained on a small dataset for POC~~  
            -   ~~Probability score~~  
            -   Training on a larger dataset for better suggestions    

  
- ML Model using GPT2 Pre-trained Model  
            -   ~~Context~~  
            -   ~~Grammatically correct suggestions~~     
            -   ~~Improve response speed on LLM model~~  
            -   ~~clean the generated output remove ('\', '()', '!!!', '~' etc.)~~   
            -   ~~Generate probability score for suggestions~~    
            
            

- Backend/Frontend  
            -  ~~Infrastructure setup~~  
            -  ~~Model Service~~  
            -  ~~Output from ML piped to Frontend~~   
            -  ~~Realtime suggestions~~  
            -  ~~Suggested word gets added to input on click~~     
            

                    

