# -*- coding: utf-8 -*-

from collections import deque
import operator


def inference(csp, variable):
    """Performs an inference procedure for the variable assignment.

    For P6, *you do not need to modify this method.*
    """
    return ac3(csp, csp.constraints[variable].arcs())


def backtracking_search(csp):
    """Entry method for the CSP solver.  This method calls the backtrack method to solve the given CSP.

    If there is a solution, this method returns the successful assignment (a dictionary of variable to value);
    otherwise, it returns None.

    For P6, *you do not need to modify this method.*
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
        if is_consistent(csp, unassigned, i):
            csp.variables.begin_transaction()
          
            csp.assignment[unassigned]=i
            unassigned.assign(i)
            if inference(csp,unassigned):
                if backtrack(csp):
                    return True
            # if backtrack(csp):
            #     return True
            csp.variables.rollback()
    return False




def ac3(csp, arcs=None):
    """Executes the AC3 or the MAC (p.218 of the textbook) algorithms.
        
        If the parameter 'arcs' is None, then this method executes AC3 - that is, it will check the arc consistency
        for all arcs in the CSP.  Otherwise, this method starts with only the arcs present in the 'arcs' parameter
        in the queue.
        
        Note that the current domain of each variable can be retrieved by 'variable.domains'.
        
        This method returns True if the arc consistency check succeeds, and False otherwise."""
    
    queue_arcs = deque(arcs if arcs is not None else csp.constraints.arcs())
    while len(queue_arcs)>0:
        (xi,xj)=queue_arcs.pop()
        if revise(csp,xi,xj):
            if len(xi.domain)==0:
                return False
            for x in (csp.constraints[xi]):
                if x.var2!=xj:
                    queue_arcs.append((x.var2,xi));

    return True
# TODO implement this


def revise(csp, xi, xj):
    # You may additionally want to implement the 'revise' method.
    revised=False
    satisfied=False
    for vi in xi.domain:
        satisfied=False
        for vj in xj.domain:
            for constraint in csp.constraints[xi,xj]:
                if constraint.is_satisfied(vi,vj):
                    satisfied=True
                    break
            if satisfied:
                break
        if satisfied==False:
            xi.domain.remove(vi)
            revised=True
    return revised


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




def select_unassigned_variable(csp):
    """Selects the next unassigned variable, or None if there is no more unassigned variables
        (i.e. the assignment is complete).
        
        This method implements the minimum-remaining-values (MRV) and degree heuristic. That is,
        the variable with the smallest number of values left in its available domain.  If MRV ties,
        then it picks the variable that is involved in the largest number of constraints on other
        unassigned variables.
        """
    
    # TODO implement this
    min=float("infinity")
 
    count=0
    for variable in csp.variables:
        if variable.is_assigned()==False:
            count=len(variable.domain)
            if count==min:
                num1=0
                num2=0
                for num in csp.constraints[variable]:
                    if num.var1==variable and num.var2==False:
                        num1=num1+1
                for num in csp.constraints[minVar]:
                    if num.var1==minVar and num.var2==False:
                        num2=num2+1
                if num1>num2:
                    minVar=variable
            elif count<min:
                min=count
                minVar=variable
    return minVar

def order_domain_values(csp, variable):
    """Returns a list of (ordered) domain values for the given variable.
        
        This method implements the least-constraining-value (LCV) heuristic; that is, the value
        that rules out the fewest choices for the neighboring variables in the constraint graph
        are placed before others.
        """
    
    # TODO implement this
    list=[]
    for x in variable.domain:
        num=0
        for neighbor in csp.constraints[variable]:
            for neighbourVar in neighbor.var2.domain:
                if neighbor.is_satisfied(x,neighbourVar):
                    num=num+1
        list.append((x,num))
    list=sorted(list,key=operator.itemgetter(1),reverse=True)
    newList=[]
    for value in list:
        newList.append(value[0])
    return newList


