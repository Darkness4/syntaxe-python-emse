# -*- coding: utf-8 -*-
"""Language Tour: Class"""
import abc


# Class
class Complex:
    """A class supposed to be a complex, but lost his meaning of life.

    Parameters
    ----------
    realpart : float
        Partie réelle
    imagpart : float
        Partie imaginaire

    Attributes
    ----------
    public_property : str
        Propriété publique, accessible partout
    _protected_property : str
        Propriété protégé, accessible pour ses subclasses
    __encrypted_password : str
        Propriété privée, accessible uniquement sur soi
    """
    public_property = "Hey i'm public"  # Read and write everywhere
    _protected_property = "Hey i'm protected"  # Read and write from subclass
    __private_property = "Hey i'm private"  # Read and write self
    __get_only_m8 = "README"  # Read only self
    __encrypted_password = "setmein"  # Read, Write throught getter/setter self

    def __init__(self, realpart: float, imagpart: float):  # Constructor
        if realpart == 0:
            raise ValueError("This is retarded but 0 is not allowed")
        self.realpart = realpart  # instance var à initialiser
        self.imagpart = imagpart

    def method(self):
        """do"""

    # Getter : Read only use case
    # getter
    @property
    def readme(self) -> str:
        """doc"""
        return self.__get_only_m8

    # Getter, Setter: Calculus use case
    # getter
    @property
    def password(self) -> str:
        """doc"""
        print("Decrypting...")
        return self.__encrypted_password

    # setter
    @password.setter
    def password(self, value: str) -> str:
        """doc"""
        print("Encrypting... Get some salt...")
        self.__encrypted_password = value

    @staticmethod
    def static_func(arg: int) -> int:  # static
        """doc"""
        print(Complex.__private_property)
        return arg

    @classmethod
    def named_contructor(
            cls,
            complex_var: complex,
    ):  # Constructor with a name
        """doc"""
        return cls(complex_var.real, complex_var.imag)

    @abc.abstractmethod
    def abstract_func(self, arg: int):
        """doc"""
        raise NotImplementedError


class HeritFrom(Complex):
    """Empty caus' don't want to fill"""

    def abstract_func(self, arg: int):
        """I'm an implemented function."""
        return arg


if __name__ == "__main__":
    complex_class = Complex(1, 2)
    complex_class = Complex.named_contructor(complex(1, 2))

    print(complex_class.public_property)
    print(complex_class.realpart)
    print(complex_class.imagpart)
    complex_class.password = "my password"
    print(complex_class.password)
    print(complex_class.readme)
    try:
        complex_class.abstract_func(10)  # => NotImplementedError
    except NotImplementedError as error:
        print(error)
    print(Complex.static_func(100))

    complex_class2 = HeritFrom(1, 2)
    print(complex_class2.abstract_func(10))  # => 10
