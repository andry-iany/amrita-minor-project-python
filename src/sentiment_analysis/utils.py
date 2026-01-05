import os

def _get_absolute_path(relative_path):
    """
    Convert a relative file path to an absolute file path based on the current working directory.
    
    Args:
        relative_path (str): The relative file path.
        
    Returns:
        str: The absolute file path.
    """

    current_directory = os.getcwd()
    joined_path = os.path.join(current_directory, relative_path)
    absolute_path = os.path.abspath(joined_path)

    return absolute_path


PATH_INITIAL_DATASET = _get_absolute_path('../data/raw/IMDB Dataset.csv')
PATH_TRAINING_DATASET = _get_absolute_path('../data/raw/dataset-training.csv')
PATH_UNSEEN_DATA = _get_absolute_path('../data/raw/dataset-unseen.csv')
