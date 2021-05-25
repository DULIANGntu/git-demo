class Company(object):
    def __init__(self, employee_list):
        self.employee = employee_list

    def __getitem__(self, item):
        return self.employee[item]

    def __len__(self):
        return len(self.employee)

company = Company(["tom",'bon','jane'])

company = company[:2]
#定义了_getitem_之后 就可以遍历一个类
for em in company:
    print(em)

print(len(company))