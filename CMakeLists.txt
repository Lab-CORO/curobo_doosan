cmake_minimum_required(VERSION 3.0.2)
project(string_to_float64_multiarray)

find_package(catkin REQUIRED COMPONENTS
  roscpp
  std_msgs
)

catkin_package()

include_directories(
  ${catkin_INCLUDE_DIRS}
)

add_executable(string_to_float64_multiarray_node src/string_to_float64_multiarray.cpp)
add_executable(measure_latency_node src/measure_latency.cpp)

target_link_libraries(string_to_float64_multiarray_node
  ${catkin_LIBRARIES}
)

target_link_libraries(measure_latency_node
  ${catkin_LIBRARIES}
)
