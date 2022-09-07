from y2021.day3.main_a import InputHandler,OutputHandler,PowerConsumption
from y2021.day3.data import real_input

i = InputHandler()
i.handle_raw_input(real_input)
p = PowerConsumption(i.elements)
print(p.get_power_consumption())

from y2021.day3.main_b import InputHandler,PowerConsumption
i = InputHandler()
i.handle_raw_input(real_input)
p = PowerConsumption(i.elements)
print(p.get_life_support_rating())
