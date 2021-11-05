def append_common_to_distinct(domain1, domain2, common_proportion):
    distinct_rating_file_1 = domain1 + '_' + domain2 + '/' + domain1 + '_item_list_distinct.dat'
    distinct_rating_file_2 = domain1 + '_' + domain2 + '/' + domain2 + '_item_list_distinct.dat'
    common_rating_file_1 = domain1 + '_' + domain2 + '/' + domain1 + '_item_list_common.dat'
    common_rating_file_2 = domain1 + '_' + domain2 + '/' + domain2 + '_item_list_common.dat'

    output_rating_file_1 = domain1 + '_' + domain2 + '/' + domain1 + '_item_list_proportion_' + str(common_proportion) + '.dat'
    output_rating_file_2 = domain1 + '_' + domain2 + '/' + domain2 + '_item_list_proportion_' + str(common_proportion) + '.dat'

    common_rating_dic_1 = {}
    common_rating_dic_2 = {}
    with open(common_rating_file_1) as f_common1:
        for line in f_common1.readlines():
            u_id = line.strip('\n').split(' ')[0]
            items = line.strip('\n').split(' ')[1:]
            common_rating_dic_1[u_id] = items
    with open(common_rating_file_2) as f_common2:
        for line in f_common2.readlines():
            u_id = line.strip('\n').split(' ')[0]
            items = line.strip('\n').split(' ')[1:]
            common_rating_dic_2[u_id] = items

    index_of_user_1 = 0
    index_of_user_2 = 0
    with open(distinct_rating_file_1) as f_d1:
        with open(output_rating_file_1, 'w') as out_1:
            for line in f_d1.readlines():
                out_1.write(line)
                index_of_user_1 += 1
    with open(distinct_rating_file_2) as f_d2:
        with open(output_rating_file_2, 'w') as out_2:
            for line in f_d2.readlines():
                out_2.write(line)
                index_of_user_2 += 1
    num_common_user = int((index_of_user_1 + index_of_user_2)*common_proportion/100)
    print(num_common_user)
    with open(output_rating_file_1, 'a') as out_1:
        with open(output_rating_file_2, 'a') as out_2:
            for i in range(num_common_user):
                out_1.write(str(index_of_user_1) + ' ' + ' '.join([str(i) for i in common_rating_dic_1[str(i)]]) + '\n')
                index_of_user_1 += 1
                out_2.write(str(index_of_user_2) + ' ' + ' '.join([str(i) for i in common_rating_dic_2[str(i)]]) + '\n')
                index_of_user_2 += 1


# common proportion
x = 40
append_common_to_distinct('Movie', 'Book', common_proportion=x)


