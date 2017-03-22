import sys
from collections import defaultdict

class BasicInterpreter:
    def __init__(self):
        self._cur_instr = None
        self._vars = defaultdict(int)
        self._instrs = {}
        self._label_chain = {None: None}
        self._val_op_handlers = {
            '+': self._op_add,
            '-': self._op_sub,
            '*': self._op_mul,
            '/': self._op_div,
        }
        self._cond_op_handlers = {
            '=': lambda x, y: self._get_var(x) == self._get_var(y),
            '>': lambda x, y: self._get_var(x) > self._get_var(y),
            '<': lambda x, y: self._get_var(x) < self._get_var(y),
            '<>': lambda x, y: self._get_var(x) != self._get_var(y),
            '<=': lambda x, y: self._get_var(x) <= self._get_var(y),
            '>=': lambda x, y: self._get_var(x) >= self._get_var(y),
        }
        # Each instruction takes one argument, its args as a list.
        # They are responsible for incrementing the instruction counter
        # themselves
        self._instr_handlers = {
            'LET': self._instr_LET,
            'IF': self._instr_IF,
            'PRINT': self._instr_PRINT,
            'PRINTLN': self._instr_PRINTLN,
        }

    def _next_instr(self):
        return self._label_chain[self._cur_instr]

    def _get_var(self, val):
        if val.isdigit():
            return int(val)
        else:
            return self._vars[val]

    def _32_bit_wrap(self, n):
        return ((n + 2147483648) % (4294967296)) - 2147483648

    def _op_sub(self, var1, var2):
        var1 = self._get_var(var1)
        var2 = self._get_var(var2)
        ans = var1 - var2
        return self._32_bit_wrap(ans)

    def _op_add(self, var1, var2):
        var1 = self._get_var(var1)
        var2 = self._get_var(var2)
        ans = var1 + var2
        return self._32_bit_wrap(ans)

    def _op_mul(self, var1, var2):
        var1 = self._get_var(var1)
        var2 = self._get_var(var2)
        ans = var1 * var2
        return self._32_bit_wrap(ans)

    def _op_div(self, var1, var2):
        var1 = self._get_var(var1)
        var2 = self._get_var(var2)
        ans = var1 // var2
        return self._32_bit_wrap(ans)

    def _instr_PRINT(self, args):
        if '"' in args:
            sys.stdout.write(args.strip('"'))
        else:
            sys.stdout.write(str(self._vars[args[0]]))
        self._cur_instr = self._next_instr()

    def _instr_PRINTLN(self, args):
        self._instr_PRINT(args)
        sys.stdout.write('\n')

    def _instr_LET(self, args):
        args = args.split()
        if len(args) == 3:
            assign, _, var = args
            self._vars[assign] = self._get_var(var)
        else:
            assign, _, var1, op, var2 = args
            self._vars[assign] = self._val_op_handlers[op](var1, var2)
        self._cur_instr = self._next_instr()

    def _instr_IF(self, args):
        var1, op, var2, _, _, t_next = args.split()
        if self._cond_op_handlers[op](var1, var2):
            self._cur_instr = int(t_next)
        else:
            self._cur_instr = self._next_instr()

    def add_instructions(self, instructions):
        for instruction in [ins.strip() for ins in instructions]:
            space = instruction.find(' ')
            label, instr = instruction[:space], instruction[space + 1:]
            self._instrs[int(label)] = instr
        label_order = sorted(self._instrs)
        self._label_chain = {l: nl for l, nl in zip(
            [None] + label_order,
            label_order + [None])}

    def loop(self):
        self._cur_instr = self._next_instr()
        while self._cur_instr != None:
            full_instr = self._instrs[self._cur_instr]
            space = full_instr.find(' ')
            inst, args = full_instr[:space], full_instr[space + 1:]
            self._instr_handlers[inst](args)


if __name__ == '__main__':
    bi = BasicInterpreter()
    bi.add_instructions(sys.stdin.readlines())
    bi.loop()

