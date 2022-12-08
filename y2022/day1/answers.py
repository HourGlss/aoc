from y2022.day1.main_a import InputHandler,OutputHandler
from y2022.day1.data import real_input
i = InputHandler()
i.handle_raw_input(real_input)

o = OutputHandler(i)

from y2022.day1.main_b import InputHandler,OutputHandler
i = InputHandler()
i.handle_raw_input(real_input)
o = OutputHandler(i)

