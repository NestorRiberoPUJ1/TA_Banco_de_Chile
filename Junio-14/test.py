

class Aritmetica():

    @staticmethod
    def divisores(num):
        divnum = []
        for index in range(1, num+1):
            if (num % index == 0):
                divnum.append(index)
        return divnum

    @staticmethod
    def maxDiv(num1, num2):
        print(num1, num2)
        d1 = Aritmetica.divisores(num1)
        d2 = Aritmetica.divisores(num2)
        MCD = 1
        for n1 in d1:
            for n2 in d2:
                if (n1 == n2):
                    MCD = n1
        
        return MCD


if __name__ == "__main__":

    print(Aritmetica.maxDiv(12, 16))

    print(Aritmetica.maxDiv(32, 30))