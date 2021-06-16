#pragma once

#include <ATen/cuda/CUDAContext.h>

// See https://github.com/pytorch/pytorch/pull/53040
#if defined(CUDART_VERSION) && defined(CUSOLVER_VERSION) && CUSOLVER_VERSION >= 11000
// cuSOLVER version >= 11000 includes 64-bit API
#define USE_CUSOLVER_64_BIT
#endif

#ifdef CUDART_VERSION

namespace at {
namespace cuda {
namespace solver {

#define CUDASOLVER_GETRF_ARGTYPES(Dtype)  \
    cusolverDnHandle_t handle, int m, int n, Dtype* dA, int ldda, int* ipiv, int* info

template<class Dtype>
void getrf(CUDASOLVER_GETRF_ARGTYPES(Dtype)) {
  TORCH_CHECK(false, "at::cuda::solver::getrf: not implemented for ", typeid(Dtype).name());
}
template<>
void getrf<float>(CUDASOLVER_GETRF_ARGTYPES(float));
template<>
void getrf<double>(CUDASOLVER_GETRF_ARGTYPES(double));
template<>
void getrf<c10::complex<double>>(CUDASOLVER_GETRF_ARGTYPES(c10::complex<double>));
template<>
void getrf<c10::complex<float>>(CUDASOLVER_GETRF_ARGTYPES(c10::complex<float>));


#define CUDASOLVER_GETRS_ARGTYPES(Dtype)  \
    cusolverDnHandle_t handle, int n, int nrhs, Dtype* dA, int lda, int* ipiv, Dtype* ret, int ldb, int* info

template<class Dtype>
void getrs(CUDASOLVER_GETRS_ARGTYPES(Dtype)) {
  TORCH_CHECK(false, "at::cuda::solver::getrs: not implemented for ", typeid(Dtype).name());
}
template<>
void getrs<float>(CUDASOLVER_GETRS_ARGTYPES(float));
template<>
void getrs<double>(CUDASOLVER_GETRS_ARGTYPES(double));
template<>
void getrs<c10::complex<double>>(CUDASOLVER_GETRS_ARGTYPES(c10::complex<double>));
template<>
void getrs<c10::complex<float>>(CUDASOLVER_GETRS_ARGTYPES(c10::complex<float>));


#define CUDASOLVER_GESVDJ_ARGTYPES(Dtype, Vtype)  \
    cusolverDnHandle_t handle, cusolverEigMode_t jobz, int econ, int m, int n, Dtype* A, int lda, Vtype* S, Dtype* U, \
    int ldu, Dtype *V, int ldv, int *info, gesvdjInfo_t params

template<class Dtype, class Vtype>
void gesvdj(CUDASOLVER_GESVDJ_ARGTYPES(Dtype, Vtype)) {
  TORCH_INTERNAL_ASSERT(false, "at::cuda::solver::gesvdj: not implemented for ", typeid(Dtype).name());
}
template<>
void gesvdj<float>(CUDASOLVER_GESVDJ_ARGTYPES(float, float));
template<>
void gesvdj<double>(CUDASOLVER_GESVDJ_ARGTYPES(double, double));
template<>
void gesvdj<c10::complex<float>>(CUDASOLVER_GESVDJ_ARGTYPES(c10::complex<float>, float));
template<>
void gesvdj<c10::complex<double>>(CUDASOLVER_GESVDJ_ARGTYPES(c10::complex<double>, double));


#define CUDASOLVER_GESVDJ_BATCHED_ARGTYPES(Dtype, Vtype)  \
    cusolverDnHandle_t handle, cusolverEigMode_t jobz, int m, int n, Dtype* A, int lda, Vtype* S, Dtype* U, \
    int ldu, Dtype *V, int ldv, int *info, gesvdjInfo_t params, int batchSize

template<class Dtype, class Vtype>
void gesvdjBatched(CUDASOLVER_GESVDJ_BATCHED_ARGTYPES(Dtype, Vtype)) {
  TORCH_INTERNAL_ASSERT(false, "at::cuda::solver::gesvdj: not implemented for ", typeid(Dtype).name());
}
template<>
void gesvdjBatched<float>(CUDASOLVER_GESVDJ_BATCHED_ARGTYPES(float, float));
template<>
void gesvdjBatched<double>(CUDASOLVER_GESVDJ_BATCHED_ARGTYPES(double, double));
template<>
void gesvdjBatched<c10::complex<float>>(CUDASOLVER_GESVDJ_BATCHED_ARGTYPES(c10::complex<float>, float));
template<>
void gesvdjBatched<c10::complex<double>>(CUDASOLVER_GESVDJ_BATCHED_ARGTYPES(c10::complex<double>, double));


#define CUDASOLVER_POTRF_ARGTYPES(Dtype)  \
    cusolverDnHandle_t handle, cublasFillMode_t uplo, int n, Dtype* A, int lda, Dtype* work, int lwork, int* info

template<class Dtype>
void potrf(CUDASOLVER_POTRF_ARGTYPES(Dtype)) {
  TORCH_INTERNAL_ASSERT(false, "at::cuda::solver::potrf: not implemented for ", typeid(Dtype).name());
}
template<>
void potrf<float>(CUDASOLVER_POTRF_ARGTYPES(float));
template<>
void potrf<double>(CUDASOLVER_POTRF_ARGTYPES(double));
template<>
void potrf<c10::complex<float>>(CUDASOLVER_POTRF_ARGTYPES(c10::complex<float>));
template<>
void potrf<c10::complex<double>>(CUDASOLVER_POTRF_ARGTYPES(c10::complex<double>));


#define CUDASOLVER_POTRF_BUFFERSIZE_ARGTYPES(Dtype)  \
    cusolverDnHandle_t handle, cublasFillMode_t uplo, int n, Dtype* A, int lda, int* lwork

template<class Dtype>
void potrf_buffersize(CUDASOLVER_POTRF_BUFFERSIZE_ARGTYPES(Dtype)) {
  TORCH_INTERNAL_ASSERT(false, "at::cuda::solver::potrf_buffersize: not implemented for ", typeid(Dtype).name());
}
template<>
void potrf_buffersize<float>(CUDASOLVER_POTRF_BUFFERSIZE_ARGTYPES(float));
template<>
void potrf_buffersize<double>(CUDASOLVER_POTRF_BUFFERSIZE_ARGTYPES(double));
template<>
void potrf_buffersize<c10::complex<float>>(CUDASOLVER_POTRF_BUFFERSIZE_ARGTYPES(c10::complex<float>));
template<>
void potrf_buffersize<c10::complex<double>>(CUDASOLVER_POTRF_BUFFERSIZE_ARGTYPES(c10::complex<double>));


#define CUDASOLVER_POTRF_BATCHED_ARGTYPES(Dtype)  \
    cusolverDnHandle_t handle, cublasFillMode_t uplo, int n, Dtype** A, int lda, int* info, int batchSize

template<class Dtype>
void potrfBatched(CUDASOLVER_POTRF_BATCHED_ARGTYPES(Dtype)) {
  TORCH_INTERNAL_ASSERT(false, "at::cuda::solver::potrfBatched: not implemented for ", typeid(Dtype).name());
}
template<>
void potrfBatched<float>(CUDASOLVER_POTRF_BATCHED_ARGTYPES(float));
template<>
void potrfBatched<double>(CUDASOLVER_POTRF_BATCHED_ARGTYPES(double));
template<>
void potrfBatched<c10::complex<float>>(CUDASOLVER_POTRF_BATCHED_ARGTYPES(c10::complex<float>));
template<>
void potrfBatched<c10::complex<double>>(CUDASOLVER_POTRF_BATCHED_ARGTYPES(c10::complex<double>));


#define CUDASOLVER_ORGQR_BUFFERSIZE_ARGTYPES(Dtype)                        \
  cusolverDnHandle_t handle, int m, int n, int k, const Dtype *A, int lda, \
      const Dtype *tau, int *lwork

template <class Dtype>
void orgqr_buffersize(CUDASOLVER_ORGQR_BUFFERSIZE_ARGTYPES(Dtype)) {
  TORCH_CHECK(
      false,
      "at::cuda::solver::orgqr_buffersize: not implemented for ",
      typeid(Dtype).name());
}
template <>
void orgqr_buffersize<float>(CUDASOLVER_ORGQR_BUFFERSIZE_ARGTYPES(float));
template <>
void orgqr_buffersize<double>(CUDASOLVER_ORGQR_BUFFERSIZE_ARGTYPES(double));
template <>
void orgqr_buffersize<c10::complex<float>>(CUDASOLVER_ORGQR_BUFFERSIZE_ARGTYPES(c10::complex<float>));
template <>
void orgqr_buffersize<c10::complex<double>>(CUDASOLVER_ORGQR_BUFFERSIZE_ARGTYPES(c10::complex<double>));


#define CUDASOLVER_ORGQR_ARGTYPES(Dtype)                             \
  cusolverDnHandle_t handle, int m, int n, int k, Dtype *A, int lda, \
      const Dtype *tau, Dtype *work, int lwork, int *devInfo

template <class Dtype>
void orgqr(CUDASOLVER_ORGQR_ARGTYPES(Dtype)) {
  TORCH_CHECK(
      false,
      "at::cuda::solver::orgqr: not implemented for ",
      typeid(Dtype).name());
}
template <>
void orgqr<float>(CUDASOLVER_ORGQR_ARGTYPES(float));
template <>
void orgqr<double>(CUDASOLVER_ORGQR_ARGTYPES(double));
template <>
void orgqr<c10::complex<float>>(CUDASOLVER_ORGQR_ARGTYPES(c10::complex<float>));
template <>
void orgqr<c10::complex<double>>(CUDASOLVER_ORGQR_ARGTYPES(c10::complex<double>));

#ifdef USE_CUSOLVER_64_BIT

template<class Dtype>
cudaDataType get_cusolver_datatype() {
  TORCH_CHECK(false, "cusolver doesn't support data type ", typeid(Dtype).name());
}
template<> cudaDataType get_cusolver_datatype<float>();
template<> cudaDataType get_cusolver_datatype<double>();
template<> cudaDataType get_cusolver_datatype<c10::complex<float>>();
template<> cudaDataType get_cusolver_datatype<c10::complex<double>>();

void xpotrf_buffersize(
    cusolverDnHandle_t handle, cusolverDnParams_t params, cublasFillMode_t uplo, int64_t n, cudaDataType dataTypeA, const void *A,
    int64_t lda, cudaDataType computeType, size_t *workspaceInBytesOnDevice, size_t *workspaceInBytesOnHost);

void xpotrf(
    cusolverDnHandle_t handle, cusolverDnParams_t params, cublasFillMode_t uplo, int64_t n, cudaDataType dataTypeA, void *A,
    int64_t lda, cudaDataType computeType, void *bufferOnDevice, size_t workspaceInBytesOnDevice, void *bufferOnHost, size_t workspaceInBytesOnHost,
    int *info);

#endif // USE_CUSOLVER_64_BIT

} // namespace solver
} // namespace cuda
} // namespace at

#endif // CUDART_VERSION
