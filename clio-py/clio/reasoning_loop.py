
import logging
from .belief_graph import BeliefGraph
from .uncertainty import Uncertainty

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class ReasoningLoop:
    """Orchestrates the reasoning process."""
    def __init__(self, base_model, certainty_threshold=0.7, max_retries=3):
        self.base_model = base_model
        self.certainty_threshold = certainty_threshold
        self.max_retries = max_retries

    def run(self, prompt, steering=None):
        """Runs the reasoning loop."""
        belief_graph = BeliefGraph()
        root_node = belief_graph.add_node(f"Prompt: {prompt}")

        # 1. Formulate a plan
        logging.info("Formulating plan...")
        plan = self.base_model.formulate_plan(prompt, steering)
        plan_node = belief_graph.add_node(f"Plan: {plan}")
        belief_graph.add_edge(root_node, plan_node, label="formulates")

        # 2. Execute the plan
        logging.info("Executing plan...")
        results = []
        for step in plan:
            retries = 0
            while retries < self.max_retries:
                logging.info(f"Executing step: {step} (Attempt {retries + 1})")
                result, certainty = self.base_model.execute_step(step, steering)
                logging.info(f"Certainty of step: {certainty}")
                if certainty >= self.certainty_threshold:
                    break
                logging.warning(f"Certainty of step is below threshold. Re-running step.")
                retries += 1
            
            results.append(result)
            step_node = belief_graph.add_node(f"Step: {step}")
            result_node = belief_graph.add_node(f"Result: {result} (Certainty: {certainty})")
            belief_graph.add_edge(plan_node, step_node, label="includes")
            belief_graph.add_edge(step_node, result_node, label="produces")

        # 3. Reflect on the results
        logging.info("Reflecting on results...")
        reflection = self.base_model.reflect(prompt, results, steering)
        reflection_node = belief_graph.add_node(f"Reflection: {reflection}")
        belief_graph.add_edge(result_node, reflection_node, label="reflects_on")

        # 4. Formulate a final conclusion
        logging.info("Formulating conclusion...")
        conclusion = self.base_model.formulate_conclusion(prompt, reflection, steering)
        conclusion_node = belief_graph.add_node(f"Conclusion: {conclusion}")
        belief_graph.add_edge(reflection_node, conclusion_node, label="concludes")

        # 5. Calculate overall uncertainty
        logging.info("Calculating overall uncertainty...")
        overall_certainty = self.base_model.calculate_certainty(conclusion)
        uncertainty = Uncertainty(overall_certainty)

        return belief_graph, uncertainty
