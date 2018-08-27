#include <string>
#include <vector>

using namespace std;

class Result {
 public:
  virtual int GetResult() = 0;
};

class IntResult : public Result {
 public:
  IntResult(int r) : r_(r) {}
  int GetResult() override {
    return r_;
  }
  int r_;
};

class BasicExpr : public Result {
 public:
  BasicExpr(const string &expr) {
    unsigned int i = 0;
    while (i < expr.size()) {
      if (expr[i] == ' ') {
        ++i;
      } else if ('0' <= expr[i] and expr[i] <= '9') {
        int d = 0;
        while (i < expr.size() and '0' <= expr[i] and expr[i] <= '9') {
          d = (d * 10) + (expr[i] - '0'); 
          ++i;
        }
        res_parts.push_back(new IntResult(d));
      } else if (expr[i] == '(') {
        ++i;
        int open_count = 1;
        string brackets;
        while (open_count > 0) {
          brackets += expr[i];
          if (expr[i] == '(') ++open_count;
          else if (expr[i] == ')') --open_count;
          ++i;
        }
        brackets.resize(brackets.size() - 1);
        res_parts.push_back(new BasicExpr(brackets));
      } else if (expr[i] == '+' or expr[i] == '-') {
        ops.push_back(expr[i]);
        ++i;
      }
    }
  }

  int GetResult() override {
    if (res_parts.size() == 1)
      return res_parts[0]->GetResult();
    vector<Result *> new_parts;
    new_parts.push_back(res_parts[0]);
    for (unsigned int i = 0; i < ops.size(); ++i) {
      if (ops[i] == '-') {
        new_parts.back() = new IntResult(
            new_parts.back()->GetResult() - res_parts[i + 1]->GetResult());
      } else {
        new_parts.push_back(res_parts[i + 1]);
      }
    }
    int final_res = 0;
    for (auto &res : new_parts) {
      final_res += res->GetResult();
    }
    return final_res;
  }

  vector<Result *> res_parts;
  vector<char> ops;
};

class Solution {
public:
    int calculate(string s) {
        BasicExpr expr(s);
        return expr.GetResult();
    }
};
