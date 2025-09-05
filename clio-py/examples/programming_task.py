
import os
import sys

# Add the parent directory to the Python path to allow for imports
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from clio import BaseModel, ReasoningLoop, Steering

def programming_steering_function(belief_graph, results):
    """A steering function for programming tasks."""
    # TODO: Implement a more sophisticated steering function for programming tasks.
    return None

def main():
    """Main function for the programming task example."""
    # 1. Create an instance of the base model
    base_model = BaseModel()

    # 2. Create a steering object with the programming steering function
    steering = Steering(steering_function=programming_steering_function)

    # 3. Create an instance of the reasoning loop
    reasoning_loop = ReasoningLoop(base_model)

    # 4. Define a programming task
    prompt = "Write a Python function that takes a list of integers and returns the sum of all the even numbers in the list."

    # 5. Run the reasoning loop with the steering object
    belief_graph, uncertainty = reasoning_loop.run(prompt, steering)

    # 6. Print the final conclusion and uncertainty
    conclusion_node = belief_graph.nodes[-1]
    print(f"Conclusion: {conclusion_node.label}")
    print(f"Uncertainty: {uncertainty}")

    # 7. Generate a visualization of the belief graph
    graphviz_graph = belief_graph.to_graphviz()
    output_path = os.path.join(os.path.dirname(__file__), "programming_task_belief_graph")
    graphviz_graph.render(output_path, format='png', view=False)
    print(f"Belief graph saved to {output_path}.png")

if __name__ == "__main__":
    main()
