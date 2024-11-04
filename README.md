# Flask Web Application with AI Agents

This repository contains a Flask web application that simulates a dialog between various AI agents and displays the results on a webpage. The application uses Bootstrap for the frontend and shows the messages from the agents as well as an analysis graphic. This code is very simple and only for demonstration purposes.

It also provides a cheat mode that, instead of actually calling the LLMs, their discussion is read from a previously created protocoll.

## Prerequisites

- Anaconda or Miniconda
- Python 3.8 or higher

## Installation

1. **Install Anaconda:**
   - Download and install Anaconda from the official website: https://www.anaconda.com/products/distribution

2. **Clone this repository:**
   ```sh
   git clone <adress of this repo>
   cd path_to_repo
    ```

3. **Create and activate the Anaconda environment:**
   ```sh
   conda create --name autogen_demo python=3.8
   conda activate autogen_demo
   ```

4. **Install dependencies**
   ```sh
   pip install -r requirements.txt
   ```

5. **Set Open AI API Key:**
* store your OpenAI API Key (the "sk-..." string) in a file `api_key` an place it into `app/ai/`.

6. **Start the Flask application:**
   ```sh
   python run.py
   ```

7. **Open the web browser and navigate to the application, go to http://localhost:5000.**

## Usage

Click the "Klicken Sie hier" button to start the dialog between the AI agents.
* If the cheat mode is _off_ in 'app/ai/agents.py', the actual LLM agents are called using your `api_key`. The whole dialog is first computed, then displayed in the browser, so watch the command line for iterative output. After computation, the whole dialog will be stored in a json in `/app/ai` and also handed to the browser client for display.
* If the cheat mode is _on_ in 'app/ai/agents.py', the json file in `/` will be read and displayed. No AI is called.

The messages from the agents will be displayed one by one with a delay of 0.5 seconds per message in the browser. At the end, the analysis graphic analysis.png will be displayed