from pydantic import BaseModel


class Multiplication(BaseModel):
    """
    Instantiate a multiplication operation.
    Numbers will be multiplied by the given multiplier.

    :param multiplier: The multiplier.
    :type multiplier: int
    """

    multiplier: int

    def multiply(self, number: int) -> int:
        """
        Multiply a given number by the multiplier.

        :param number: The number to multiply.
        :type number: int

        :return: The result of the multiplication.
        :rtype: int
        """

        return number * self.multiplier
