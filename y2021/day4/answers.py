from y2021.day4.main_a import InputHandler,OutputHandler
from y2021.day4.data import real_draws,real_boards

i = InputHandler()
i.handle_boards(real_boards)
i.handle_draws(real_draws)
o = OutputHandler(i)
print(o.get_output())

from y2021.day4.main_b import InputHandler,OutputHandler
i = InputHandler()
i.handle_boards(real_boards)
i.handle_draws(real_draws)
o = OutputHandler(i)
print(o.get_output())