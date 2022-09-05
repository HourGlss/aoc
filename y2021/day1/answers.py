from y2021.day1.main_a import InputHandler,OutputHandler,IncreasingTester
from y2021.day1.data import real_input
i = InputHandler()
i.handle_raw_input(real_input)
ita = IncreasingTester(i.elements)
print(ita.iterate_through_list_and_count())

from y2021.day1.main_b import InputHandler,OutputHandler
i = InputHandler()
i.handle_raw_input(real_input)
ita = IncreasingTester(i.elements)
print(ita.iterate_through_list_and_count())