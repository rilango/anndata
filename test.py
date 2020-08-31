import rapids_scanpy_funcs
import anndata
import cupy
import scanpy as sc

min_genes_per_cell = 200
max_genes_per_cell = 6000

adata = sc.read('/data/anndata/krasnow_hlca_10x_UMIs.sparse.h5ad')
a = adata.T

genes = a.var_names
# print(type(genes))
# print(genes)

#a = anndata.read_h5ad('/data/anndata/krasnow_hlca_10x_UMIs.sparse.h5ad', as_sparse_fmt=cupy.sparse.csr_matrix)

#print(type(a.X))
#print(dir(a.X))
#print(a.X.shape)
#print(a.X.nnz)
#print(a.X)

# print(type(a.X))
sparse_gpu_array = rapids_scanpy_funcs.filter_cells(\
        a.X, \
        min_genes=min_genes_per_cell, \
        max_genes=max_genes_per_cell)

#print(sparse_gpu_array)

#print('-----')
#print(type(a.var))
#print(a.var)

#print(type(a.var_names))
#print(a.var_names)

