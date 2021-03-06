from backpack.core.derivatives.conv2d import (Conv2DDerivatives,
                                              Conv2DConcatDerivatives)

from backpack.extensions.firstorder.batch_grad.batch_grad_base import BatchGradBase


class BatchGradConv2d(BatchGradBase):
    def __init__(self):
        super().__init__(
            derivatives=Conv2DDerivatives(),
            params=["bias", "weight"]
        )


class BatchGradConv2dConcat(BatchGradBase):
    def __init__(self):
        super().__init__(
            derivatives=Conv2DConcatDerivatives(),
            params=["weight"]
        )
