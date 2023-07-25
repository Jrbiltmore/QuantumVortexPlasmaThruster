import os

# Define the directory structure
dirs = [
    "docs",
    "src/models",
    "src/solvers",
    "src/visualization",
    "src/interface",
    "tests/unit",
    "tests/integration",
    "tests/e2e",
    "utils",
    "env"
]

# Define the files
files = [
    "docs/user_guide.md",
    "docs/developer_guide.md",
    "src/models/plasma_model.py",
    "src/models/surface_tension_model.py",
    "src/models/thermodynamics_model.py",
    "src/solvers/numerical_methods.py",
    "src/visualization/data_visualization.py",
    "src/interface/user_input.py",
    "src/interface/result_display.py",
    "src/main.py",
    "tests/unit/test_plasma_model.py",
    "tests/unit/test_surface_tension_model.py",
    "tests/unit/test_thermodynamics_model.py",
    "tests/unit/test_numerical_methods.py",
    "tests/integration/test_integration.py",
    "tests/e2e/test_end_to_end.py",
    "utils/logging.py",
    "env/Dockerfile",
    "README.md",
    "requirements.txt",
    ".gitignore",
    "Jenkinsfile"
]

# Create directories
for directory in dirs:
    os.makedirs(directory, exist_ok=True)

# Create files
for file in files:
    with open(file, 'w') as fp:
        pass

print("Directories and files have been created successfully.")
