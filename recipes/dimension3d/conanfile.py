import os
from conans import ConanFile, CMake, tools
import conan

class Dimension3DConan(ConanFile):
    name = "dimension3d"
    version = "0.1"
    generators = "cmake"
    repo_url = "https://github.com/angeluriot/Dimension3D.git"
    repo_folder = "Dimension3D"
    exports_sources = [ "CMakeLists.txt", "conanfile.txt", "patches/*" ]
    def source( self ):
        self.run( "git clone " + self.repo_url )
        conan.tools.files.copy( self, "CMakeLists.txt", src=".", dst=self.repo_folder )
        #conan.tools.files.copy( self, "*.patch", src="./patches", dst="patches")
        print( "Patching... " )
        for patch in self.conan_data.get("patches", {}).get(self.version, []): 
            print( patch )
            print( tools.patch(**patch) )
            with open( patch[ 'patch_file' ], 'r' ) as f: 
                print( f.readlines() )

    def requirements( self ):
        for requirement in self.conan_data[ "requirements" ]:
            print( requirement )
            self.requires( requirement )

    def build( self ): 
        cmake = CMake( self )
        cmake.configure( source_folder = os.path.join( self.folders.source, self.repo_folder ) )
        cmake.build()

    def package(self):
        includes_folder = os.path.join( self.repo_folder, "includes" )
        self.copy("*.hpp", dst="include", src=includes_folder)
        self.copy("*.h", dst="include", src=includes_folder)
        self.copy("*.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.dylib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self)
        self.cpp_info.libs = [ self.name ]
