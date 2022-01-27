# Recommendation_system
<p> Python recommendation systems are important.
The most common and smartest way for e-commerce websites to display relevant items to their clients is to use an automated system. </p>


<p>This system will be in charge of calculating the probability of similarity between items or user preferences. These systems are called recommendation systems, recommender systems or recommendation engines. A recommender system is one of the most well-known applications of data science and machine learning. In this article, we will go over Python Recommendation Systems. </p>

<p> In fact, almost every major tech company has applied them at some point. Amazon recommends you products, Spotify recommends you music, Google recommends you search results, and YouTube recommends you videos. It is such a common practice that, in 2009, Netflix offered a million dollars to anyone who could improve the accuracy of its movie recommendation system by 10%. </p>

<p> Recommender systems have great commercial importance; they have changed the way websites communicate with their users, increasing interaction to provide a richer experience by autonomously identifying recommendations for individual users based on the user’s past purchases and searches, as well as their behavior.</p>

#### Recommendation systems can be classified into 3 types:

### SIMPLE RECOMMENDERS
<p>This is the type of recommender we will build in this article. It offers generalized recommendations to each user, based on each element’s attributes. In a movie recommendation scenario, it will make recommendations to each user based on movie genre, movie rating or movie title. An example of a simple recommender is IMDd’s Top 250. </p>

### CONTENT-BASED RECOMMENDERS
<p>These recommenders suggest similar items based on a specific one, taking into account each user’s preferences. This system uses item metadata and the general idea behind it is that if a person likes a particular item, they will also like a similar one. This does not involve other users, just each individual’s preferences. Based on what you like, the algorithm will pick items with similar content and recommend them.

It will never recommend products within categories the user has not bought or liked in the past. So, for example, if a user has watched or liked only action movies so far, that’s the only genre the system will recommend.</p>

### COLLABORATIVE FILTERING ENGINES

The collaborative filtering algorithm uses user behavior to select the items to be recommended. These systems are widely used and do not require item metadata like their content-based counterparts. There are different types of collaborating filtering techniques.

### USER-USER COLLABORATIVE FILTERING
<p>This algorithm finds similarities between users grading a score in the process. Based on this score, it picks the most similar users and recommends products that they have previously liked or bought. Essentially, it generates a prediction for item A based on how other users in the neighborhood rated it.</p>

### ITEM-ITEM COLLABORATIVE FILTERING
<p>In this case, the algorithm computes the similarity between each pair of items. Similar items are identified based on how people have rated them in the past. For example, if Julia, Christian, and Vic have given 5 stars to <b> The Lord of the Rings and Harry Potter </b>, the system identifies the items as similar. Therefore, if someone buys <b>The Lord of the Rings, </b>the system also recommends <b>Harry Potter </b> to them.</p>

### Why Python Recommendation Systems? 
<p>You can build this system in virtually any language, but Python certainly takes the most points in this particular field. Python offers readable code for complex algorithms and versatile workflows in machine learning and AI. Python allows you to put all the effort into solving a machine learning problem instead of focusing on the language itself.

Moreover, Python is easy to learn since its code is easy for people to follow, which makes it easier to build models for machine learning. Python is more intuitive than other programming languages. It has many frameworks, libraries, and extensions that simplify the implementation of different functionalities. </p> 

Today, we will be using some of those libraries: 
- Scikit-lear 
Scikit-learn offers simple and efficient tools for predictive data analysis. It is accessible to all and reusable in various contexts. It is built on NumPy, SciPy, and matplotlib. Moreover, it’s open-source and commercially available under the BSD license.

- Pandas (from my favourites)
Pandas is a data analysis and manipulation tool. It was built on top of the Python programming language. This tool is fast, powerful, flexible, open-source and easy-to-use.

- Numpy
NumPy is the fundamental package for scientific computing with Python. Nearly every scientist working with Python draws on the power of NumPy. With this power comes simplicity: a solution in NumPy is often clear and elegant.
 
 Thanks to Joaquin Acuña
 
## Build a simple movie with Python recommendation system 
Lets get to Data and Coding

