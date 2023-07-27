import unittest
import numpy as np
from src.interface.user_input import UserInput
from src.interface.result_display import ResultDisplay
from src.main import QuantumThrusterSimulation

class TestEndToEnd(unittest.TestCase):
    def setUp(self):
        """
        Setup the necessary objects for the test.
        This runs before each test case.
        """
        self.user_input = UserInput()
        self.result_display = ResultDisplay()
        self.simulation = QuantumThrusterSimulation()

    def tearDown(self):
        """
        Cleanup after the test case.
        This runs after each test case.
        """
        # Depending on your application, you may need to perform some cleanup here.
        # For example, you might need to reset the state of the application, delete files, etc.

    def test_end_to_end(self):
        """
        Test the whole process from user input to result display.
        """
        # Define the input parameters for the simulation.
        plasma_parameters = self.user_input.get_parameters()

        # Run the simulation.
        simulation_results = self.simulation.run(plasma_parameters)

        # Display the results.
        self.result_display.show_results(simulation_results)

        # Verify the results.
        # We use numpy's allclose function to compare the results, which allows us to specify a tolerance level.
        # This is useful when comparing floating point numbers, which may not be exactly equal due to rounding errors.
        expected_results = self.get_expected_results(plasma_parameters)
        np.testing.assert_allclose(simulation_results, expected_results, rtol=1e-05, atol=1e-08)

    def get_expected_results(self, plasma_parameters):
        """
        Get the expected results for the given input parameters.

        Parameters:
            plasma_parameters (dict): The input parameters for the simulation.

        Returns:
            expected_results (dict): The expected results of the simulation.
        """
        # Implement a method to get the expected results for the given input parameters.
        # This could involve reading from a file, calculating the expected results, etc.

        # Example: Calculate the expected results based on the input parameters.
        expected_results = {}
        for parameter, value in plasma_parameters.items():
            # Calculate the expected result for this parameter.
            expected_results[parameter] = value * 2  # This is a placeholder calculation.

        return expected_results

if __name__ == "__main__":
    unittest.main()
