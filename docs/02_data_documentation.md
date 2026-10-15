## Sales Dataset Validation

### Dataset Size

The `sales_train_validation.csv` file contains:

- Total records: 30,490
- Total columns: 1,919
- Identifier columns: 6
- Daily sales columns: 1,913

### Record-Level Validation

- Duplicate product-store IDs: 0
- Result: No duplicate values were found in the `id` column.

### Data Grain

Each row represents one product-store combination with historical daily sales values.

The dataset contains 1,913 daily sales columns, ranging from `d_1` to `d_1913`.

### Important Observation

The 30,490 records represent product-store combinations, not unique products. Unique product, department, category, store, and state counts will be calculated separately using the full dataset.


## Sales Dataset Entity Summary

The full sales dataset contains the following unique entities:

| Entity | Unique Count |
|---|---:|
| Products | 3,049 |
| Departments | 7 |
| Categories | 3 |
| Stores | 10 |
| States | 3 |

The dataset contains 30,490 product-store records.

There are 3,049 products and 10 stores. The product count multiplied by the store count equals 30,490, which matches the number of product-store records in the dataset.

All identifier columns contain 30,490 non-null values.

### Identifier Data Types

The five inspected identifier columns are stored as string (`str`) data types:

- `item_id`
- `dept_id`
- `cat_id`
- `store_id`
- `state_id`