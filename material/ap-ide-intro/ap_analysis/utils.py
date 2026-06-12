

import numpy as np
import matplotlib.pyplot as plt


def get_aps(voltage, voltage_threshold=-0.06, time_window=50):
    """
    voltage: a numpy array that stores the voltages recorded for one cell. The numer of elements is therefore the number of time points
    """
    action_potentials = []
    for index in range(1, len(voltage)):
        crossed_threshold_upward = voltage[index] >= voltage_threshold and voltage[index - 1] < voltage_threshold

        # make sure we are not taking chunks at the very end of the voltage array
        enough_room_left = index + time_window <= len(voltage)
        if crossed_threshold_upward and enough_room_left:

            # take a chunk out of voltate array
            segment = voltage[index:index + time_window]
            action_potentials.append(segment)
    return action_potentials


def amplitude(segment, threshold=-0.06):
    peak_voltage = np.max(segment)
    return peak_voltage - threshold


def rise_time(segment, dt):
    """
    Need help? look up numpy.argmax documentation online.
    """
    peak_index = np.argmax(segment)
    return peak_index * dt


def plot_ap_waves(voltage_control, voltage_drug, dt):
    """Overlay all detected AP waveforms, control in black and drug in red.
    voltage_control: a numpy array of shape (number_of_time_points) that holds the voltages over time
    for a single cell, when no drug was applied.
    voltage_drug: the same but with drug application.
    """

    # detect action potentials
    control_segments = get_aps(voltage_control,)
    drug_segments = get_aps(voltage_drug,)
    
    # plot action potentials
    for segment in control_segments:
        time_axis = np.arange(len(segment)) * dt
        plt.plot(time_axis, segment, color="black")
    for segment in drug_segments:
        time_axis = np.arange(len(segment)) * dt
        plt.plot(time_axis, segment, color="red")
    plt.xlabel("time (s)")
    plt.ylabel("voltage (V)")
    plt.title("AP waveforms (black = control, red = drug)")
    plt.show()


def plot_mean_amplitude(population_control, population_drug, dt):
    """For each cell, compute the mean AP amplitude in each condition,
    then show the values as a scatter plot (control vs. drug).
    
    population_control: a numpy array that has the voltages of different cells over time. It has shape (number of neurons, number of time points). 
    It has different neurons in different rows (i.e. axis 0) and differet times in different columns (i.e. axis 1). These cells were not treated with a drug.

    population_drug: has the same shape as population_control but just tht a drug was applied to the neurons.
    """
    number_of_cells = population_control.shape[0]
    mean_amplitude_control = []
    mean_amplitude_drug = []
    for cell_index in range(number_of_cells):

        # first detect all the action potentials of the cell
        control_trace = population_control[cell_index] # a single cell voltage trace
        drug_trace = population_drug[cell_index]
        control_segments = get_aps(control_trace,) # singe cell action potentials
        drug_segments = get_aps(drug_trace,)
        control_amplitudes = []

        # calculate amplitudes of the individual action potentials (=segments)
        for segment in control_segments:
            control_amplitudes.append(amplitude(segment)) # store all ampliltudes here
        drug_amplitudes = []
        for segment in drug_segments:
            drug_amplitudes.append(amplitude(segment))

        # take the mean over all amplitudes for a single cell.
        mean_amplitude_control.append(np.mean(control_amplitudes))
        mean_amplitude_drug.append(np.mean(drug_amplitudes))
    
    x_control = [0] * number_of_cells
    x_drug = [1] * number_of_cells
    plt.scatter(x_control, mean_amplitude_control, label="control")
    plt.scatter(x_drug, mean_amplitude_drug, label="drug")
    plt.xticks([0, 1], ["control", "drug"])
    plt.ylabel("mean AP amplitude (V)")
    plt.title("Mean AP amplitude per cell")
    plt.legend()
    plt.show()


