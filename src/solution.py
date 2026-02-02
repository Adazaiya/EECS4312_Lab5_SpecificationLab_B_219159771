## Student Name: Uzma Alam
## Student ID: 219159771

"""
Stub file for the is allocation feasible exercise.

Implement the function `is_allocation_feasible` to  Determine whether a set of resource requests can be satisfied 
given limited capacities. Take int account any possible constraints. See the lab handout
for full requirements.
"""
    
from typing import Dict, List, Union

Number = Union[int, float]


def is_allocation_feasible(
    resources: Dict[str, Number],
    requests: List[Dict[str, Number]]
) -> bool:
    """
    Determine whether a set of resource requests can be satisfied given limited capacities.

    Args:
        resources : Dict[str, Number], Mapping from resource name to total available capacity.
        requests : List[Dict[str, Number]], List of requests. Each request is a mapping from resource name to the amount required.

    Returns:
        True if the allocation is feasible, False otherwise.


    """
    # TODO: Implement this function
    #raise NotImplementedError("suggest_slots function has not been implemented yet")
    # Create a copy of the resources to track remaining capacities
    remaining_resources = resources.copy()
    # Iterate through the requests
    for request in requests:
        # Check each resource 
        for resource, amount in request.items():
            # If the resource is not available or the requested amount exceeds the remaining capacity
            if resource not in remaining_resources or amount > remaining_resources[resource]:
                return False
            # Substract the requested amount from the remaining capacity
            remaining_resources[resource] -= amount
    
    return True


