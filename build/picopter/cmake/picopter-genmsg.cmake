# generated from genmsg/cmake/pkg-genmsg.cmake.em

message(STATUS "picopter: 4 messages, 0 services")

set(MSG_I_FLAGS "-Ipicopter:/home/pi/picopter/src/picopter/msg;-Istd_msgs:/opt/ros/kinetic/share/std_msgs/cmake/../msg")

# Find all generators
find_package(gencpp REQUIRED)
find_package(geneus REQUIRED)
find_package(genlisp REQUIRED)
find_package(gennodejs REQUIRED)
find_package(genpy REQUIRED)

add_custom_target(picopter_generate_messages ALL)

# verify that message/service dependencies have not changed since configure



get_filename_component(_filename "/home/pi/picopter/src/picopter/msg/SpinRates.msg" NAME_WE)
add_custom_target(_picopter_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "picopter" "/home/pi/picopter/src/picopter/msg/SpinRates.msg" ""
)

get_filename_component(_filename "/home/pi/picopter/src/picopter/msg/IMUOutput.msg" NAME_WE)
add_custom_target(_picopter_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "picopter" "/home/pi/picopter/src/picopter/msg/IMUOutput.msg" ""
)

get_filename_component(_filename "/home/pi/picopter/src/picopter/msg/Interface.msg" NAME_WE)
add_custom_target(_picopter_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "picopter" "/home/pi/picopter/src/picopter/msg/Interface.msg" ""
)

get_filename_component(_filename "/home/pi/picopter/src/picopter/msg/CamMeasurement.msg" NAME_WE)
add_custom_target(_picopter_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "picopter" "/home/pi/picopter/src/picopter/msg/CamMeasurement.msg" ""
)

#
#  langs = gencpp;geneus;genlisp;gennodejs;genpy
#

### Section generating for lang: gencpp
### Generating Messages
_generate_msg_cpp(picopter
  "/home/pi/picopter/src/picopter/msg/SpinRates.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/picopter
)
_generate_msg_cpp(picopter
  "/home/pi/picopter/src/picopter/msg/IMUOutput.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/picopter
)
_generate_msg_cpp(picopter
  "/home/pi/picopter/src/picopter/msg/Interface.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/picopter
)
_generate_msg_cpp(picopter
  "/home/pi/picopter/src/picopter/msg/CamMeasurement.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/picopter
)

### Generating Services

### Generating Module File
_generate_module_cpp(picopter
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/picopter
  "${ALL_GEN_OUTPUT_FILES_cpp}"
)

