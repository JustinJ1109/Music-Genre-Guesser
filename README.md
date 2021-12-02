# Music-Classifier  

This program attempts to guess the genre of a sound file.  

Given a song, the program will output the top 3 matches it guesses and their relative percentages of how strongly the program matches the genre.  

This model uses the GTZAN Dataset found [here](https://www.kaggle.com/andradaolteanu/gtzan-dataset-music-genre-classification)   

It includes 100 30 second royalty-free sound files from 10 different genres pre-classified for use as well as respective spectrograms for each song (unused).  

The 10 genres included in training are:  
- blues  
- classical  
- country  
- disco  
- hiphop  
- jazz  
- metal  
- pop  
- reggae  
- rock  
  
## How to Install  
Clone this repo  
  
Once cloned, using python3, run ```pip install -r ./requirements.txt``` to install all dependencies  
  
### Using The Web App  
Install Angular in terminal using  
```npm install -g @angular/cli```  
Then, [install Node.js and npm](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm)  
  
run ```ng serve``` in the "GenreGuesser" directory to load up the website  
Finally, run ```server.py```  
  
### Once the web app is loaded,  
Upload any sound file in **.wav format** (must convert), click upload. Then go back a page and refresh to see the results.   
  
## Generating the Data  
The MFCC data was too large to upload to git, you can expect about ~650MB of data generated within a JSON.  
To generate, run ```preProcess.py```, This should generate all of the data into a 'data.json' file in "./preProcessedData/"  
  
## Training the Model  
The model is contained within `train_model.py` and can be trained simply by running the script. Parameters are at the bottom of the file for tweaking if desired  
All models are saved under "./saved_models/"  
  
## Predicting on a song    
`test.py` contains everything needed to generate an output.  
