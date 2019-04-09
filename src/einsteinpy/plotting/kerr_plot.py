import astropy.units as u
import matplotlib.pyplot as plt
import numpy as np

from einsteinpy.utils import kerr_utils, schwarzschild_radius


class KerrPlotter:
    """
		Class for plotting event horizon and ergosphere of Kerr black hole
	"""

    def __init__(self, mass, maximally=False):
        self.mass = mass
        self.scr = schwarzschild_radius(self.mass * u.kg).value
        self.a = (0.499999 if maximally else 0.3) * self.scr

    def _calc_event_horizon(self, start, end, steps, coord):
        hori = list()
        thetas = np.linspace(start, end, steps)
        for t in thetas:
            hori.append(kerr_utils.event_horizon(self.scr, self.a, t, coord))
        hori1 = np.array(hori)
        Xh, Yh = hori1[:, 0] * np.sin(hori1[:, 1]), hori1[:, 0] * np.cos(hori1[:, 1])
        return Xh, Yh

    def _calc_ergosphere(self, start, end, steps, coord):
        ergo = list()
        thetas = np.linspace(start, end, steps)
        for t in thetas:
            ergo.append(kerr_utils.radius_ergosphere(self.scr, self.a, t, coord))
        ergo1 = np.array(ergo)
        Xe, Ye = ergo1[:, 0] * np.sin(ergo1[:, 1]), ergo1[:, 0] * np.cos(ergo1[:, 1])
        return Xe, Ye

    def plot_event_horizon(self, start, end, steps, color, coord="BL", opacity=0.3):
        Xh, Yh = self._calc_event_horizon(start, end, steps, coord)
        fig, ax = plt.subplots()
        ax.fill(Xh, Yh, color, alpha=opacity)
        ax.fill(-1 * Xh, Yh, color, alpha=opacity)

    def plot_ergosphere(self, start, end, steps, color, coord="BL", opacity=0.3):
        Xe, Ye = self._calc_ergosphere(start, end, steps, coord)
        fig, ax = plt.subplots()
        ax.fill(Xe, Ye, color, alpha=opacity)
        ax.fill(-1 * Xe, Ye, color, alpha=opacity)

    def plot(self, start, end, steps, ergo_color, hori_color, coord="BL", opacity=0.3):
        Xh, Yh = self._calc_event_horizon(start, end, steps, coord)
        Xe, Ye = self._calc_ergosphere(start, end, steps, coord)
        fig, ax = plt.subplots()
        ax.fill(Xh, Yh, hori_color, Xe, Ye, ergo_color, alpha=opacity)
        ax.fill(-1 * Xh, Yh, hori_color, -1 * Xe, Ye, ergo_color, alpha=opacity)

    def show(self):
        plt.show()
