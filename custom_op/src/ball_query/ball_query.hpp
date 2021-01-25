#ifndef _BALL_QUERY_HPP
#define _BALL_QUERY_HPP

#include <torch/script.h>

at::Tensor ball_query_forward(at::Tensor centers_coords,
                              at::Tensor points_coords, const double radius,
                              const int64_t num_neighbors);

#endif
