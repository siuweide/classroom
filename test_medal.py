class country:
    def __init__(self,country_name,gold_medal,silver_medal,bronze_medal):
        self.country_name = country_name
        self.gold_medal = gold_medal
        self.silver_medal = silver_medal
        self.bronze_medal = bronze_medal

    def add_medal(self,rank):
        if rank == 1:
            self.gold_medal += 1
        elif rank == 2:
            self.silver_medal +=1
        elif rank == 3:
            self.bronze_medal += 1

    def __str__(self):
        return '%s: %d 金, %d 银, %d 铜, %d 总' %(
            self.country_name,self.gold_medal,self.silver_medal,self.bronze_medal,self.count_medal)

    @property
    def count_medal(self):
        return  self.gold_medal + self.silver_medal + self.bronze_medal


china = country('中国',30,20,10)
us = country('美国',20,20,10)
uk = country('英国',25,20,20)
print(china)
print(us)
print(uk)
print('按金牌数排序')
medal_list = [china,us,uk]
order_by_count = sorted(medal_list,key=lambda x:x.gold_medal,reverse=True)
for i in order_by_count:
    print(i)
print('按奖牌总数来排序')
medal_list = [china,us,uk]
order_by_count = sorted(medal_list,key=lambda x:x.count_medal,reverse=True)
for i in order_by_count:
    print(i)
