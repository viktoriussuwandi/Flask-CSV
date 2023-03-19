Check Off Each Requirement
Now it's time to write some code. Look at the list of requirements below for this project. Just like a real client project, the front-end has already been built for you (If you have more time/want more practice with HTML/Bootstrap you can build the entire project from scratch, just create a new empty PyCharm project). But the main goal of today is to ensure that you are fully comfortable with Flask-WTF, Flask-Bootstrap, Bootstrap classes and do a bit of revision on csv manipulation.

### Requirements
1. The home page should use the css/styles.css file to look like this:
   HINT: Think about bootstrap blocks and super blocks
![1](static/img/1.gif)

2. The /cafes route should render the cafes.html file. This file should contain a Bootstrap table which displays all the data from the cafe-data.csv
   HINT: A object called cafes is passed to cafes.html from the /cafes route. try putting it in a <p> to see what the data in cafes look like.
![2](static/img/2.gif)

3. The location URL should be rendered as an anchor tag <a> in the table instead of the full link. It should have the link text "Maps Link" and the href should be the actual link. HINT: All location links have the first 4 characters as "http".
![3](static/img/3.gif)

5. Clicking on the "Show Me!" button on the home page should take you to the cafes.html page.
![4](static/img/4.gif)

6. There should be a secret route "/add" which doesn't have a button, but those in the know should be able to access it and it should take you to the add.html file.
![5](static/img/5.gif)

7. Use what you have learnt about WTForms to create a quick_form in the add.html page that contains all the fields you can see in the demo below:
HINT: https://flask-wtf.readthedocs.io/en/stable/quickstart.html
https://pythonhosted.org/Flask-Bootstrap/forms.html
![6](static/img/6.gif)

8. Make sure that the location URL field has validation that checks the data entered is a valid URL:
HINT: https://wtforms.readthedocs.io/en/2.3.x/validators/
How to switch off client-side (browser) validation with quick_forms: https://stackoverflow.com/a/61166621/10557313
![7](static/img/7.gif)

9. When the user successfully submits the form on add.html, make sure the data gets added to the cafe-data.csv. It needs to be appended to the end of the csv file. The data from each field need to be comma-separated like all the other lines of data in cafe-data.csv
   HINT: https://www.w3schools.com/python/python_file_write.asp
![8](static/img/8.gif)

10. Make sure all the navigation links in the website work.
![9](static/img/9.gif)

As always remember that the learning happens when you're stuck and solve your problems. The learning doesn't happen in tutorials, it happens when you struggle and overcome your struggles. When you show your struggles who's boss!


So I recommend at least spending 1 hour on this project to write the code and debug. I know it can be frustrating when you feel like you've been stuck on step 1 for half an hour. You feel super unproductive and start questioning your abilities. Don't worry. This happens to the best of us. Just take a break, go for a walk, eat something and come back to the code. You'll be surprised how many breakthroughs you'll make this way.

Only check the solution when you've given the project enough time or if you want to check your solution against mine. (Remember there are multiple ways of doing the same thing, so the sample solution is not the only way to complete this project).