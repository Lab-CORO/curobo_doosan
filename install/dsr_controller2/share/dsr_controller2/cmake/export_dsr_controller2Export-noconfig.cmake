#----------------------------------------------------------------
# Generated CMake target import file.
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "dsr_controller2::dsr_controller2" for configuration ""
set_property(TARGET dsr_controller2::dsr_controller2 APPEND PROPERTY IMPORTED_CONFIGURATIONS NOCONFIG)
set_target_properties(dsr_controller2::dsr_controller2 PROPERTIES
  IMPORTED_LOCATION_NOCONFIG "${_IMPORT_PREFIX}/lib/libdsr_controller2.so"
  IMPORTED_SONAME_NOCONFIG "libdsr_controller2.so"
  )

list(APPEND _cmake_import_check_targets dsr_controller2::dsr_controller2 )
list(APPEND _cmake_import_check_files_for_dsr_controller2::dsr_controller2 "${_IMPORT_PREFIX}/lib/libdsr_controller2.so" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)