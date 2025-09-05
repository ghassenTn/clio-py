
import os
import sys

# Add the parent directory to the Python path to allow for imports
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from clio import BaseModel, ReasoningLoop, Steering

def steering_function(belief_graph, results):
    """A simple steering function that checks the certainty of the last step."""
    last_result_node = belief_graph.nodes[-1]
    last_result_certainty = float(last_result_node.label.split("Certainty: ")[1][:-1])
    if last_result_certainty < 0.8:
        return "Re-run the last step with more detail."
    return None

def main():
    """Main function for the software engineering QA example."""
    # 1. Create an instance of the base model
    base_model = BaseModel()

    # 2. Create a steering object with the steering function
    steering = Steering(steering_function=steering_function)

    # 3. Create an instance of the reasoning loop
    reasoning_loop = ReasoningLoop(base_model)

    # 4. Define a software engineering question
    prompt = "create a python system that manages a todo list with add, remove, and view functionalities."

    # 5. Run the reasoning loop with the steering object
    belief_graph, uncertainty = reasoning_loop.run(prompt, steering)

    # 6. Print the final conclusion and uncertainty
    conclusion_node = belief_graph.nodes[-1]
    print(f"Conclusion: {conclusion_node.label}")
    print(f"Uncertainty: {uncertainty}")

    # 7. Generate a visualization of the belief graph
    graphviz_graph = belief_graph.to_graphviz()
    output_path = os.path.join(os.path.dirname(__file__), "software_engineer_belief_graph")
    graphviz_graph.render(output_path, format='png', view=False)
    print(f"Belief graph saved to {output_path}.png")

if __name__ == "__main__":
    main()
