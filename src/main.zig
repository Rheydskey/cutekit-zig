const other_file = @import("./other.zig");

export fn main() usize {
    _ = other_file.aa() catch {
        return 0;
    };

    return 0;
}
