from fight_pattern import *

class Store:
    Item_list = []
    Item_list.append(RedDice)
    Item_list.append(BlueDice)
    @classmethod
    def Open_Store(cls,hero):
        choose = None

        printt("<<<<상점>>>>")
        printt("현재 남은 돈:{0}".format(hero.money))
        try:
            while choose != 0 and hero.money >= 0:
                choose = int(input("몇번째 아이템을 구매하시겠습니까?\n1.붉은 마나 주사위 {0}\n2.푸른 마나 주사위 {1}\n(끝낼려면 0)".format(RedDice().price, BlueDice().price)))
                if choose != 0 and hero.money >= 0:
                    select = cls.Item_list[choose-1]()

                    select.buy(hero)

                    printt("현재 남은 돈:{0}".format(hero.money))
                    print("가방:", hero.bag_name_list)
                    printt("*")
                elif choose == 0:
                    printt("상점에서 나갔습니다.")
        except:
            printt("잘못 입력하였습니다.")
            cls.Open_Store(hero)
