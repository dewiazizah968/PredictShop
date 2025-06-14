import pkg_resources

used_libs = [
    "streamlit",
    "pandas",
    "numpy",
    "joblib",
    "Pillow",     # PIL = Pillow
    "base64",     # built-in
    "io",         # built-in
    "random",     # built-in
    "os",         # built-in
    "time",       # built-in
    "re",         # built-in
]

external_libs = ["streamlit", "pandas", "numpy", "joblib", "Pillow"]

with open("requirements.txt", "w") as f:
    for lib in external_libs:
        try:
            version = pkg_resources.get_distribution(lib).version
            f.write(f"{lib}=={version}\n")
        except pkg_resources.DistributionNotFound:
            print(f"{lib} tidak ditemukan di environment")
