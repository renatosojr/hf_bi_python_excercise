<h1>HF BI Python Exercise</h1>
This repository contains a Python project aimed at processing recipe data from a JSON file, identifying recipes that include "chilies" as an ingredient, and evaluating their cooking difficulty based on preparation and cook times.

<h2>Getting Started</h2>
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

<h3>Prerequisites</h3>
Before you begin, ensure you have the following installed:

  * Python 3.x
  * pip (Python package installer)
    
<h3>Installation</h3>
  <h4>Clone the Repository</h4>
  Clone the Repository:
  
    git clone https://github.com/renatosojr/hf_bi_python_excercise.git
    cd hf_bi_python_excercise
      
  <h4>Set up a Virtual Environment</h4>

It's a good practice to use a virtual environment for Python projects. To set up a virtual environment, run:

  python -m venv hf_bi_python_excercise
  <br/>
  source venv/bin/activate
  

<h5>Install the project dependencies using pip:</h5>

Run: <br/>
pip install -r requirements.txt

<h5>Running the Project</h5>
Once the installation is complete, you can run the project with:

python ./main.py
<br/>
This command will execute the main script, which downloads the recipe JSON, processes the data, and outputs results based on the criteria defined in the project.

<h5>Running Tests</h5>
To run the unit tests and ensure everything is working as expected, execute:

<br/>
python -m unittest discover -s tests
<br/><br/>
This command will discover and run all tests in the tests directory.

<br/><br/>
License
This project is licensed under the MIT License - see the LICENSE file for details
