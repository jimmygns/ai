# -*- coding: utf-8 -*-

from collections import deque


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
                if constraint.is_satisfied(vi,vj)==True:
                    satisfied=True
                    break
            if satisfied:
                break
        if satisfied==False:
            xi.domain.remove(vi)
            revised=True
    return revised