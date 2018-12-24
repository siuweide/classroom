with open('test_data.txt',encoding='utf-8') as f:
    scores = f.readlines()

total_score = ['平均',0,0,0,0,0,0,0,0,0]
scores = [x.split() for x in scores]
scores_title = scores[0] #标题
scores_data = scores[1:] #内容

for line in scores_data:
    sum_score = 0
    for data in range(len(line[1:])):
        #将每一项学生的的科目成绩求和
        sum_score += int(line[data+1])
        #将所有学生的每个科目的成绩分别求和
        total_score[data+1] += int(line[data+1])
        if int(line[data+1]) < 60:
            #分数小于60分的话，值改为不及格
            line[data+1]= '不及格'
    #记录每个学生的总成绩
    sum_result = sum_score
    #记录每个学生的平均分
    avg_result = '%.1f' %(sum_result/9)
    #将总成绩写入到内容当中
    line.append(sum_result)
    #将平均分写入到内容当中
    line.append(avg_result)

#统计学生的总成绩，由高到低排
scores_data = sorted(scores_data,key=lambda x:x[11],reverse=True)
#生成新的列表，汇总每一科目的平均分
total_score = ['%.1f' %(x/len(scores_data)) for x in total_score[1:]]
#将列表的内容转化为浮点类型
total_score = [float(x) for x in total_score]
#汇总每个科目的平均分，然后添加进列表里
total_score.append('%.1f' %(sum(total_score[:])))
#求出总平均分，然后添加到列表里
total_score.append('%.1f' %(sum(total_score[:-1])/9))
#将0的序号添加到汇总每一科目的总成绩前面
total_score.insert(0,0)
#将平均的列插入到汇总成绩里面
total_score.insert(1,'平均')

#在标题前面添加名次列
scores_title.insert(0,'名次')
#在标题后面添加总分列
scores_title.append('总分')
#在标题后面添加平均分列
scores_title.append('平均分')

# 将序号添加到每个学生成绩的前面
for i in range(len(scores_data)):
    scores_data[i].insert(0,i+1)

# 将标题和学生成绩情况相加起来合并成一个新的列表
scores_results = [scores_title] + [total_score] + scores_data

new_str_results = []
for result in scores_results:
    #新建一个列表，将列表内含有int的，全部转换为str类型
    str_list_results = [str(x) for x in result]
    # print(str_list_results)
    #将列表转化为字符串
    str_results = ' '.join(str_list_results)
    #将每行字符串的内容添加到new_str_results列表当中
    new_str_results.append(str_results + '\n')

#将结果写入到另一个文件当中
with open('result.txt','w') as w:
    w.writelines(new_str_results)
