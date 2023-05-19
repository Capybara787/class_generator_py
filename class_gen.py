def super_class_gen(class_name, class_attribs): #class_name -> str, class_attribs -> list
    """
        Generates a class with the given name, attributes, and methods.

        Args:
            class_name (str): The name of the class.
            attributes (list): A list of attribute names.

        Returns:
            txt file: The generated class.
        """

    with open("result.py", "w") as f:
        f.write(f"class {class_name}:\n")

        #init statement
        init_str = "self"
        for i in range(len(class_attribs)):
            init_str += f", {class_attribs[i]}"
        print(class_attribs)

        f.write(f"\tdef __init__({init_str}): \n")
        for i in range(len(class_attribs)):
            f.write(f"\t\tself.{class_attribs[i]} = {class_attribs[i]}\n")

        # setter getter
        for i in range(len(class_attribs)):
            f.write(f"\tdef get_{class_attribs[i]}(self): \n")
            f.write(f"\t\treturn self.{class_attribs[i]}\n")
            f.write(f"\tdef set_{class_attribs[i]}(self, {class_attribs[i]}):\n")
            f.write(f"\t\tself.{class_attribs[i]} = {class_attribs[i]}\n")
        # str method
#       f.write(f"\tdef __str__(self): \n")
#       f.write(f"\t\t return f'{init_str}'")

#super_class_gen("Book", ["title", "author", "publisher"])
#super_class_gen("Pet", ["name", "animal_type","age"])
#super_class_gen("Car", ["year_model", "make", "speed"])

eman = input("What is the name of your class?\n")
sbirtta = []
inp = 0
while inp != "-1":
    inp = input("Enter name of attributes: (enter -1 to end) ")
    sbirtta.append(inp)
sbirtta.pop(-1)
super_class_gen(eman, sbirtta)