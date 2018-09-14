import numpy as np
from data import data_cluster
from typing import List
from typing import Union


def pickup_same_cluster(cluster: Union[data_cluster.ClusterCentral, int],
                        data_set: List[data_cluster.Data])->List[data_cluster.Data]:
    """
    データセットから自分と同じクラスタのものを抽出する
    :param cluster: クラスタの中心となるデータ
    :param data_set: 抽出元となるデータセット
    :return: 同じクラスタと判断されたデータセット
    """
    cluster_number = cluster.cluster if type(cluster) == data_cluster.ClusterCentral else cluster
    return [data for data in data_set if data.cluster == cluster_number.cluster]


def calc_new_center_of_cluster(cluster: data_cluster.ClusterCentral,
                               data_set: List[data_cluster.Data])->data_cluster.ClusterCentral:
    """
    クラスタの中心を更新する
    :param cluster: もともとのクラスターデータ
    :param data_set: データセット
    :return: 新しいクラスターデータ
    """
    same_cluster_data_set = pickup_same_cluster(cluster.cluster, data_set)
    data_pos = np.array([data.position for data in same_cluster_data_set])
    gravity = np.sum(data_pos, dtype=float)/len(data_pos)
    return data_cluster.ClusterCentral(gravity, cluster.cluster)


def update_cluster(distance_calculator: data_cluster.FuncDistance,
                   center_cluster_set: List[data_cluster.ClusterCentral],
                   original_data: data_cluster.Data)->data_cluster.Data: