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

    # TODO implement this


def revise(csp, xi, xj):
    # You may additionally want to implement the 'revise' method.
    revised=false
    notsatisfied=false
    for vi in xi.domain:
        for vj in xj.domain:
            for constraint in csp.constraints[xi,xj]:
                if is_satisfied(vi,vj)==False:
                    notsatisfied=True
                    break
            if(notsatisfied)