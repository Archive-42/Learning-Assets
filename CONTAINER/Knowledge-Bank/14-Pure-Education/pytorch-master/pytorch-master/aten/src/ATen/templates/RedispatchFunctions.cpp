// ${generated_comment}

#include <ATen/Functions.h>

#include <ATen/core/dispatch/Dispatcher.h>
#include <ATen/core/op_registration/hacky_wrapper_for_legacy_signatures.h>

${static_dispatch_extra_headers}

namespace at {

namespace redispatch {
    ${function_redispatch_definitions}
} // namespace redispatch

} // namespace at
