#/bin/sh
make clean
make -j8 CXXFLAGS="-target x86_64-apple-macos10.12 -std=c++11 -O3" LDFLAGS="-target x86_64-apple-macos10.12 -Lbuild -ltundra" CFLAGS="-target x86_64-apple-macos10.12 -O3"
rm -rfv x86_bins
mkdir x86_bins
cp build/tundra2 build/t2-inspect build/t2-lua build/t2-unittest x86_bins
make clean
make -j8 CXXFLAGS="-target arm64-apple-macos11 -std=c++11 -O3" LDFLAGS="-target arm64-apple-macos11 -Lbuild -ltundra" CFLAGS="-target arm64-apple-macos11 -O3"
lipo -create -output build/tundra2 x86_bins/tundra2 build/tundra2
lipo -create -output build/t2-lua x86_bins/t2-lua build/t2-lua
lipo -create -output build/t2-unittest x86_bins/t2-unittest build/t2-unittest