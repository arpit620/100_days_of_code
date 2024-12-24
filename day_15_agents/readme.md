
# Installation
conda create --name py311_lc python=3.11
conda activate py311_lc
pip install -r requirements.txt 
conda deactivate


pip install -e .

## Fix
When tried to run `python agents/wiki_lookup_agents.py` it was unable to import the `tools` package. 
As a solution created a `setup.py` file and installed the program in interactive mode.
`pip install -e .`

