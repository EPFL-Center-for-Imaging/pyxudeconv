import os
import inspect
import pyxudeconv
#package_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))))))
package_dir = os.path.dirname(inspect.getfile(pyxudeconv))

def airyscan_params():
    params = dict()
    params['model'] = [
        os.path.join(package_dir, 'trained_models','3Dtubes')
    ]
    params['epochoi'] = [40180]
    params['lmbd'] = [0.5, 1, 2]  #np.arange(0.6, 2.1, 0.2),
    params['sigma'] = [1.2]  #np.arange(0.1, 2.1, 0.2)
    return params