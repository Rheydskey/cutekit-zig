from cutekit.rules import Rule, append

append(
    Rule(
        "zig",
        ["*.zig"],
        "*.o.o",
        "build-obj $flags -femit-bin=$out $in",
        [
            "-fPIE",
            "-fcompiler-rt",
        ],
    )
)
