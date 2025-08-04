import kociemba

# Face names
face_names = ['U', 'R', 'F', 'D', 'L', 'B']

# Display cube in notation form
def display_cube_notation(cube_str):
    print("\nCube Notation (Faces - U, R, F, D, L, B):")
    for i, face in zip(range(0, 54, 9), face_names):
        print(face + ':', cube_str[i:i+9])

# Display cube visually in 2D ASCII layout
def display_cube_visual(cube_str):
    print("\n🧩 Visual Representation of the Cube:\n")

    def get_face(face):
        start = face_names.index(face) * 9
        return cube_str[start:start+9]

    def format_face(face):
        return [face[i:i+3] for i in range(0, 9, 3)]

    u, r, f, d, l, b = map(get_face, face_names)
    u_rows = format_face(u)
    r_rows = format_face(r)
    f_rows = format_face(f)
    d_rows = format_face(d)
    l_rows = format_face(l)
    b_rows = format_face(b)

    for row in u_rows:
        print("      ", " ".join(row))
    for l_row, f_row, r_row, b_row in zip(format_face(l), f_rows, format_face(r), format_face(b)):
        print(" ".join(l_row), " ", " ".join(f_row), " ", " ".join(r_row), " ", " ".join(b_row))
    for row in d_rows:
        print("      ", " ".join(row))

# Solve cube and print steps
def solve_cube(cube_str):
    try:
        print("\nSolving Rubik’s Cube...")
        solution = kociemba.solve(cube_str)
        steps = solution.split()
        print("\n✅ Solution Steps:")
        for i, move in enumerate(steps, 1):
            print(f"Step {i}: {move}")
        print("\n🎉 Cube Solved in", len(steps), "moves!")
    except Exception as e:
        print("\n❌ Error: Invalid Cube String\n", str(e))

# Cube input options
def simulate_input():
    print("Choose Input Method:")
    print("1. Use Example Solved Cube")
    print("2. Enter Your Own Cube (54-letter string)")
    choice = input("Enter choice (1 or 2): ")

    if choice == '1':
        return (
            'UUUUUUUUU'  # U
            'RRRRRRRRR'  # R
            'FFFFFFFFF'  # F
            'DDDDDDDDD'  # D
            'LLLLLLLLL'  # L
            'BBBBBBBBB'  # B
        )
    elif choice == '2':
        print("\nEnter cube string in this order:")
        print("U (up), R (right), F (front), D (down), L (left), B (back)")
        print("Each face must have 9 letters using only: U, R, F, D, L, B")
        cube_str = input("Paste your cube string (54 letters): ").strip().upper()
        if len(cube_str) != 54 or not all(c in "URFDLB" for c in cube_str):
            print("Invalid input! Must be 54 letters using U, R, F, D, L, B.")
            return simulate_input()
        return cube_str
    else:
        print("Invalid choice. Try again.")
        return simulate_input()

if _name_ == "_main_":
    print("🧠 Rubik's Cube Solver (Simulated Input)")
    cube_string = simulate_input()
    display_cube_notation(cube_string)
    display_cube_visual(cube_string)
    solve_cube(cube_string)
