from y2016.day2.main_a import OutputHandler, Keypad, InputHandler
from y2016.day2.data import real_input

k = Keypad()
i = InputHandler()
i.handle_raw_input(real_input)
o = OutputHandler(k, i)
o.build_output()
print(o.get_output())

from y2016.day2.main_b import OutputHandler, Keypad, InputHandler

k = Keypad()
i = InputHandler()
i.handle_raw_input(real_input)
o = OutputHandler(k, i)
o.build_output()
print(o.get_output())
