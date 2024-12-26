
# Installation
```bash
conda create --name py311_lc python=3.11
conda activate py311_lc
pip install -r requirements.txt 
conda deactivate
```

Python Install or Uninstall package:
```python
pip install -e .
pip uninstall <package_name>
pip uninstall day_15_agents
```

## Fix
When tried to run `python agents/wiki_lookup_agents.py` it was unable to import the `tools` package. 
As a solution created a `setup.py` file and installed the program in interactive mode.
`pip install -e .`

Uninstall the package after use to ensure 

### LangSmith
To add observability and tracing, just add LangSmith for the details. 
Just add the details in `.env` file and it will handle the rest. 
https://smith.langchain.com/

### Reference Project: 
https://github.com/emarco177/ice_breaker/tree/main
