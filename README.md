# FeelingHungry
Feeling hungry? Simply enter what you want to eat, and we'll suggest some healthy, and tasty options!

Everyone craves unhealthy food sometimes, but with Feeling Hungry?, you can get five similar yet healthy suggestions generated using machine learning. Selecting one of the suggestions shows a recipe as well as locations near you where you can purchase that item.

We created a simple vanillaJS website conntected to a Flask web server, analyzed recipe data from MIT's 1M+ dataset using spacy, and made a specialized database for quick search using FAISS and the data from spacy. 

Even though none of us had much web development experience, we decided to make this a web app to minimize the barrier to entry and maximize cross-platform usability. The user simply has to go to the website and enter a food name into our intuitive and beautiful UI.

We faced significant challenges along the way, including trying to figure out how to get the word vector libraries to work, dealing with CSS, and somehow connecting the front end with the Python back end. In addition, we spent a significant effort optimizing the speed of our machine learning and image search. We used spacy and FAISS to create a database of vector maps to reduce the time spent searching for similar recipes in the database. We also significantly reworked and updated an existing image query API for DuckDuckGo to meet our speed requirements.

Working on this project has been extremely rewarding! We learned so much about machine learning, web development, and server management through copious amounts of Googling and problem solving.

Created at UofTHacks VII.

![Main](screenshots/main.jpg?raw=true "Main Screen")
![Results](screenshots/results.jpg?raw=true "Results Screen")
![Info](screenshots/info.jpg?raw=true "Info Screen")
