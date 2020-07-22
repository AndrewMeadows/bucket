#!/bin/python
#
# compute solar-array and battery capacity

# set these parameters according to the average of your worst week
hours_with_sunlight = 6 
hours_no_sunlight = 24 - hours_with_sunlight
sunless_power_consumption = 100 # watts
sunny_power_consumption = 100 # watts

# Batteries need to supply all of sunless_energy, and then some.
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

# set the battery voltage according to the batteries you're thinking of buying
# lead-acid deep cycle batteries are usually 12V per cell
# but can sometimes come in 6V and 24V
# lithium battery packs come in more variable configurations
battery_voltage = 12 # volts

# compute battery capacity as "amp-hours at aforementioned voltage"
sunless_energy_consumption = hours_no_sunlight * sunless_power_consumption # watt-hours
battery_capacity = BATTERY_SAFETY_FACTOR * sunless_energy_consumption
battery_amp_hours = battery_capacity / battery_voltage

# Now compute solar array size
sunny_energy_consumption = hours_with_sunlight * sunny_power_consumption

total_energy_consumption = sunless_energy_consumption + sunny_energy_consumption

solar_power = total_energy_consumption / hours_with_sunlight


print("sunless_power = {}".format(sunless_power_consumption))
print("sunny power = {}".format(sunny_power_consumption))
print("battery_type = {}".format(battery_type))
print("battery_voltage = {} volts".format(battery_voltage))
print("battery_amp_hours = {} amp-hours".format(battery_amp_hours))
print("solar_power = {} watts minimum".format(solar_power))
