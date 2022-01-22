#!/usr/bin/env python3

import numpy as np

from hb_common import DynamicsBase, Params, Command


class Dynamics(DynamicsBase):
    def __init__(self):
        super().__init__()

    def dynamics(self, param, state, command):
        l1 = param.l1
        l2 = param.l2
        l3x = param.l3x
        l3y = param.l3y
        l3z = param.l3z
        lT = param.lT
        d = param.d
        m1 = param.m1
        m2 = param.m2
        m3 = param.m3
        J1x = param.J1x
        J1y = param.J1y
        J1z = param.J1z
        J2x = param.J2x
        J2y = param.J2y
        J2z = param.J2z
        J3x = param.J3x
        J3y = param.J3y
        J3z = param.J3z
        Bphi = param.Bphi
        Bth = param.Bth
        Bpsi = param.Bpsi
        km = param.km
        g = param.g

        phi = state[0]
        theta = state[1]
        psi = state[2]
        phid = state[3]
        thetad = state[4]
        psid = state[5]

        # forces
        fl = km * command.left
        fr = km * command.right

        # angle rate dynamics
        sphi = np.sin(phi)
        cphi = np.cos(phi)
        stheta = np.sin(theta)
        ctheta = np.cos(theta)
        spsi = np.sin(psi)
        cpsi = np.cos(psi)

        ################################################
        # Implement Dynamics for Accelerations Here    #

        M = np.zeros((3, 3))
        M[0, 0] =
        M[0, 2] =
        M[1, 1] =
        M[1, 2] =
        M[2, 0] =
        M[2, 1] =
        M[2, 2] =

        c = np.zeros((3, 1))
        c[0] =
        c[1] =
        c[2] =

        dPdq = np.zeros((3, 1))
        dPdq[1] =

        Tau = np.zeros((3, 1))
        Tau[0] =
        Tau[1] =
        Tau[2] =

        B = np.zeros((3, 3))
        B[0, 0] =
        B[1, 1] =
        B[2, 2] =

        ################################################

        xdot = np.zeros((6, 1))
        xdot[0:3] = state[3:6]  # angle dynamics
        xdot[3:6] = np.linalg.solve(
            M, Tau - B@xdot[0:3] - c - dPdq)  # angle rate dynamics

        return xdot


if __name__ == '__main__':
    d = Dynamics()
    d.run()
