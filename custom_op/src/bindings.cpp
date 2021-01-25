#include <torch/script.h>

#include "ball_query/ball_query.hpp"
//#include "grouping/grouping.hpp"
//#include "interpolate/neighbor_interpolate.hpp"
//#include "interpolate/trilinear_devox.hpp"
//#include "sampling/sampling.hpp"
//#include "voxelization/vox.hpp"

TORCH_LIBRARY(_pvcnn_backend, m) {
  //m.def("gather_features_forward", &gather_features_forward);
  //m.def("gather_features_backward", &gather_features_backward);
  //m.def("furthest_point_sampling", &furthest_point_sampling_forward);
  m.def("ball_query", &ball_query_forward);
  //m.def("grouping_forward", &grouping_forward);
  //m.def("grouping_backward", &grouping_backward);
  //m.def("three_nearest_neighbors_interpolate_forward", &three_nearest_neighbors_interpolate_forward);
  //m.def("three_nearest_neighbors_interpolate_backward", &three_nearest_neighbors_interpolate_backward);
  //m.def("trilinear_devoxelize_forward", &trilinear_devoxelize_forward);
  //m.def("trilinear_devoxelize_backward", &trilinear_devoxelize_backward);
  //m.def("avg_voxelize_forward", &avg_voxelize_forward);
  //m.def("avg_voxelize_backward", &avg_voxelize_backward);
}
