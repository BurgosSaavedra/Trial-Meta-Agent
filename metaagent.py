"""
Default script template for the Python Meta Action Agent.

When importing packages, follow the format below to add a comment at the end of declaration 
and specify a version or a package name when the import name is different from expected python package.
This allows the agent to install the correct package version during configuration:
e.g. import paho.mqtt as np  # version=2.1.0 package=paho-mqtt

This script provides a structure for implementing on_create, on_receive, and on_destroy functions.
It includes a basic example using 'foo' and 'bar' concepts to demonstrate functionality.
Each function should return a dictionary object with result data, or None if no result is needed.
"""
import pandas as pd

# Global variable to store the 'foo' and 'bar' values
foo_value = None
bar_value = None

def on_create(data: dict) -> dict | None:
    """
    Initialize the script with provided data.

    Args:
        data (dict): Initialization data containing 'foo' value.

    Returns:
        dict | None: Configuration dictionary with initialized 'foo' value.
    """
    global foo_value
    foo_value = data.get("foo", 0)
    return {
        "apple": foo_value
    }

def on_receive(data: dict) -> dict:
    """
    Process received event data, concatenating 'foo' and 'bar' to create 'foo_bar'.

    Args:
        data (dict): Received event data containing new 'bar' value.
        or data (list[dict]): Received event data when Proces as Batch is ticked
    Returns:
        dict or list[dict]: Result of processing the event data, including a 'foo_bar' value.
    """

    a = data.get("apple", None)
    b = data.get("banana", None)
    c = data.get("orange", "NotFound")

    return {
        "apple": 8*a,
        "banana": 10*b,
        "orange": 2*c
    }

def on_destroy() -> dict | None:
    """
    Clean up resources when the script is being destroyed.

    Returns:
        dict | None: Final values of 'foo' and 'bar'.
    """
    global foo_value, bar_value
    return {
        "final_foo": foo_value,
        "final_bar": bar_value
    }
