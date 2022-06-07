project(Dimension3D) #LANGUAGE CXX)
set(CXX_STANDARD 20)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

# Sources
file(GLOB_RECURSE SOURCES sources/*.cpp)
file(GLOB_RECURSE HEADERS includes/*.hpp includes/*.h sources/*.hpp sources/*.h)

add_library(dimension3d STATIC ${SOURCES})

target_include_directories(dimension3d PUBLIC includes/ includes/dim sources/ ${CONAN_INCLUDE_DIRS})
target_link_libraries(dimension3d PUBLIC ${CONAN_LIBS})

