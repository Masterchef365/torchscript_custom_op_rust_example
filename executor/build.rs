fn main() {
    let mut current_dir = std::env::current_dir().unwrap();
    current_dir.pop();
    current_dir.push("custom_op");
    println!("cargo:rustc-link-search={}", current_dir.clone().into_os_string().into_string().unwrap());
    current_dir.push("build_tmp");
    current_dir.push("Release");
    current_dir.push("src");
    current_dir.push("ball_query");
    println!("cargo:rustc-link-search={}", current_dir.into_os_string().into_string().unwrap());
    println!("cargo:rustc-link-lib={}", "_pvcnn_backend");
}