import numpy as np

def water_filling(noise_levels, total_power):
    # Sort noise levels in increasing order
    sorted_noise = np.sort(noise_levels)
    print("Sorted Noise:", sorted_noise)
    
    # Initialize power allocation array
    power_allocation = np.zeros_like(noise_levels)
    print("Power allocation:", power_allocation)
    
    # Total available power that we need to allocate
    remaining_power = total_power
    print("Remaining Power:", remaining_power)
    
    # Water-filling process
    # Loop through the list of sorted noise levels
    for i in range(len(noise_levels)):
        # Check if the noise level at index i is less than the remaining power divided by the number of remaining channels
        if sorted_noise[i] < (remaining_power / (len(noise_levels) - i)):
            
            # If the condition is met, allocate power to the i-th channel
            # This power allocation is the remaining power divided by the number of remaining channels, minus the noise level for the current channel
            power_allocation[i] = remaining_power / (len(noise_levels) - i) - sorted_noise[i]
            
            # Subtract the allocated power from the remaining power
            remaining_power -= power_allocation[i]
        else:
            # If the noise level is too high for the remaining power to allocate, break out of the loop since no more power can be allocated
            break
    
    # Assign the remaining power to the original channels based on their sorted positions
    power_allocation_final = np.zeros_like(noise_levels)
    for i, idx in enumerate(np.argsort(noise_levels)):
        power_allocation_final[idx] = power_allocation[i]
        print("Power_allocated=", power_allocation_final[idx])
    
    return power_allocation_final
    
# Example Usage:
noise_levels = np.array([1.0, 0.5, 1.5, 0.8])  # Noise levels of 4 channels
total_power = 10  # Total power to allocate

power_allocation = water_filling(noise_levels, total_power)
print("Power Allocation:", power_allocation)


