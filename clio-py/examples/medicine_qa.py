import os
import sys

# Add the parent directory to the Python path to allow for imports
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from clio import BaseModel, ReasoningLoop, Steering

def main():
    """Main function for the medicine QA example."""
    try:
        # 1. Create an instance of the base model
        base_model = BaseModel()

        # 2. Create an instance of the reasoning loop
        reasoning_loop = ReasoningLoop(base_model)

        # 3. Define a medicine question
        prompt = "What are the common side effects of aspirin?"

        # 4. Run the reasoning loop
        belief_graph, uncertainty = reasoning_loop.run(prompt)

        # 5. Print the final conclusion and uncertainty
        conclusion_node = belief_graph.nodes[-1]
        print(f"Conclusion: {conclusion_node.label}")
        print(f"Uncertainty: {uncertainty}")

        # 6. Generate a visualization of the belief graph
        graphviz_graph = belief_graph.to_graphviz()
        output_path = os.path.join(os.path.dirname(__file__), "medicine_qa_belief_graph")
        graphviz_graph.render(output_path, format='png', view=False)
        print(f"Belief graph saved to {output_path}.png")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()