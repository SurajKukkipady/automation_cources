from oops import Calculator

class child_imp_1(Calculator):
    num2 = 200 #class variable

    def get_all_data(self):
        return self.first_num, self.sec_num, self.num, self.num2, self.summation()


child_obj = child_imp_1(10, 20)
print(child_obj.get_all_data())