# -*- coding: utf-8 -*-



def select_unassigned_variable(csp):
    """Selects the next unassigned variable, or None if there is no more unassigned variables
    (i.e. the assignment is complete).

    For P3, *you do not need to modify this method.*
    """
    
    return next((variable for variable in csp.variables if not variable.is_assigned()))


def order_domain_values(csp, variable):
    """Returns a list of (ordered) domain values for the given variable.

    For P3, *you do not need to modify this method.*
    """
    return [value for value in variable.domain]


def inference(csp, variable):
    """Performs an inference procedure for the variable assignment.

    For P3, *you do not need to modify this method.*
    """
    return True

def is_complete(csp):
    """Returns True when the CSP assignment is complete, i.e. all of the variables in the CSP have values assigned."""
    variables = csp.variables
    for variable in variables:
        if not variable.is_assigned():
            return False
    return True


def is_consistent(csp, variable, value):
    """Returns True when the variable assignment to value is consistent, i.e. it does not violate any of the constraints
        associated with the given variable for the variables that have values assigned.
        
        For example, if the current variable is X and its neighbors are Y and Z (there are constraints (X,Y) and (X,Z)
        in csp.constraints), and the current assignment as Y=y, we want to check if the value x we want to assign to X
        violates the constraint c(x,y).  This method does not check c(x,Z), because Z is not yet assigned."""
    
    for constraint in csp.constraints[variable]:
        if constraint.var2.is_assigned():
            if not constraint.is_satisfied(value,constraint.var2.value):
                return False
    return True


def backtracking_search(csp):
    """Entry method for the CSP solver.  This method calls the backtrack method to solve the given CSP.

    If there is a solution, this method returns the successful assignment (a dictionary of variable to value);
    otherwise, it returns None.

    For P3, *you do not need to modify this method.*
    """
    if backtrack(csp):
        return csp.assignment
    else:
        return None


def backtrack(csp):
    """Performs the backtracking search for the given csp.

    If there is a solution, this method returns True; otherwise, it returns False.
    """

    # TODO implement this
    if is_complete(csp)==True:
        return True
    unassigned=select_unassigned_variable(csp);
    for i in order_domain_values(csp,unassigned):
        if is_consistent(csp, unassigned, i)==True:
            csp.variables.begin_transaction()
            unassigned.assign(i)
            csp.assignment[unassigned]=i
            if backtrack(csp)==True:
                return True
            else:
                csp.variables.rollback()
    return False





