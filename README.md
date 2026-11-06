# CuervosStats - Basketball Analytics Tracker 🏀

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Streamlit](https://img.shields.io/badge/Streamlit-%23FE4B4B.svg?style=for-the-badge&logo=streamlit&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)

## 📌 Overview
CuervosStats is an interactive, real-time web application built with Python and Streamlit, specifically tailored for youth basketball team management. It allows coaches to dynamically load rosters, track live game statistics (points and fouls), and instantly export post-game performance reports to Excel. 

## 🚀 Architecture & Tech Stack
*   **Language:** Python 3
*   **Frontend & State Management:** Streamlit (`st.session_state` for real-time reactivity).
*   **Data Processing:** Pandas (DataFrame manipulation and `.xlsx` generation).
*   **Data Storage:** JSON-based local storage for dynamic roster structuring.

## ✨ Key Features
*   **Real-Time State Management:** Utilizes Streamlit's `session_state` to accurately track live points and fouls for multiple players simultaneously without data loss during UI re-renders.
*   **Dynamic Roster Loading:** A custom data manager parses nested JSON structures (`categories.json`) to dynamically fetch and render team rosters based on selected age categories (e.g., Micro, Infantil, Pasarela) and divisions.
*   **Automated Excel Reporting:** Leverages Pandas DataFrames to compile live match data into structured formats, instantly generating downloadable `.xlsx` files for post-game technical analysis.
*   **Custom UI Injection:** Implements injected CSS (`unsafe_allow_html`) to override default Streamlit styles, creating optimized, touch-friendly action buttons (+/-) tailored for fast-paced courtside data entry.

## 📂 Project Structure
*   `app.py`: Main entry point and match configuration screen.
*   `pages/capture.py`: Real-time statistics capture interface and logic.
*   `data_manager.py`: Core logic for data retrieval and Excel export processing.
*   `categories.json`: Centralized database of athlete rosters segmented by division.

## 💻 Live Demo

You can try out the live application [here](https://cuervostats.streamlit.app/).

*Note: The system is currently configured with active rosters for the following club divisions: **Micro Mixto, Infantil Mixto, Pasarela Mixto, Juvenil Menor Varonil**.*

## ⚙️ Local Development Setup

### 1. Clone the repository
```bash
git clone https://github.com/daninanguyasmu/cuervostats.git
cd cuervostats
```

### 2. Create and activate a virtual environment (Windows)
```bash
python -m venv .venv
.venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the application
```bash
streamlit run app.py
```
*The application will automatically open in your default web browser at `http://localhost:8501`.*

## 👨‍💻 Author
**Daniel Horacio Nanguyasmú Mejía**  
Computer Systems Engineering Student @ TecNM Campus Tuxtla Gutiérrez
