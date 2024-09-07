from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup
import json

app = Flask(__name__)

# Function to read past data
def read_past_data():
    try:
        with open('past_data.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

# Function to update past data
def update_past_data(data):
    past_data = {name: problems_solved for name, problems_solved, _, _, _ in data}
    with open('past_data.json', 'w') as file:
        json.dump(past_data, file)

# Function to scrape scores
def scrape_scores():
    url = [
        ('Meghana Gunnada', 'https://www.codechef.com/users/meghanagunnada'),
        ('Spandana Patta', 'https://www.codechef.com/users/spandu_2004'),
        ('Mahima Cutie', 'https://www.codechef.com/users/mahi_68'),
        ('Pavani Reddy', 'https://www.codechef.com/users/pavani_3113')
    ]
    
    past_data = read_past_data()
    data = []
    
    for name, link in url:
        response = requests.get(link)
        soup = BeautifulSoup(response.content, 'html.parser')
        h3_tags = soup.find_all('h3')
        problems_solved = int(h3_tags[-1].text[23:])  # Adjust index based on actual content
        score = problems_solved * 10
        past_problems_solved = past_data.get(name, 0)
        score_improvement = (problems_solved - past_problems_solved) * 10
        new_problems_solved = problems_solved - past_problems_solved
        data.append((name, problems_solved, score, new_problems_solved, score_improvement))
    
    data.sort(key=lambda x: x[2], reverse=True)  # Sort by score
    return data

@app.route('/')
def leaderboard():
    data = scrape_scores()
    update_past_data(data)
    return render_template('leaderboard.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
