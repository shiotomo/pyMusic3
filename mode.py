class Mode:
    def selectMode(self):
        print("--- mode ---")
        print("loop")
        print("single")
        print("exit or q")
        print("------------")

        intmode = input("=> ")

        if intmode in {"q", "exit"}:
            exit()

        if intmode in {"loop", "single"}:
            return intmode

        return "EOF"
