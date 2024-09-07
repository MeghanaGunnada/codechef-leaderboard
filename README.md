# codechef-leaderboard
To build a website that dynamically displays a leaderboard with updated scores, you’ll need to set up a few components:

Web Scraping Script: The script that fetches scores from the users codechef profile webpage to update.
Backend: To manage the data and serve it to the frontend.
Frontend: To display the leaderboard.
## Create a project directory
in a command line navigate to your desktop
### cd C:\Users\MEGHANA\Desktop
create new directory for project
### mkdir leaderboard_project
### cd leaderboard_project
## create a virtual environment
### python -m venv venv
## activate virtual environment
### venv\Scripts\activate
In the leaderboard_project directory, create a file named requirements.txt and add these: Flask, requests, beautifulsoup4
## Install Packages
### pip install -r requirements.txt
Now we already have all the required files, so run and test the application.
## Start Flask Server
### python app.py
## Test the application
To view the leaderboard open the browser and go to 
### http://127.0.0.1:5000
This image shows scores before solving 2 extra problems
![Screenshot 2024-09-08 032931](https://github.com/user-attachments/assets/97154455-0613-40c3-be76-5b8f0736654b)
This image is taken after solving 2 more problems and the score improvement is clearly shown.
![Screenshot 2024-09-08 035013](https://github.com/user-attachments/assets/c300a180-8429-417b-8f72-0c8bbfb941a3)