def plot_mean_rise_time(population_control, population_drug, dt):
    """Compute the mean rise time for each cell and plot it"""
    number_of_cells = population_control.shape[0]
    mean_rise_time_control = []
    mean_rise_time_drug = []
    for cell_index in range(number_of_cells):

        # first detect all the action potentials of the cell
        control_trace = population_control[cell_index]
        drug_trace = population_drug[cell_index]
        control_segments = get_aps(control_trace,)
        drug_segments = get_aps(drug_trace,)
        control_rise_times = []

        # get the rise times here
        for segment in control_segments:
            control_rise_times.append(rise_time(segment, dt))
        drug_rise_times = []
        for segment in drug_segments:
            drug_rise_times.append(rise_time(segment, dt))
        mean_rise_time_control.append(np.mean(control_rise_times))
        mean_rise_time_drug.append(np.mean(drug_rise_times))
    x_control = [0] * number_of_cells
    x_drug = [1] * number_of_cells
    plt.scatter(x_control, mean_rise_time_control, label="control")
    plt.scatter(x_drug, mean_rise_time_drug, label="drug")
    plt.xticks([0, 1], ["control", "drug"])
    plt.ylabel("mean AP rise time (s)")
    plt.title("Mean AP rise time per cell")
    plt.legend()
    plt.show()


# ======================================================================
#  BUGGY VERSIONS OF plot_mean_amplitude  
# ======================================================================

def plot_mean_amplitude_v1(population_control, population_drug, dt):
    number_of_cells = population_control.shape[0]
    mean_amplitude_control = []
    mean_amplitude_drug = []
    for cell_index in range(number_of_cells + 1):
        control_trace = population_control[cell_index]
        drug_trace = population_drug[cell_index]
        control_segments = get_aps(control_trace,)
        drug_segments = get_aps(drug_trace,)
        control_amplitudes = []
        for segment in control_segments:
            control_amplitudes.append(amplitude(segment))
        drug_amplitudes = []
        for segment in drug_segments:
            drug_amplitudes.append(amplitude(segment))
        
        # get one mean amplitude value per cell
        mean_amplitude_control.append(np.mean(control_amplitudes))
        mean_amplitude_drug.append(np.mean(drug_amplitudes))
    x_control = [0] * number_of_cells
    x_drug = [1] * number_of_cells
    plt.scatter(x_control, mean_amplitude_control, label="control")
    plt.scatter(x_drug, mean_amplitude_drug, label="drug")
    plt.xticks([0, 1], ["control", "drug"])
    plt.ylabel("mean AP amplitude (V)")
    plt.legend()
    plt.show()


def plot_mean_amplitude_v2(population_control, population_drug, dt):
    number_of_cells = population_control.shape[0]
    mean_amplitude_control = []
    mean_amplitude_drug = []
    for cell_index in range(number_of_cells):
        control_trace = population_control[cell_index]
        drug_trace = population_drug[cell_index]
        control_segments = get_aps(control_trace,)
        drug_segments = get_aps(drug_trace,)
        control_amplitudes = []
        for segment in control_segments:
            control_amplitudes.append(amplitude(segment))
        drug_amplitudes = []
        for segment in drug_segments:
            drug_amplitudes.append(amplitude(segment))

        # get one mean amplitude value per cell
        mean_amplitude_control.append(np.mean(control_amplitudes))
        mean_amplitude_drug.append(np.mean(drug_amplitudes))
    number_of_points = population_control.shape[1]
    x_control = [0] * number_of_points
    x_drug = [1] * number_of_points
    plt.scatter(x_control, mean_amplitude_control, label="control")
    plt.scatter(x_drug, mean_amplitude_drug, label="drug")
    plt.xticks([0, 1], ["control", "drug"])
    plt.ylabel("mean AP amplitude (V)")
    plt.legend()
    plt.show()


def plot_mean_amplitude_v3(population_control, population_drug, dt):
    number_of_cells = population_control.shape[0]
    mean_amplitude_control = []
    mean_amplitude_drug = []
    for cell_index in range(number_of_cells):
        control_trace = population_control[cell_index]
        drug_trace = population_drug[cell_index]
        control_segments = get_aps(control_trace,)
        drug_segments = get_aps(drug_trace,)
        control_amplitudes = []
        for segment in control_segments:
            control_amplitudes.append(amplitude(segment))
        drug_amplitudes = []
        for segment in control_segments:
            drug_amplitudes.append(amplitude(segment))
        
        # get one mean amplitude value per cell
        mean_amplitude_control.append(np.mean(control_amplitudes))
        mean_amplitude_drug.append(np.mean(drug_amplitudes))
    x_control = [0] * number_of_cells
    x_drug = [1] * number_of_cells
    plt.scatter(x_control, mean_amplitude_control, label="control")
    plt.scatter(x_drug, mean_amplitude_drug, label="drug")
    plt.xticks([0, 1], ["control", "drug"])
    plt.ylabel("mean AP amplitude (V)")
    plt.legend()
    plt.show()
