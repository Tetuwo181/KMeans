import numpy as np
from typing import Union
from typing import Tuple
from typing import Optional
from typing import Callable
from typing import List

Position = Union[np.ndarray, Tuple]


class AbsData(object):
    """
    データを格納するクラスのベース
    """

    def __init__(self, position: Position):
        """
        :param position: データの座標
        """
        self.__position = np.array(position)

    @property
    def position(self):
        return self.__position


class Data(AbsData):
    """
    データを格納するクラス
    """
    def __init__(self, position: Position, cluster: Optional[int] = None, cluster_real: Optional[int] = None):
        """
        :param position: データの座標
        :param cluster: データが所属すると判定されたクラスタ　ミュータブル
        :param cluster_real: オリジナルのデータに記されているクラスタ
        """
        self.cluster = cluster
        self.__cluster_real = cluster_real
        super.__init__(position)

    @property
    def cluster_real(self):
        return self.__cluster_real


class ClusterCentral(AbsData):
    """
    クラスタの中心地を表すクラス
    """
    def __init__(self, position: Position, cluster: int):
        """
        :param position: クラスタの中心地
        :param cluster: クラスタ
        """
        self.__cluster = cluster
        super.__init__(position)

    @property
    def cluster(self):
        return self.__cluster


DataInput = Union[AbsData, np.ndarray]
FuncDistance = Callable[[DataInput, DataInput], float]


def convert_data(raw_data: DataInput)->np.ndarray:
    if type(raw_data) is np.ndarray:
        return raw_data
    return raw_data.position


def get_distance(calc_distance: FuncDistance,
                 raw_data1: DataInput,
                 raw_data2: DataInput)->float:
    """
    データや座標から距離を求める
    :param calc_distance: 距離を求める関数
    :param raw_data1: 1個目のデータ
    :param raw_data2: 2個目のデータ
    :return: 2点間の距離
    """
    data1 = convert_data(raw_data1)
    data2 = convert_data(raw_data2)
    return calc_distance(data1, data2)


def init_calc_distance(calc_distance: FuncDistance)->FuncDistance:
    """
    先に距離を求める関数だけ初期化する
    :param calc_distance:距離を求める関数
    :return: 2つのデータや座標から距離を求める関数
    """
    return lambda data1, data2: get_distance(calc_distance, data1, data2)
