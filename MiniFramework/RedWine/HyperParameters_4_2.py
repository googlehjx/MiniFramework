# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license. See LICENSE file in the project root for full license information.

from RedWine.EnumDef_6_0 import *

"""

设置超参，例如学习率、最大迭代遍数、批大小、网络类型回归还是分类，多分类还是二分类;
参数的初始化方法、以及优化算法

"""
class HyperParameters_4_2(object):
    def __init__(self, eta=0.1, max_epoch=10000, batch_size=5,
                 net_type=NetType.Fitting, 
                 init_method=InitialMethod.Xavier,
                 optimizer_name=OptimizerName.SGD,
                 stopper = None,
                 regular_name=RegularMethod.Nothing, regular_value=1.0):
        self.eta = eta
        self.max_epoch = max_epoch
        # if batch_size == -1, it is FullBatch
        if batch_size == -1:
            self.batch_size = self.num_example
        else:
            self.batch_size = batch_size
        # end if
        self.net_type = net_type
        self.init_method = init_method
        self.optimizer_name = optimizer_name
        self.stopper = stopper
        self.regular_name = regular_name
        self.regular_value = regular_value

    def toString(self):
        title = str.format("bz:{0},eta:{1},init:{2},op:{3}", self.batch_size, self.eta, self.init_method.name, self.optimizer_name.name)
        if self.regular_name != RegularMethod.Nothing:
            title += str.format(",rgl:{0}:{1}", self.regular_name.name, self.regular_value)
        return title
