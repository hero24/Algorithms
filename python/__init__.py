"""
Many of life's failures are people who did not realize 
how close they were to success when they gave up.
-Thomas A. Edison
"""

def _get_dirs():
    from os import walk
    exclude = ["dist",
               "__pycache__",
               "build",
               "lib",
               "algorithms"
    ]
    dirs = {"hero24/algorithms" : "."}
    for _, d1, _ in walk("."):
        for d in d1:
            if d in exclude:
                continue
            dirs["hero24/algorithms/"+d] = d
    print(dirs)
    return dirs

if __name__ == "__main__":
    from distutils.core import setup, Extension
    from sys import argv

    argv += ['install']
    dirs = _get_dirs()
    packs = [k for k in dirs]
    
    setup(name="algorithms",
      version="0.1",
      description="Python implementations of various algorithms",
      author="hero24",
      package_dir=dirs,
      packages=packs,
            ext_modules=[Extension("hero24/algorithms/capi/rabin_karp", ["capi/rk.c"]),
              Extension("hero24/algorithms/capi/boyer_moore", ["capi/bm.c"]),
              Extension("hero24/algorithms/capi/knuth_morris_pratt", ["capi/kmp.c"]),
              Extension("hero24/algorithms/capi/hashing", ["capi/hashing.c"])]
      )
