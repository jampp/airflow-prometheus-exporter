import yaml


def load_xcom_config(path):
    """Loads the XCom config if present."""
    try:
        with open(path) as file:
            # The FullLoader parameter handles the conversion from YAML
            # scalar values to Python the dictionary format
            return yaml.load(file, Loader=yaml.FullLoader)
    except FileNotFoundError:
        return {}
