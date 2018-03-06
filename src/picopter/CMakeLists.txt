cmake_minimum_required(VERSION 2.8.3)
project(picopter)

set(CMAKE_CXX_FLAGS "-std=c++11 -Ofast")

find_package(catkin REQUIRED COMPONENTS
  cv_bridge
  image_transport
  sensor_msgs
  std_msgs
  roscpp
  rospy
  apriltags
)

find_package(OpenCV REQUIRED)

catkin_package(
  INCLUDE_DIRS include
)

include_directories(
  include
  ${Eigen_INCLUDE_DIRS}
  ${OpenCV_INCLUDE_DIRS}
  ${catkin_INCLUDE_DIRS}
)

set(${PROJECT_NAME}_SOURCES
  src/tag_detector.cpp
  src/nodes/tag_detector_node.cpp
)
add_executable(tag_detector ${${PROJECT_NAME}_SOURCES})

target_link_libraries(tag_detector
  ${Eigen_LIBRARIES}
  ${OpenCV_LIBRARIES}
  ${catkin_LIBRARIES}
)
