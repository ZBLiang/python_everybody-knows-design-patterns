class Package:
    """包裹信息"""

    def __init__(self, object,name, phoneNum, address):
        self.__object = object
        self.__name = name
        self.__phoneNum = phoneNum
        self.__address = address

    def getName(self):
        return self.__name

    def information(self, isShow = True):
        print("物品：" + str(self.__object),
              "名字：" + str(self.__name),
              "电话：" + str(self.__phoneNum),
              "地址：" + str(self.__address)if isShow else '')

class Station:
    """代拿快递点"""

    def __init__(self, name):
        self.__packages = []
        self.__name = name

    def getName(self):
        return self.__name

    def addPackage(self, package):
        self.__packages.append(package)

    def removePackage(self, package):
        for packageI in self.__packages:
            if(packageI == package):
                self.__packages.remove(packageI)

    def matchPackage(self):
        print(self.getName(),"为您找到以下包裹信息：\n")
        for package in self.__packages:
            package.information(True)
        return self.__packages

    def setPackage(self,proxy,man):
        print(man.getName() + "，您的快递将由" + proxy.getName() + "在" + proxy.getTime() + "送达，请您按时等候")

class Proxy:
    """兼职代拿的打工人"""

    def __init__(self, name, time, path):
        self.__name = name
        self.__time = time
        self.__path = path
        self.__packageS = None

    def getName(self):
        return self.__name

    def getTime(self):
        return self.__time

    def recPackage(self, package):
        print(self.__name + "，您有一个快递将送给" + package.getName() + "，请您按时送货")

class Man:
    """需要帮忙代拿的同学"""

    def __init__(self, name):
        self.__name = name
        # self.__time = time
        # self.__address = address
        self.__packageInfo = None

    def getName(self):
        return self.__name

    def setPackage(self, object, name, phoneNum, address):
        self.__packageInfo = Package(object, name, phoneNum, address)

    def tellStation(self, station):
        station.addPackage(self.__packageInfo)
        print(self.getName() + "在", station.getName(), "发布代拿包裹信息")

def test():
    station = Station("疫情临时代拿点")
    man = Man("小亮")
    proxy = Proxy('小张', "下午", "西区")

    man.setPackage('酸牛奶', '小亮', 13435047257, '广东海洋大学西区海欢a602')
    man.tellStation(station)
    print("小张听到后赶紧去代拿点做兼职")
    packages = station.matchPackage()
    name = input("打工人，请输入你要选择送的同学的名字。")
    for package in packages:
        if package.getName() == name:
            print("匹配成功！")
            break
    proxy.recPackage(package)
    station.setPackage(proxy, man)

test()
