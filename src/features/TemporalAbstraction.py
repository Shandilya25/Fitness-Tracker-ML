{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "f848acd7-e891-4e47-99a2-19a42bbbbdcb",
   "metadata": {},
   "outputs": [],
   "source": [
    "##############################################################\n",
    "#                                                            #\n",
    "#    Mark Hoogendoorn and Burkhardt Funk (2017)              #\n",
    "#    Machine Learning for the Quantified Self                #\n",
    "#    Springer                                                #\n",
    "#    Chapter 4                                               #\n",
    "#                                                            #\n",
    "##############################################################\n",
    "\n",
    "# Updated by Dave Ebbelaar on 22-12-2022\n",
    "\n",
    "import numpy as np\n",
    "import scipy.stats as stats\n",
    "\n",
    "# Class to abstract a history of numerical values we can use as an attribute.\n",
    "class NumericalAbstraction:\n",
    "\n",
    "    # This function aggregates a list of values using the specified aggregation\n",
    "    # function (which can be 'mean', 'max', 'min', 'median', 'std')\n",
    "    def aggregate_value(self, aggregation_function):\n",
    "        # Compute the values and return the result.\n",
    "        if aggregation_function == \"mean\":\n",
    "            return np.mean\n",
    "        elif aggregation_function == \"max\":\n",
    "            return np.max\n",
    "        elif aggregation_function == \"min\":\n",
    "            return np.min\n",
    "        elif aggregation_function == \"median\":\n",
    "            return np.median\n",
    "        elif aggregation_function == \"std\":\n",
    "            return np.std\n",
    "        else:\n",
    "            return np.nan\n",
    "\n",
    "    # Abstract numerical columns specified given a window size (i.e. the number of time points from\n",
    "    # the past considered) and an aggregation function.\n",
    "    def abstract_numerical(self, data_table, cols, window_size, aggregation_function):\n",
    "\n",
    "        # Create new columns for the temporal data, pass over the dataset and compute values\n",
    "        for col in cols:\n",
    "            data_table[\n",
    "                col + \"_temp_\" + aggregation_function + \"_ws_\" + str(window_size)\n",
    "            ] = (\n",
    "                data_table[col]\n",
    "                .rolling(window_size)\n",
    "                .apply(self.aggregate_value(aggregation_function))\n",
    "            )\n",
    "\n",
    "        return data_table"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "id": "0a87f0b1-c096-43ed-929c-30ec77edbd74",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
