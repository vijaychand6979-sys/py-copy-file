def copy_file(command: str) -> None:
    if len(command.split()) != 3:
        return

    cmd, file_in, file_out = command.split()

    if file_in != file_out and cmd == "cp":
        try:
            with (
                open(file_in, "r") as in_file,
                open(file_out, "w") as out_file
            ):
                out_file.writelines(in_file.readlines())
        except FileNotFoundError as e:
            print(e)
