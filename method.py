import networkx as nx
import numpy as np
import math

# 输入为networkx的一个子网,以及node的列表
def get_within_module_degree(graph, node_list):
    ans = {}
    value_list = []
    value_all = 0
    node_number = 0
    degree_dict = dict(nx.degree(graph))
    for key, value in degree_dict.items():
        value_all += value
        node_number += 1
    value_mean = value_all / node_number
    value_deviation = np.std(value_list, ddof=0)
    for node in node_list:
        ans[node] = (degree_dict[node] - value_mean) / value_deviation
    return ans


# 输入为属性列表
def get_clique_diversity(attribute_list):
    value_all = 0
    value_number = 0
    for attribute_value in attribute_list:
        value_all += attribute_value
        value_number += 1
    value_mean = value_all / value_number
    ans = np.std(attribute_list, ddof=0) / value_mean
    return ans

# 输入为企业属性字典
def get_firm_distance(attribute_dict):
    attribute_number = len(attribute_dict)
    attribute_list = list(attribute_dict.values())
    sum_squares = 0
    ans = {}
    for key, value in attribute_dict:
        for node_value in attribute_list:
            sum_squares += (node_value - value) * (node_value - value)
        ans[key] = math.sqrt(sum_squares) / attribute_number
    return ans

# 输入为整网和网络中的子群列表
def get_participation_coefficient(graph, subgroup_list):
    ans = {}
    degree_dict = dict(nx.degree(graph))
    subgroup_number = len(subgroup_list)
    for i, subgroup in enumerate(subgroup_list):
        for node in subgroup:
            degree_distribution = [0] * subgroup_number
            neighbers = nx.all_neighbors(graph, node)
            for neighber in neighbers:
                for j in range(subgroup_number):
                    if neighber in subgroup_list[j]:
                        degree_distribution[j] += 1
            sum_squares = 0
            node_degree = degree_dict[node]
            for k in range(subgroup_number):
                sum_squares += degree_distribution[k] / node_degree
            ans[node] = 1 - sum_squares
    return ans

# 输入为两个年份的两个子群
def get_overlap_rate(subgroup_first, subgroup_second)
    union_number = len(subgroup_first)
    intersection_number = 0
    for node in subgroup_second:
        if node in subgroup_first:
            intersection_number += 1
        else:
            union_number += 1
    return intersection_number / union_number

# 输入为两个年份的两个子群
def get_turnover_rate(subgroup_first, subgroup_second):
    return 1 - get_overlap_rate(subgroup_first, subgroup_second)

# 输入为时间t，节点列表，社区年份list，里面是字典，key为社区名，value为社区值
def get_prior_community_affiliation(year, node_list, community_list):
    ans = {}
    for node in node_list:
        node_community = []
        for i in range(year-2000):
            for key, value in community_list[i].items():
                if node in value:
                    if key not in node_community:
                        node_community.append(key)
        ans[node] = len(node_community)
    return ans

# 焦点公司，以及时间t的网络和时间t+1网络, 以及时间t和时间t+1的子群划分
def get_new_bridging_ties(company, net_t, net_t1, community_t, community_t1):
    ans = 0
    net_t_neighber = []
    net_t1_neighber = []
    for node in nx.all_neighbors(net_t, company):
        net_t_neighber.append(node)
    for node in nx.all_neighbors(net_t1, company):
        net_t1_neighber.append(node)
    for node in net_t1_neighber:
        if node not in net_t_neighber:
            ans += 1
    return ans

# 输入为两个节点i和j，j所属的子群，网络
def get_constraint_index(node_i, node_j, community_j ,graph):
    common_neighbers = []
    node_j_inside_link = 0
    neighber_node_i = nx.all_neighbors(graph, node_i)
    for node in nx.all_neighbors(graph, node_j):
        if node in neighber_node_i:
            common_neighbers.append(node)
        if node in community_j:
            node_j_inside_link += 1
    multi_sum = 0
    for node in common_neighbers:
        Piq = graph.get_edge_data(node_i, node)['weight']
        Pjq = graph.get_edge_data(node_j, node)['weight']
        multi_sum += Piq * Pjq
    Pij = graph.get_edge_data(node_i, node_j)['weight']
    ans = (Pij + multi_sum) ** 2 * node_j_inside_link / (len(community_j) - 1)
    return ans

graph = nx.Graph()