add_custom_target(picopter_generate_messages_cpp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_cpp}
)
add_dependencies(picopter_generate_messages picopter_generate_messages_cpp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/pi/picopter/src/picopter/msg/SpinRates.msg" NAME_WE)
add_dependencies(picopter_generate_messages_cpp _picopter_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/pi/picopter/src/picopter/msg/IMUOutput.msg" NAME_WE)
add_dependencies(picopter_generate_messages_cpp _picopter_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/pi/picopter/src/picopter/msg/Interface.msg" NAME_WE)
add_dependencies(picopter_generate_messages_cpp _picopter_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/pi/picopter/src/picopter/msg/CamMeasurement.msg" NAME_WE)
add_dependencies(picopter_generate_messages_cpp _picopter_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(picopter_gencpp)
add_dependencies(picopter_gencpp picopter_generate_messages_cpp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS picopter_generate_messages_cpp)

### Section generating for lang: geneus
### Generating Messages
_generate_msg_eus(picopter
  "/home/pi/picopter/src/picopter/msg/SpinRates.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/picopter
)
_generate_msg_eus(picopter
  "/home/pi/picopter/src/picopter/msg/IMUOutput.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/picopter
)
_generate_msg_eus(picopter
  "/home/pi/picopter/src/picopter/msg/Interface.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/picopter
)
_generate_msg_eus(picopter
  "/home/pi/picopter/src/picopter/msg/CamMeasurement.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/picopter
)

### Generating Services

### Generating Module File
_generate_module_eus(picopter
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/picopter
  "${ALL_GEN_OUTPUT_FILES_eus}"
)

add_custom_target(picopter_generate_messages_eus
  DEPENDS ${ALL_GEN_OUTPUT_FILES_eus}
)
add_dependencies(picopter_generate_messages picopter_generate_messages_eus)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/pi/picopter/src/picopter/msg/SpinRates.msg" NAME_WE)
add_dependencies(picopter_generate_messages_eus _picopter_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/pi/picopter/src/picopter/msg/IMUOutput.msg" NAME_WE)
add_dependencies(picopter_generate_messages_eus _picopter_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/pi/picopter/src/picopter/msg/Interface.msg" NAME_WE)
add_dependencies(picopter_generate_messages_eus _picopter_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/pi/picopter/src/picopter/msg/CamMeasurement.msg" NAME_WE)
add_dependencies(picopter_generate_messages_eus _picopter_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(picopter_geneus)
add_dependencies(picopter_geneus picopter_generate_messages_eus)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS picopter_generate_messages_eus)

### Section generating for lang: genlisp
### Generating Messages
_generate_msg_lisp(picopter
  "/home/pi/picopter/src/picopter/msg/SpinRates.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/picopter
)
_generate_msg_lisp(picopter
  "/home/pi/picopter/src/picopter/msg/IMUOutput.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/picopter
)
_generate_msg_lisp(picopter
  "/home/pi/picopter/src/picopter/msg/Interface.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/picopter
)
_generate_msg_lisp(picopter
  "/home/pi/picopter/src/picopter/msg/CamMeasurement.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/picopter
)

### Generating Services

### Generating Module File
_generate_module_lisp(picopter
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/picopter
  "${ALL_GEN_OUTPUT_FILES_lisp}"
)

add_custom_target(picopter_generate_messages_lisp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_lisp}
)
add_dependencies(picopter_generate_messages picopter_generate_messages_lisp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/pi/picopter/src/picopter/msg/SpinRates.msg" NAME_WE)
add_dependencies(picopter_generate_messages_lisp _picopter_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/pi/picopter/src/picopter/msg/IMUOutput.msg" NAME_WE)
add_dependencies(picopter_generate_messages_lisp _picopter_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/pi/picopter/src/picopter/msg/Interface.msg" NAME_WE)
add_dependencies(picopter_generate_messages_lisp _picopter_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/pi/picopter/src/picopter/msg/CamMeasurement.msg" NAME_WE)
add_dependencies(picopter_generate_messages_lisp _picopter_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(picopter_genlisp)
add_dependencies(picopter_genlisp picopter_generate_messages_lisp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS picopter_generate_messages_lisp)

### Section generating for lang: gennodejs
### Generating Messages
_generate_msg_nodejs(picopter
  "/home/pi/picopter/src/picopter/msg/SpinRates.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/picopter
)
_generate_msg_nodejs(picopter
  "/home/pi/picopter/src/picopter/msg/IMUOutput.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/picopter
)
_generate_msg_nodejs(picopter
  "/home/pi/picopter/src/picopter/msg/Interface.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/picopter
)
_generate_msg_nodejs(picopter
  "/home/pi/picopter/src/picopter/msg/CamMeasurement.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/picopter
)

### Generating Services

### Generating Module File
_generate_module_nodejs(picopter
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/picopter
  "${ALL_GEN_OUTPUT_FILES_nodejs}"
)

add_custom_target(picopter_generate_messages_nodejs
  DEPENDS ${ALL_GEN_OUTPUT_FILES_nodejs}
)
add_dependencies(picopter_generate_messages picopter_generate_messages_nodejs)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/pi/picopter/src/picopter/msg/SpinRates.msg" NAME_WE)
add_dependencies(picopter_generate_messages_nodejs _picopter_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/pi/picopter/src/picopter/msg/IMUOutput.msg" NAME_WE)
add_dependencies(picopter_generate_messages_nodejs _picopter_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/pi/picopter/src/picopter/msg/Interface.msg" NAME_WE)
add_dependencies(picopter_generate_messages_nodejs _picopter_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/pi/picopter/src/picopter/msg/CamMeasurement.msg" NAME_WE)
add_dependencies(picopter_generate_messages_nodejs _picopter_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(picopter_gennodejs)
add_dependencies(picopter_gennodejs picopter_generate_messages_nodejs)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS picopter_generate_messages_nodejs)

### Section generating for lang: genpy
### Generating Messages
_generate_msg_py(picopter
  "/home/pi/picopter/src/picopter/msg/SpinRates.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/picopter
)
_generate_msg_py(picopter
  "/home/pi/picopter/src/picopter/msg/IMUOutput.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/picopter
)
_generate_msg_py(picopter
  "/home/pi/picopter/src/picopter/msg/Interface.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/picopter
)
_generate_msg_py(picopter
  "/home/pi/picopter/src/picopter/msg/CamMeasurement.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/picopter
)

### Generating Services

### Generating Module File
_generate_module_py(picopter
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/picopter
  "${ALL_GEN_OUTPUT_FILES_py}"
)

add_custom_target(picopter_generate_messages_py
  DEPENDS ${ALL_GEN_OUTPUT_FILES_py}
)
add_dependencies(picopter_generate_messages picopter_generate_messages_py)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/pi/picopter/src/picopter/msg/SpinRates.msg" NAME_WE)
add_dependencies(picopter_generate_messages_py _picopter_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/pi/picopter/src/picopter/msg/IMUOutput.msg" NAME_WE)
add_dependencies(picopter_generate_messages_py _picopter_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/pi/picopter/src/picopter/msg/Interface.msg" NAME_WE)
add_dependencies(picopter_generate_messages_py _picopter_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/pi/picopter/src/picopter/msg/CamMeasurement.msg" NAME_WE)
add_dependencies(picopter_generate_messages_py _picopter_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(picopter_genpy)
add_dependencies(picopter_genpy picopter_generate_messages_py)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS picopter_generate_messages_py)



if(gencpp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/picopter)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/picopter
    DESTINATION ${gencpp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_cpp)
  add_dependencies(picopter_generate_messages_cpp std_msgs_generate_messages_cpp)
endif()

if(geneus_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/picopter)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/picopter
    DESTINATION ${geneus_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_eus)
  add_dependencies(picopter_generate_messages_eus std_msgs_generate_messages_eus)
endif()

if(genlisp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/picopter)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/picopter
    DESTINATION ${genlisp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_lisp)
  add_dependencies(picopter_generate_messages_lisp std_msgs_generate_messages_lisp)
endif()

if(gennodejs_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/picopter)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/picopter
    DESTINATION ${gennodejs_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_nodejs)
  add_dependencies(picopter_generate_messages_nodejs std_msgs_generate_messages_nodejs)
endif()

if(genpy_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/picopter)
  install(CODE "execute_process(COMMAND \"/usr/bin/python\" -m compileall \"${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/picopter\")")
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/picopter
    DESTINATION ${genpy_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_py)
  add_dependencies(picopter_generate_messages_py std_msgs_generate_messages_py)
endif()
