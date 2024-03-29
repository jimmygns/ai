# -*- coding: utf-8 -*-
import operator
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
    
    for variable in csp.variables:
        if variable.is_assigned()==False:
            count=len(variable.domain)
            if count==min:
                num1=0
                num2=0
                for num in csp.constraints:
                    if num.var1==variable and num.var2==False or num.var1==False and num.var2==variable:
                        num1=num1+1
                for num in csp.constraints:
                    if num.var1==minVar and num.var2==False or num.var1==False and num.var2==minVar:
                        num2=num2+1
                if num1>=num2:
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


