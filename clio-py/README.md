# clio-py

`clio-py` is a Python framework for building self-adaptive reasoning systems based on the CLIO (Cognitive Loop via In-situ Optimization) concept.

## Features

*   **Reasoning Loop:** A core component that orchestrates the reasoning process.
*   **Belief Graph:** A data structure that represents the AI's belief state.
*   **Steerability:** The ability to guide the reasoning process with domain knowledge and programmatic steering.
*   **Gemini API Integration:** The framework is integrated with the Gemini API to provide real-time AI capabilities.
*   **Logging:** The reasoning loop logs each step of the process for easier debugging.
*   **Self-Reflection Module:** The framework can evaluate the certainty of each step and re-run the step if the certainty is below a certain threshold.

## Installation

To run the examples, you need to install the `graphviz` and `google-generativeai` libraries:

```bash
pip install graphviz google-generativeai
```

## Usage

1.  **Set up your API key:** Create a `.env` file in the root of the project and add your Gemini API key to it:

    ```
    GEMINI_API_KEY=<YOUR_API_KEY>
    ```

2.  **Run the examples:** Navigate to the `examples` directory and run the Python scripts:

    ```bash
    cd examples
    python biology_qa.py
    python medicine_qa.py
    ```

## Examples

*   **`biology_qa.py`:** Demonstrates how to use the framework to answer a biology question. This example also shows how to use the self-reflection and programmatic steering features.
*   **`medicine_qa.py`:** Demonstrates how to use the framework to answer a medicine question.