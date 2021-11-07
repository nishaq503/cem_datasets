from pathlib import Path

import zarr

N5_PATH = Path('/run/media/nishaq/crucial/cem_datasets/jrc_jurkat-1/jrc_jurkat-1.n5')
ZARR_PATH = Path('/run/media/nishaq/crucial/cem_datasets/parsed/jrc_jurkat-1')


def view():
    store = zarr.n5.N5Store(str(N5_PATH))
    # zarr.consolidate_metadata(store)

    root = zarr.group(store)
    em_base = root['em/fibsem-uint16/s0']
    print(em_base.shape)

    # for key in store.keys():
    #     print(key)

    return


if __name__ == '__main__':
    view()
