# FeelingHungry
Feeling hungry? Simply enter what you want to eat, and we'll suggest some healthy, and tasty options!

Everyone has that feeling when you crave some unhealthy food, but with Feeling Hungry?, you can get five similar, but healthy suggestions generated by our machine learning database, with data from MIT's recipes project. Selecting one of the suggestions shows a recipe as well as locations near you where you can purchase that item.

Even though none of us had much web development experience, we decided to make this a web app to minimize the barrier to entry and maximize cross-platform usability. The user simply has to go to the website and enter a food name into our intuitive and beautiful UI.

We faced significant challenges along the way, including trying to figure out how to get the word vector libraries to work, dealing with CSS, and somehow connecting the front end with the Python back end. In addition, we spent a significant effort optimizing the speed of our machine learning and image search. We used FAISS to generate a database of vector maps to reduce the time spent searching for similar words in the recipes database. We also significantly reworked and updated an existing image query API for DuckDuckGo to meet our speed requirements.

Working on this project has been extremely rewarding! We learned so much about machine learning, web development, and server management through copious amounts of Googling and problem solving.
