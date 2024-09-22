# Chess.com Stats

**Chess.com_stats** is a Python-based project designed to scrape and display user statistics from [Chess.com](https://www.chess.com/). It utilizes Selenium for web scraping and Streamlit for a simple and interactive user interface. The project currently displays key player statistics, including ratings, number of games played, and highest ratings for different game modes (Rapid, Blitz, Bullet).

## Features

- **Web Scraping with Selenium**: Scrapes data from Chess.com using the Chrome WebDriver.
- **Streamlit UI**: Provides a clean and interactive interface for displaying statistics.
- **Basic Statistics**: Displays key metrics:
  - Current rating across different game modes (Rapid, Blitz, Bullet)
  - Number of games played
  - Highest rating achieved
- **Future Enhancements**:
  - Data visualizations for performance tracking
  - Deeper analytics such as game-specific insights

## Project Structure

\`\`\`
Chess.com_stats/
│
├── .ipynb_checkpoints/      # Jupyter notebook checkpoints
├── README.md                # Project documentation
├── chromedriver.exe         # Chrome WebDriver for Selenium
├── main.py                  # Main script with Streamlit UI
├── scraper.ipynb            # Jupyter notebook for scraping stats (Rapid, Blitz, Bullet)
\`\`\`

## Explanation of Files

- `main.py`: The Streamlit app that displays the stats in an interactive UI.
- `scraper.ipynb`: Jupyter notebook for scraping player stats (currently supports Rapid, Blitz, and Bullet modes).
- `chromedriver.exe`: Chrome WebDriver for Selenium scraping.
- `.ipynb_checkpoints`: Automatically generated Jupyter notebook checkpoints.

## Installation

1. **Clone the Repository**:
   \`\`\`bash
   git clone https://github.com/dnp314/Chess.com_stats.git
   \`\`\`

2. **Navigate to the Project Directory**:
   \`\`\`bash
   cd Chess.com_stats
   \`\`\`

3. **Set Up Dependencies**:
   - Ensure Python 3.12.5 is installed.
   - Manually install the required packages for Selenium and Streamlit:
     \`\`\`bash
     pip install selenium streamlit
     \`\`\`

4. **Set Up WebDriver**:
   - Download and set up the Chrome WebDriver according to your Chrome version, and ensure it's added to your system's PATH or place it in the project directory.

## Usage

1. **Scraping Data**: Run the `scraper.ipynb` Jupyter notebook to scrape player statistics for Rapid, Blitz, and Bullet.

2. **Displaying Statistics**: Launch the Streamlit UI to display the scraped data:
   \`\`\`bash
   streamlit run main.py
   \`\`\`
   The Streamlit app will display the player's current ratings, number of games played, and highest ratings for various game modes.

3. **Future Features**:
   - The UI will soon support visualizations and additional performance analytics.

## Future Enhancements

- **Data Visualization**: Add visualizations like rating trends and performance charts.
- **Expanded Analytics**: Incorporate insights into game-specific stats like tactics, time management, and popular openings.
- **Real-time Updates**: Enable real-time scraping and display of live stats.

## Contributing

We welcome contributions! Feel free to open issues or submit pull requests. Please ensure that changes are well-documented and tested.