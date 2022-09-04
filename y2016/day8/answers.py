from y2016.day8.main_a import InputHandler,OutputHandler,LightGrid
from y2016.day8.data import real_input
from y2016.day8.data import width as WIDTH, height as HEIGHT

i = InputHandler()
i.handle_raw_input(real_input)
l = LightGrid(width=WIDTH,height=HEIGHT)
o = OutputHandler(i, l)
print(o.get_output())
print("READ THE LETTERS")
l.print_grid()
# from y2016.day7.main_b import InputHandler,OutputHandler
# i = InputHandler()
# i.handle_raw_input(real_input)
# o = OutputHandler(i)
# print(o.get_output())