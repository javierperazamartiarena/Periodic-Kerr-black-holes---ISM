# Periodic Kerr solution as an infinite soliton chain

This repository contains data supporting the results of the paper:

> **Dmitry Korotkin, Javier Peraza**  
> "Periodic Kerr solution as an infinite soliton chain"  
> *Phys. Rev. D*, 2025.  
> [DOI: 10.1103/mhb9-mhjt](https://doi.org/10.1103/mhb9-mhjt)

## 📁 Repository Contents

- `data/`: Contains `.npz` files with numerical arrays used in simulations and figures.
- `scripts/`: Example code for loading and inspecting the data.

## 📊 How to Use the Data

Use the following script to load and inspect the data:  
[extract-data](scripts/data_extraction.py)

---

## 📦 File Contents

### `Run_final_geom_param_area_fixed_v2.npz`

This file includes the following data fields:

| Key           | Shape              | Dtype     | Description                         |
|---------------|--------------------|-----------|-------------------------------------|
| `sigmas`      | `(20, 20)`         | `float64` | 2D NumPy array                      |
| `N_points`    | `()`               | `int32`   | Scalar integer                      |
| `meridian_Nz` | `()`               | `int32`   | Scalar integer                      |
| `Js`          | `(20,)`            | `float64` | 1D NumPy array                      |
| `Ps`          | `(20, 20)`         | `float64` | 2D NumPy array                      |
| `Ls`          | `(20,)`            | `float64` | 1D NumPy array                      |
| `Dist`        | `(20, 20)`         | `float64` | 2D NumPy array                      |
| `SN_dist`     | `(20, 20)`         | `float64` | 2D NumPy array                      |
| `Area`        | `(20, 20)`         | `float64` | 2D NumPy array                      |
| `Ang_vel`     | `(20, 20)`         | `float64` | 2D NumPy array                      |
| `radii`       | `(20, 20, 20)`     | `float64` | 3D NumPy array                      |
| `meridian`    | `(20, 20, 20)`     | `float64` | 3D NumPy array                      |
| `Kasner`      | `(20, 20)`         | `float64` | 2D NumPy array                      |
| `sigma`       | `()`               | `float64` | Scalar float                        |
| `r_rho`       | `()`               | `int32`   | Scalar integer                      |
| `Ns`          | `()`               | `int32`   | Scalar integer                      |

### `Run_final_geom_param_area_fixed.npz`

This file includes the following data fields:

| Key           | Shape              | Dtype     | Description                         |
|---------------|--------------------|-----------|-------------------------------------|
| `sigmas`      | `(30, 30)`         | `float64` | 2D NumPy array                      |
| `N_points`    | `()`               | `int32`   | Scalar integer                      |
| `meridian_Nz` | `()`               | `int32`   | Scalar integer                      |
| `Js`          | `(30,)`            | `float64` | 1D NumPy array                      |
| `Ps`          | `(30, 30)`         | `float64` | 2D NumPy array                      |
| `Ls`          | `(30,)`            | `float64` | 1D NumPy array                      |
| `Dist`        | `(30, 30)`         | `float64` | 2D NumPy array                      |
| `SN_dist`     | `(30, 30)`         | `float64` | 2D NumPy array                      |
| `Area`        | `(30, 30)`         | `float64` | 2D NumPy array                      |
| `Ang_vel`     | `(30, 30)`         | `float64` | 2D NumPy array                      |
| `radii`       | `(30, 30, 30)`     | `float64` | 3D NumPy array                      |
| `meridian`    | `(30, 30, 30)`     | `float64` | 3D NumPy array                      |
| `Kasner`      | `(30, 30)`         | `float64` | 2D NumPy array                      |
| `sigma`       | `()`               | `float64` | Scalar float                        |
| `r_rho`       | `()`               | `int32`   | Scalar integer                      |
| `Ns`          | `()`               | `int32`   | Scalar integer                      |

### `Run_final_geom_param.npz`

This file includes the following data fields:

| Key           | Shape              | Dtype     | Description                         |
|---------------|--------------------|-----------|-------------------------------------|
| `N_points`    | `()`               | `int32`   | Scalar integer                      |
| `meridian_Nz` | `()`               | `int32`   | Scalar integer                      |
| `ps`          | `(30,)`            | `float64` | 1D NumPy array                      |
| `Ls`          | `(30,)`            | `float64` | 1D NumPy array                      |
| `Dist`        | `(30, 30)`         | `float64` | 2D NumPy array                      |
| `SN_dist`     | `(30, 30)`         | `float64` | 2D NumPy array                      |
| `Area`        | `(30, 30)`         | `float64` | 2D NumPy array                      |
| `Ang_vel`     | `(30, 30)`         | `float64` | 2D NumPy array                      |
| `radii`       | `(30, 30, 30)`     | `float64` | 3D NumPy array                      |
| `meridian`    | `(30, 30, 30)`     | `float64` | 3D NumPy array                      |
| `Kasner`      | `(30, 30)`         | `float64` | 2D NumPy array                      |
| `sigma`       | `()`               | `int32`   | Scalar integer                      |
| `r_rho`       | `()`               | `int32`   | Scalar integer                      |
| `Ns`          | `()`               | `int32`   | Scalar integer                      |

### `Run_final_geom_param_area_fixed.npz`

This file includes the following data fields:

| Key           | Shape              | Dtype     | Description                         |
|---------------|--------------------|-----------|-------------------------------------|
| `N_points`    | `()`               | `int32`   | Scalar integer                      |
| `meridian_Nz` | `()`               | `int32`   | Scalar integer                      |
| `ps`          | `(20,)`            | `float64` | 1D NumPy array                      |
| `Ls`          | `(20,)`            | `float64` | 1D NumPy array                      |
| `Dist`        | `(20, 20)`         | `float64` | 2D NumPy array                      |
| `SN_dist`     | `(20, 20)`         | `float64` | 2D NumPy array                      |
| `Area`        | `(20, 20)`         | `float64` | 2D NumPy array                      |
| `Ang_vel`     | `(20, 20)`         | `float64` | 2D NumPy array                      |
| `radii`       | `(20, 20, 20)`     | `float64` | 3D NumPy array                      |
| `meridian`    | `(20, 20, 20)`     | `float64` | 3D NumPy array                      |
| `Kasner`      | `(20, 20)`         | `float64` | 2D NumPy array                      |
| `sigma`       | `()`               | `int32`   | Scalar integer                      |
| `r_rho`       | `()`               | `int32`   | Scalar integer                      |
| `Ns`          | `()`               | `int32`   | Scalar integer                      |

### `kasner_exp.npz`

This file includes the following data fields:
| Key           | Shape              | Dtype     | Description                         |
|---------------|--------------------|-----------|-------------------------------------|
| `kasner_exp`    | `(30,30)`        | `float64` | 2D NumPy array                      |