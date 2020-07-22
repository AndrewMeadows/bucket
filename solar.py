#!/bin/python
#
# compute solar-array and battery capacity

# Assume the batteries get their most workout at night
# when there is no sun.  This determines the battery capacity.
hours_of_night = 14
nighttime_power_consumption = 100 # watts
nighttime_energy_consumption = hours_of_night * nighttime_power_consumption # watt-hours

# Batteries need to supply all of nighttime energy, and then some.
# This to prevent battery deterioration.
# For lithium batteries we can use a safety factor of a little over 1.0
# (they can be nearly completely depleted and still be fine).
# but for lead-acid deep-cycle batteries the factor should be at least 2.0
# (try to keep them at least 50% charged).
battery_type = "lithium"
if (battery_type == "lithium"):
    BATTERY_SAFETY_FACTOR = 1.2
else:
    BATTERY_SAFETY_FACTOR = 2.0
battery_capacity = BATTERY_SAFETY_FACTOR * nighttime_energy_consumption

# set the battery voltage according to the batteries you're thinking of buying
# lead-acid deep cycle batteries are usually 12V per cell
# but can sometimes come in 6V and 24V
# lithium battery packs come in more variable configurations
battery_voltage = 12 # volts
battery_amp_hours = battery_capacity / battery_voltage

# Now compute solar array size
hours_of_sunlight = 6
daytime_power_consumption = 100 # watts
daytime_energy_consumption = (24 - hours_of_night) * daytime_power_consumption

total_energy_consumption = nighttime_energy_consumption + daytime_energy_consumption

solar_power = total_energy_consumption / hours_of_sunlight


print("nighttime power = {}".format(nighttime_power_consumption))
print("daytime power = {}".format(daytime_power_consumption))
print("battery_type = {}".format(battery_type))
print("battery_voltage = {} volts".format(battery_voltage))
print("battery_amp_hours = {} amp-hours".format(battery_amp_hours))
print("solar_power = {} watts minimum".format(solar_power))
