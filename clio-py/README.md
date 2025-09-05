
# clio-py

`clio-py` is a Python framework for building self-adaptive reasoning systems based on the CLIO (Cognitive Loop via In-situ Optimization) concept.

## Installation

To run the examples, you need to install the `graphviz` library:

```bash
pip install graphviz
```

## Usage

To run the example applications, navigate to the `examples` directory and run the Python scripts:

```bash
cd examples
python biology_qa.py
python medicine_qa.py
```

This will generate PNG images of the belief graphs in the `examples` directory.

## Next Steps

The current implementation uses a placeholder `BaseModel`. The next step is to replace this with a real AI model to get meaningful results.
