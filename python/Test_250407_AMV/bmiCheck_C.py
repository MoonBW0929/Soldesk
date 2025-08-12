# HomeController

from bmiCheck_V import ConsoleScreen
from Doctor_M import Doctor


if __name__ == "__main__":
    guest = ConsoleScreen.get_info()
    Doctor.bmi_check(guest)
    ConsoleScreen.printResult(guest)