fn main() {
    #[cfg(target_os = "windows")]
    {
        let mut current_dir = std::env::current_dir().unwrap();
        current_dir.pop();
        current_dir.push("custom_op");
        current_dir.push("build");
        current_dir.push("Release");
        println!("cargo:rustc-link-search={}", current_dir.into_os_string().into_string().unwrap());
    }

    #[cfg(target_os = "linux")]
    println!("cargo:rustc-link-search={}", "../custom_op/build/");

    println!("cargo:rustc-link-lib=dylib={}", "test_op");
}