Chess.com Stats
Chess.com_stats is a Python-based project designed to scrape and display user statistics from Chess.com. It utilizes Selenium for web scraping and Streamlit for a simple and interactive user interface. The project currently displays key player statistics, including ratings, number of games played, and highest ratings for different game modes (Rapid, Blitz, Bullet).

Features
Web Scraping with Selenium: Scrapes data from Chess.com using the Chrome WebDriver.
Streamlit UI: Provides a clean and interactive interface for displaying statistics.
Basic Statistics: Displays key metrics:
Current rating across different game modes (Rapid, Blitz, Bullet)
Number of games played
Highest rating achieved
Future Enhancements:
Data visualizations for performance tracking
Deeper analytics such as game-specific insights
Project Structure
bash
Copy code
Chess.com_stats/
│
├── .ipynb_checkpoints/      # Jupyter notebook checkpoints
├── README.md                # Project documentation
├── chromedriver.exe         # Chrome WebDriver for Selenium
├── main.py                  # Main script with Streamlit UI
├── scraper.ipynb            # Jupyter notebook for scraping stats (Rapid, Blitz, Bullet)
Explanation of Files
main.py: The Streamlit app that displays the stats in an interactive UI.
scraper.ipynb: Jupyter notebook for scraping player stats (currently supports Rapid, Blitz, and Bullet modes).
chromedriver.exe: Chrome WebDriver for Selenium scraping.
.ipynb_checkpoints: Automatically generated Jupyter notebook checkpoints.
Installation
Clone the Repository:

bash
Copy code
git clone https://github.com/dnp314/Chess.com_stats.git
Navigate to the Project Directory:

bash
Copy code
cd Chess.com_stats
Set Up Dependencies:

Ensure Python 3.12.5 is installed.
Manually install the required packages for Selenium and Streamlit:
bash
Copy code
pip install selenium streamlit
Set Up WebDriver:

Download and set up the Chrome WebDriver according to your Chrome version, and ensure it's added to your system's PATH or place it in the project directory.
Usage
Scraping Data: Run the scraper.ipynb Jupyter notebook to scrape player statistics for Rapid, Blitz, and Bullet.

Displaying Statistics: Launch the Streamlit UI to display the scraped data:

bash
Copy code
streamlit run main.py
The Streamlit app will display the player's current ratings, number of games played, and highest ratings for various game modes.

Future Features:

The UI will soon support visualizations and additional performance analytics.
Future Enhancements
Data Visualization: Add visualizations like rating trends and performance charts.
Expanded Analytics: Incorporate insights into game-specific stats like tactics, time management, and popular openings.
Real-time Updates: Enable real-time scraping and display of live stats.
Contributing
We welcome contributions! Feel free to open issues or submit pull requests. Please ensure that changes are well-documented and tested.

License
This project is licensed under the MIT License. See the LICENSE file for more details.