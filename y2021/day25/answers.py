from y2021.day25.main_a import InputHandler,OutputHandler,SeaFloor
from y2021.day25.data import real_input

s = SeaFloor()
i = InputHandler(s)
i.handle_raw_input(real_input)
print(s.run())

# from y2016.day7.main_b import InputHandler,OutputHandler
# i = InputHandler()
# i.handle_raw_input(real_input)
# o = OutputHandler(i)
# print(o.get_output())