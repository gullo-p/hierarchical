{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "import math\n",
    "import matplotlib.pyplot as plt\n",
    "from scipy.stats import norm\n",
    "from scipy.optimize import fsolve\n",
    "from mpl_toolkits.mplot3d import Axes3D\n",
    "from matplotlib import cm\n",
    "from matplotlib.ticker import LinearLocator, FormatStrFormatter\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.\n",
      " 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.\n",
      " 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.\n",
      " 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.\n",
      " 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.\n",
      " 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.\n",
      " 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.\n",
      " 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.\n",
      " 0. 0. 0. 0. 0. 0. 0. 0.]\n"
     ]
    }
   ],
   "source": [
    "len(MediaX)\n",
    "\n",
    "print(M)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "ename": "IndentationError",
     "evalue": "unexpected indent (<ipython-input-10-06c7b4676c10>, line 23)",
     "output_type": "error",
     "traceback": [
      "\u001b[0;36m  File \u001b[0;32m\"<ipython-input-10-06c7b4676c10>\"\u001b[0;36m, line \u001b[0;32m23\u001b[0m\n\u001b[0;31m    linewidth=0, antialiased=False)\u001b[0m\n\u001b[0m    ^\u001b[0m\n\u001b[0;31mIndentationError\u001b[0m\u001b[0;31m:\u001b[0m unexpected indent\n"
     ]
    }
   ],
   "source": [
    "\n",
    "fig = plt.figure()\n",
    "ax =  Axes3D(fig)\n",
    "\n",
    "sigma = 1\n",
    "alfa2 = 1/2\n",
    "# Make data.\n",
    "x0 = np.linspace(-5,5, num = 200)\n",
    "MediaX = np.linspace(-5,5, num = 200)\n",
    "x0, MediaX = np.meshgrid(x0, MediaX)\n",
    "\n",
    "def m(y):\n",
    "    return y - 1 + 2*norm.cdf(x0[i] - MediaX[i],0,sigma/math.sqrt(2*alfa2))\n",
    "\n",
    "M = np.zeros(200)\n",
    "\n",
    "for i in range(0,200):\n",
    "    M[i] = fsolve(m,0)\n",
    "\n",
    "# Plot the surface.\n",
    "#surf = ax.plot_surface(x0[0:199], MediaX[0:199], M, cmap=cm.coolwarm,\n",
    "                       linewidth=0, antialiased=False)\n",
    "\n",
    "# Customize the z axis.\n",
    "#ax.set_zlim(-1.5, 1.5)\n",
    "#ax.zaxis.set_major_locator(LinearLocator(10))\n",
    "#ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))\n",
    "\n",
    "# Add a color bar which maps values to colors.\n",
    "#fig.colorbar(surf, shrink=0.5, aspect=5)\n",
    "\n",
    "#plt.show()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
