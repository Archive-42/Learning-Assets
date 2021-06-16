#include <torch/csrc/jit/tensorexpr/external_functions.h>

#include <ATen/Functions.h>
#include <ATen/NativeFunctions.h>
#include <torch/csrc/jit/tensorexpr/external_functions_registry.h>

namespace torch {
namespace jit {
namespace tensorexpr {

// A helper function to construct a vector of tensors from raw buffer arguments
std::vector<at::Tensor> constructTensors(
    int64_t bufs_num,
    void** buf_data,
    int64_t* buf_ranks,
    int64_t* buf_dims,
    int8_t* buf_dtypes) {
  std::vector<void*> buf_data_vec;
  std::vector<std::vector<int64_t>> buf_dims_vec;
  std::vector<c10::ScalarType> buf_dtypes_vec;
  int64_t buf_dims_idx = 0;
  for (int64_t i = 0; i < bufs_num; i++) {
    buf_data_vec.push_back(buf_data[i]);
    buf_dims_vec.emplace_back();
    for (int64_t dim = 0; dim < buf_ranks[i]; dim++) {
      buf_dims_vec[i].push_back(buf_dims[buf_dims_idx++]);
    }
    buf_dtypes_vec.push_back(static_cast<c10::ScalarType>(buf_dtypes[i]));
  }

  std::vector<at::Tensor> tensors;
  for (size_t i = 0; i < buf_data_vec.size(); i++) {
    auto options = at::TensorOptions()
                       .dtype(buf_dtypes_vec[i])
                       .layout(at::kStrided)
                       .device(at::kCPU) // TODO: support GPUs too
                       .requires_grad(false);
    tensors.emplace_back(
        at::from_blob(buf_data_vec[i], buf_dims_vec[i], options));
  }
  return tensors;
}

void nnc_aten_conv2d(
    int64_t bufs_num,
    void** buf_data,
    int64_t* buf_ranks,
    int64_t* buf_dims,
    int8_t* buf_dtypes,
    int64_t args_num,
    int64_t* extra_args) {
  std::vector<at::Tensor> tensors =
      constructTensors(bufs_num, buf_data, buf_ranks, buf_dims, buf_dtypes);

  at::Tensor& r = tensors[0];
  const at::Tensor& x = tensors[1];
  const at::Tensor& w = tensors[2];
  if (args_num > 0) {
    // Check that if the extra arguments are provided, then the bias tensor is
    // also present
    TORCH_INTERNAL_ASSERT(args_num == 7 && bufs_num == 4);
    const at::Tensor& b = tensors[3];

    int64_t strideH = extra_args[0];
    int64_t strideW = extra_args[1];
    int64_t paddingH = extra_args[2];
    int64_t paddingW = extra_args[3];
    int64_t dilationH = extra_args[4];
    int64_t dilationW = extra_args[5];
    int64_t groups = extra_args[6];

    try {
      r = at::conv2d(
          x,
          w,
          b,
          {strideH, strideW},
          {paddingH, paddingW},
          {dilationH, dilationW},
          groups);
    } catch (...) {
    }
  } else {
    try {
      r = at::conv2d(x, w);
    } catch (...) {
    }
  }

  // TODO: can i haz an out version of the conv2d?
  memcpy(buf_data[0], r.data_ptr(), r.element_size() * r.numel());
}

void nnc_aten_matmul(
    int64_t bufs_num,
    void** buf_data,
    int64_t* buf_ranks,
    int64_t* buf_dims,
    int8_t* buf_dtypes,
    int64_t args_num,
    int64_t* extra_args) {
  std::vector<at::Tensor> tensors =
      constructTensors(bufs_num, buf_data, buf_ranks, buf_dims, buf_dtypes);

  at::Tensor& r = tensors[0];
  const at::Tensor& x = tensors[1];
  const at::Tensor& w = tensors[2];
  try {
    at::matmul_out(r, x, w);
  } catch (...) {
  }
}

void nnc_aten_mv(
    int64_t bufs_num,
    void** buf_data,
    int64_t* buf_ranks,
    int64_t* buf_dims,
    int8_t* buf_dtypes,
    int64_t args_num,
    int64_t* extra_args) {
  std::vector<at::Tensor> tensors =
      constructTensors(bufs_num, buf_data, buf_ranks, buf_dims, buf_dtypes);

  at::Tensor& r = tensors[0];
  const at::Tensor& x = tensors[1];
  const at::Tensor& w = tensors[2];
  try {
    at::mv_out(r, x, w);
  } catch (...) {
  }
}

void nnc_aten_mm(
    int64_t bufs_num,
    void** buf_data,
    int64_t* buf_ranks,
    int64_t* buf_dims,
    int8_t* buf_dtypes,
    int64_t args_num,
    int64_t* extra_args) {
  std::vector<at::Tensor> tensors =
      constructTensors(bufs_num, buf_data, buf_ranks, buf_dims, buf_dtypes);

  at::Tensor& r = tensors[0];
  const at::Tensor& x = tensors[1];
  const at::Tensor& w = tensors[2];
  try {
    at::mm_out(r, x, w);
  } catch (...) {
  }
}

void nnc_aten_adaptive_avg_pool2d(
    int64_t bufs_num,
    void** buf_data,
    int64_t* buf_ranks,
    int64_t* buf_dims,
    int8_t* buf_dtypes,
    int64_t args_num,
    int64_t* extra_args) {
  std::vector<at::Tensor> tensors =
      constructTensors(bufs_num, buf_data, buf_ranks, buf_dims, buf_dtypes);

  at::Tensor& r = tensors[0];
  const at::Tensor& x = tensors[1];
  int64_t H = extra_args[0];
  int64_t W = extra_args[1];
  try {
    at::adaptive_avg_pool2d_out(r, x, {H, W});
  } catch (...) {
  }
}

void nnc_aten_mean(
    int64_t bufs_num,
    void** buf_data,
    int64_t* buf_ranks,
    int64_t* buf_dims,
    int8_t* buf_dtypes,
    int64_t args_num,
    int64_t* extra_args) {
  std::vector<at::Tensor> tensors =
      constructTensors(bufs_num, buf_data, buf_ranks, buf_dims, buf_dtypes);

  at::Tensor& r = tensors[0];
  const at::Tensor& x = tensors[1];
  int64_t dim = extra_args[0];
  try {
    at::mean_out(r, x, {dim});
  } catch (...) {
  }
}

const static RegisterNNCExternalFunction nnc_conv2d(
    "nnc_aten_conv2d",
    nnc_aten_conv2d);
const static RegisterNNCExternalFunction nnc_matmul(
    "nnc_aten_matmul",
    nnc_aten_matmul);
const static RegisterNNCExternalFunction nnc_mv("nnc_aten_mv", nnc_aten_mv);
const static RegisterNNCExternalFunction nnc_mm("nnc_aten_mm", nnc_aten_mm);
const static RegisterNNCExternalFunction nnc_adaptive_avg_pool2d(
    "nnc_aten_adaptive_avg_pool2d",
    nnc_aten_adaptive_avg_pool2d);
const static RegisterNNCExternalFunction nnc_mean(
    "nnc_aten_mean",
    nnc_aten_mean);

} // namespace tensorexpr
} // namespace jit
} // namespace torch
