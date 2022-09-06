from y2021.day2.main_a import InputHandler,OutputHandler,Submarine
from y2021.day2.data import real_input

i = InputHandler()
i.handle_raw_input(raw_input=real_input)
s = Submarine()
o = OutputHandler(i,s)
print(o.get_output())

from y2021.day2.main_b import InputHandler,OutputHandler,Submarine
i = InputHandler()
i.handle_raw_input(raw_input=real_input)
s = Submarine()
o = OutputHandler(i,s)
print(o.get_output())