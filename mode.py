class Mode:
    def selectMode(self):
        print("--- mode ---")
        print("loop")
        print("single")
        print("exit or q")
        print("------------")

        modeFlag = input("=> ")

        if modeFlag in {"q", "exit"}:
            exit()

        if modeFlag in {"loop", "single"}:
            return modeFlag

        return "EOF"
