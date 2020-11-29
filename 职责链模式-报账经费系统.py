from abc import ABCMeta, abstractmethod

class Person:
    """报账申请人"""
    def __init__(self, name, money, details):
        self.__name = name
        self.__money = money
        self.__details = details
        self.__leader = None

    def getName(self):
        return self.__name

    def getMoney(self):
        return self.__money

    def getDetails(self):
        return self.__details

    def setLeader(self, leader):
        self.__leader = leader

    def reuqest(self):
        print("%s 申请报账 %.2f 元。报账详情：%s" % (self.__name, self.__money, self.__details))
        if( self.__leader is not None):
            self.__leader.handleRequest(self)


class Manager(metaclass=ABCMeta):
    """学校管理人员"""

    def __init__(self, name, title):
        self.__name = name
        self.__title = title
        self._nextHandler = None

    def getName(self):
        return self.__name

    def getTitle(self):
        return self.__title

    def setNextHandler(self, nextHandler):
        self._nextHandler = nextHandler

    @abstractmethod
    def handleRequest(self, person):
        pass

class Adviser(Manager):
    """指导老师"""

    def __init__(self, name, title):
        super().__init__(name, title)

    def handleRequest(self, person):
        if(person.getMoney() <= 2000):
            print("同意 %s 报账，签字人：%s(%s)" % (person.getName(), self.getName(), self.getTitle()))

        elif(person.getMoney() > 2000 and self._nextHandler is not None):
            print('报账金额过大，现正帮你送到分管院长审核签字。')

        if (self._nextHandler is not None):
            self._nextHandler.handleRequest(person)

class Dean(Manager):
    """分管院长"""
    def __init__(self, name, title):
        super().__init__(name, title)

    def handleRequest(self, person):
        if(person.getMoney() >2000 and person.getMoney() <= 20000):
            print("同意 %s 报账，签字人：%s(%s)" % (person.getName(), self.getName(), self.getTitle()))

        elif (person.getMoney() > 20000 and self._nextHandler is not None):
            print('报账金额过大，现正帮你送到校长办公室审核签字。')

        if (self._nextHandler is not None):
            self._nextHandler.handleRequest(person)

class Headmaster(Manager):
    """校长办公室"""

    def __init__(self, name, title):
        super().__init__(name, title)

    def handleRequest(self, person):
        if (person.getMoney() > 20000 and person.getMoney() <= 1000000):
            print("同意 %s 报账，签字人：%s(%s)" % (person.getName(), self.getName(), self.getTitle()))

        elif (person.getMoney() > 1000000 and self._nextHandler is not None):
            print('报账金额过大，不予签字。')

        if (self._nextHandler is not None and person.getMoney() <= 1000000):
            self._nextHandler.handleRequest(person)
        else:
            self._nextHandler.rehandleRequest(person)

class Administrator(Manager):
    """财务处"""

    def __init__(self, name, title):
        super().__init__(name, title)

    def handleRequest(self, person):
        print("%s 的报账申请已审核，情况属实！已备案处理。处理人：%s(%s)\n" % (person.getName(), self.getName(), self.getTitle()))

    def rehandleRequest(self, person):
        print("%s 的报账申请未授权单位签字，不予办理。处理人：%s(%s)\n" % (person.getName(), self.getName(), self.getTitle()))


def testAskForLeave():
    directLeader = Adviser("王峰老师", "项目指导老师")
    departmentLeader = Dean("张院", "分管院长")
    headmaster = Headmaster("潘校", "校长办公室")
    administrator = Administrator("报账小明", "财务处")
    directLeader.setNextHandler(departmentLeader)
    departmentLeader.setNextHandler(headmaster)
    headmaster.setNextHandler(administrator)

    person1 = Person("小张", 1983.88, "购置实验室耗材。")
    person1.setLeader(directLeader)
    person1.reuqest()

    person2 = Person("小焙", 5689.12, "参与PRCV大会总花销。")
    person2.setLeader(directLeader)
    person2.reuqest()

    person3 = Person("小亮", 78934.64, "创建高级实验室。")
    person3.setLeader(directLeader)
    person3.reuqest()

    person4 = Person("打工人", 1526389.12, "想上天。")
    person4.setLeader(directLeader)
    person4.reuqest()

testAskForLeave()