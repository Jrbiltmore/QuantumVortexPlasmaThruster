class UserInput:
    @staticmethod
    def get_simulation_parameters():
        """
        Get simulation parameters from the user.

        Returns:
            simulation_parameters (dict): A dictionary containing simulation parameters.
        """
        simulation_parameters = {}

        # Get user input for simulation parameters
        plasma_type = UserInput.get_plasma_type()
        simulation_parameters['plasma_type'] = plasma_type

        droplet_radius = UserInput.get_droplet_radius()
        simulation_parameters['droplet_radius'] = droplet_radius

        droplet_temperature = UserInput.get_droplet_temperature()
        simulation_parameters['droplet_temperature'] = droplet_temperature

        plasma_density = UserInput.get_plasma_density()
        simulation_parameters['plasma_density'] = plasma_density

        plasma_temperature = UserInput.get_plasma_temperature()
        simulation_parameters['plasma_temperature'] = plasma_temperature

        num_particles = UserInput.get_number_of_particles()
        simulation_parameters['num_particles'] = num_particles

        simulation_time = UserInput.get_simulation_time()
        simulation_parameters['simulation_time'] = simulation_time

        time_step = UserInput.get_time_step()
        simulation_parameters['time_step'] = time_step

        # Additional simulation parameters can be added here

        return simulation_parameters

    @staticmethod
    def get_plasma_type():
        """
        Get user input for plasma type.

        Returns:
            plasma_type (str): Plasma type selected by the user.
        """
        valid_plasma_types = ['Cold', 'Hot', 'Ionized', 'Plasma Jet']
        plasma_type = None
        while plasma_type not in valid_plasma_types:
            print("Valid plasma types: ", valid_plasma_types)
            plasma_type = input("Select plasma type: ").capitalize()
        return plasma_type

    @staticmethod
    def get_droplet_radius():
        """
        Get user input for droplet radius.

        Returns:
            droplet_radius (float): Droplet radius entered by the user.
        """
        droplet_radius = None
        while not isinstance(droplet_radius, (float, int)) or droplet_radius <= 0:
            try:
                droplet_radius = float(input("Enter the droplet radius (in meters): "))
                if droplet_radius <= 0:
                    print("Droplet radius should be a positive value.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        return droplet_radius

    @staticmethod
    def get_droplet_temperature():
        """
        Get user input for droplet temperature.

        Returns:
            droplet_temperature (float): Droplet temperature entered by the user.
        """
        droplet_temperature = None
        while not isinstance(droplet_temperature, (float, int)) or droplet_temperature < 0:
            try:
                droplet_temperature = float(input("Enter the droplet temperature (in Kelvin): "))
                if droplet_temperature < 0:
                    print("Droplet temperature cannot be negative.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        return droplet_temperature

    @staticmethod
    def get_plasma_density():
        """
        Get user input for plasma density.

        Returns:
            plasma_density (float): Plasma density entered by the user.
        """
        plasma_density = None
        while not isinstance(plasma_density, (float, int)) or plasma_density <= 0:
            try:
                plasma_density = float(input("Enter the plasma density (in kg/m^3): "))
                if plasma_density <= 0:
                    print("Plasma density should be a positive value.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        return plasma_density

    @staticmethod
    def get_plasma_temperature():
        """
        Get user input for plasma temperature.

        Returns:
            plasma_temperature (float): Plasma temperature entered by the user.
        """
        plasma_temperature = None
        while not isinstance(plasma_temperature, (float, int)) or plasma_temperature < 0:
            try:
                plasma_temperature = float(input("Enter the plasma temperature (in Kelvin): "))
                if plasma_temperature < 0:
                    print("Plasma temperature cannot be negative.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        return plasma_temperature

    @staticmethod
    def get_number_of_particles():
        """
        Get user input for the number of plasma particles.

        Returns:
            num_particles (int): Number of plasma particles entered by the user.
        """
        num_particles = None
        while not isinstance(num_particles, int) or num_particles <= 0:
            try:
                num_particles = int(input("Enter the number of plasma particles: "))
                if num_particles <= 0:
                    print("Number of particles should be a positive integer.")
            except ValueError:
                print("Invalid input. Please enter a valid integer.")
        return num_particles

    @staticmethod
    def get_simulation_time():
        """
        Get user input for the total simulation time.

        Returns:
            simulation_time (float): Total simulation time entered by the user (in seconds).
        """
        simulation_time = None
        while not isinstance(simulation_time, (float, int)) or simulation_time <= 0:
            try:
                simulation_time = float(input("Enter the total simulation time (in seconds): "))
                if simulation_time <= 0:
                    print("Simulation time should be a positive value.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        return simulation_time

    @staticmethod
    def get_time_step():
        """
        Get user input for the time step of the simulation.

        Returns:
            time_step (float): Time step entered by the user (in seconds).
        """
        time_step = None
        while not isinstance(time_step, (float, int)) or time_step <= 0:
            try:
                time_step = float(input("Enter the time step for the simulation (in seconds): "))
                if time_step <= 0:
                    print("Time step should be a positive value.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        return time_step

    # Additional user input methods for other simulation parameters can be added here
