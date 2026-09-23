EXPECTED_BAKE_TIME = 40
def bake_time_remaining(prep_time):
    """A dummy description."""
    return EXPECTED_BAKE_TIME - prep_time

def preparation_time_in_minutes(number_of_layers):
    """A dummy description."""
    return number_of_layers * 2

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """A dummy description."""
    return preparation_time_in_minutes(number_of_layers) + (EXPECTED_BAKE_TIME - bake_time_remaining(elapsed_bake_time))