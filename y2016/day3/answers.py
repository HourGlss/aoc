from y2016.day3.main_a import OutputHandler, InputHandler
from y2016.day3.data import real_input


i = InputHandler()
i.handle_raw_input(real_input)
o = OutputHandler(i)
o.build_output()
print(o.get_output())

from y2016.day3.main_b import OutputHandler, InputHandler
from y2016.day3.data import real_input


i = InputHandler()
i.handle_raw_input(real_input)
o = OutputHandler(i)
o.build_output()
print(o.get_output())