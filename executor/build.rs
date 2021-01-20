fn main() {
    println!("cargo:rustc-link-search={}", "../custom_op/build/");
    println!("cargo:rustc-link-lib=dylib={}", "test_op");
}

