## Setup

The first thing to do is make sure we have git and install Git Large File Storage (model files are too large for git repo to track)
```sh
git lfs install
```
Next, we clone the repository:
```sh
git clone https://github.com/venkateshsridharann/Next-Word-Predictor
```
Create a virtual environment to install dependencies in and activate it:
```sh
#(in case you do not have pipenv installed)
pip install pipenv

#install all required packages from pipfile
pipenv install
pipenv shell
```
 

or if you have already installed the dependencies just activate the shell
```sh

pipenv shell
```

Start the Webapp on the local server
```sh
cd 'next word predictor\Django WebApp\myproject'
python manage.py runserver
```
And navigate to `http://127.0.0.1:8000/`.    

<br />

## Next-word-predictor

This is a web application that uses ML to suggest the next word (along with a probability score) to improve writing efficiency.  

<br />

### Model options 
![Screenshot 2023-11-25 051907](https://github.com/venkateshsridharann/Next-Word-Predictor/assets/36308828/812c56e5-7ef3-492d-928d-a88172a3baec)



<br />

### The Web app with a custom-trained model with actual predictions
![Screenshot 2023-11-25 052223](https://github.com/venkateshsridharann/Next-Word-Predictor/assets/36308828/de9ded15-438e-41bd-96f8-cae67dfa3577)



<br />

### The Webapp using GPT2-based pre-trained model with actual predictions - Better Contextual Suggestions
![Screenshot 2023-11-25 051957](https://github.com/venkateshsridharann/Next-Word-Predictor/assets/36308828/cc047f4d-26ed-45bd-835f-9210fdac4513)



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
            

                    

