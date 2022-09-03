from main_a import Sleigh,generate_instructions
from data import raw_input

s = Sleigh()
instructions = generate_instructions(raw_input)
s.use_instructions(instructions)
print(s.get_answer())


from main_b import Sleigh,generate_instructions
from data import raw_input

s = Sleigh()
instructions = generate_instructions(raw_input)
s.use_instructions(instructions)
print(s.get_answer())