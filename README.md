# Text-to-math-problem-solver
Text to math problem solver using Google Gemma-2

# Math Problem Solver using Google Gemma-2

This is a simple Streamlit-based web application that utilizes Google Gemma-2 (or similar large language models) to solve math problems from a text input. The app allows users to input any math-related query, and the system will process and give the correct result using language model-based reasoning.

## Features

- Input math problems in a natural language.
- Automatically processes the question using Google Gemma-2 (or an LLM of choice) for mathematical reasoning.
- Display the solution on the UI.
- User-friendly interface with Streamlit for easy interaction.

## Demo

You can run the app locally or deploy it to a cloud platform like Heroku or Streamlit Sharing. Here's a simple example of a math question you can ask the app:

> **"I have 5 bananas and 7 grapes. I eat 2 bananas and give away 3 grapes. Then I buy a dozen apples and 2 packs of blueberries. Each pack of blueberries contains 25 berries. How many total pieces of fruit do I have at the end?"**

The app will process the query and provide the solution.

## Requirements

Make sure you have the following Python packages installed to run the application:

- `streamlit`
- `openai` (or another large language model API you are using, like Google Gemma-2)
- `pandas` (optional, if you are using any data manipulation)
- `numpy` (optional, if you need math functions)

To install the required libraries, run:

```bash
pip install -r requirements.txt
```

## Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/Math-Problem-Solver.git
   cd Math-Problem-Solver
   ```
2. **Install dependencies:**
   Make sure to have Python 3.7 or higher and install the necessary libraries using the following command:
   ```bash
   pip install -r requirements.txt
   ```
3. **Running the app:**
   To run the app locally, use the following command:
   ```bash
   streamlit run app.py
   ```
   This will start a local server at `http://localhost:8501` where you can interact with the application.

4. **Update Your API Key:**
    If you are using a model like OpenAI or any other LLM, make sure to set up your API keys properly in the code where you make API calls.
    ```python
    import openai

    openai.api_key = "your-api-key"
    ```

## Usage

1. Upon running the app, you'll see an interface asking you to input your math question.
2. Type any math-related question and click "Find my answer" to get the result.
3. The app will process the input and display the solution.

**Example Input:**
```
I have 5 bananas and 7 grapes. I eat 2 bananas and give away 3 grapes. Then I buy a dozen apples and 2 packs of blueberries. Each pack of blueberries contains 25 berries. How many total pieces of fruit do I have at the end?
```

**Expected Output:**
```
The total number of pieces of fruit is 48.
```

## Contributing

Contributions are welcome! If you find any bugs or have improvements in mind, feel free to fork the repository, make the changes, and open a pull request.
```
