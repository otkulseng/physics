import numpy as np
import matplotlib.pyplot as plt


def beta(theta, wave_number, slit_width):
	return 1/2 * wave_number * slit_width * np.sin(theta)


def intensity(beta_values):
	return np.sinc(beta_values)**2


def fraunhofer():
	theta_vals = np.linspace(-np.pi/3, np.pi/3, 1000)
	lambda_red = 650e-9  # 650nm
	k_red = 1/lambda_red
	b = beta(theta_vals, k_red, 5.0e-6)
	I = intensity(b)
	plt.plot(theta_vals, I)
	plt.title("Intensity vs angle")
	plt.xlabel(r"$\theta$")
	plt.ylabel(r"$I/I_0$")

	plt.show()
