#include <unordered_map>
#include <algorithm>
#include <string.h>


class BasicInterpreter {
  public:
    BasicInterpreter() {
        _cur_instr = -1;
        for (char c = 65; c < 91; ++c) {
            _vars.emplace(c, 0);
        }
    }

    void read_instructions() {
        int label;
        char instr[1000];
        std::vector<int> labels;
        while (scanf("%d %[^\n]\n", &label, instr) != EOF) {
            labels.push_back(label);
            _instrs[label] = strdup(instr);
        }
        std::sort(labels.begin(), labels.end());
        int last = -1;
        for (auto it: labels) {
            _label_chain[last] = it;
            last = it;
        }
        _label_chain[last] = -1;
    }

    void loop() {
        _cur_instr = _next_instruction();
        while (_cur_instr >= 0) {
            char instr[8], args[1000];
            sscanf(_instrs[_cur_instr], "%s %[^\n]", instr, args);
            if (strcmp(instr, "LET") == 0) {
                _instr_LET(args);
            } else if (strcmp(instr, "IF") == 0) {
                _instr_IF(args);
            } else if (strcmp(instr, "PRINT") == 0) {
                _instr_PRINT(args);
            } else {
                _instr_PRINTLN(args);
            }
        }
    }

  private:
    int _cur_instr;
    std::unordered_map<char, int32_t> _vars;
    std::unordered_map<int, char *> _instrs;
    std::unordered_map<int, int> _label_chain;

    int32_t _get_var(const char *v) {
        if (strlen(v) == 1 && isalpha(v[0])) {
            return _vars[v[0]];
        } else {
            return strtol(v, nullptr, 10);
        }
    }

    int _next_instruction() {
        return _label_chain[_cur_instr];
    }

    void _instr_LET(const char *args) {
        char assign, rest[30];
        sscanf(args, "%c = %[^\n]", &assign, rest);

        if (strpbrk(rest, " ") == nullptr) {
            _vars[assign] = _get_var(rest);
        } else {
            char op, var1[13], var2[13];
            sscanf(rest, "%s %c %s", var1, &op, var2);
            switch (op) {
              case '+':
                _vars[assign] = _get_var(var1) + _get_var(var2);
                break;
              case '-':
                _vars[assign] = _get_var(var1) - _get_var(var2);
                break;
              case '*':
                _vars[assign] = _get_var(var1) * _get_var(var2);
                break;
              case '/':
                _vars[assign] = _get_var(var1) / _get_var(var2);
                break;
            }
        }
        _cur_instr = _next_instruction();
    }

    void _instr_IF(const char *args) {
        int label;
        char op[3], var1[13], var2[13];
        sscanf(args, "%s %s %s THEN GOTO %d", var1, op, var2, &label);
        bool result;
        switch (op[0]) {
          case '=':
            result = _get_var(var1) == _get_var(var2);
            break;
          case '>':
            switch (op[1]) {
              case 0:
                result = _get_var(var1) > _get_var(var2);
                break;
              case '=':
                result = _get_var(var1) >= _get_var(var2);
                break;
            }
            break;
          case '<':
            switch (op[1]) {
              case 0:
                result = _get_var(var1) < _get_var(var2);
                break;
              case '=':
                result = _get_var(var1) <= _get_var(var2);
                break;
              case '>':
                result = _get_var(var1) != _get_var(var2);
                break;
            }
            break;
        }
        if (result) {
            _cur_instr = label;
        } else {
            _cur_instr = _next_instruction();
        }
    }

    void _instr_PRINT(const char *args) {
        if (args[0] == '\"') {
            int i = 1, i_max = strlen(args) - 1;
            while (i < i_max) putchar(args[i++]);
        } else {
            printf("%d", _get_var(args));
        }
        _cur_instr = _next_instruction();
    }

    void _instr_PRINTLN(const char *args) {
        _instr_PRINT(args);
        putchar('\n');
    }
 
 };

int main() {
    BasicInterpreter bi = BasicInterpreter();
    bi.read_instructions();
    bi.loop();
    return 0;
}
