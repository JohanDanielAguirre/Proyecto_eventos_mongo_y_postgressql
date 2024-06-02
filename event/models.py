from django.db import models

"""---------------------Modelos de Mongo-------------------"""


class User(models.Model):
    """
    Modelo para representar los usuarios

    Atributos:
        id (IntegerField): Identificador único del usuario.
        username (CharField): Nombre de usuario.
        fullName (CharField): Nombre descriptivo del usuario.
        relationship (CharField): relación del usuario.
        email (CharField): correo electronico del usuario.
        city (CharField): ciudad del usuario.
    """

    id = models.AutoField(
        primary_key=True
    )

    username = models.CharField(
        max_length=120
    )

    fullName = models.CharField(
        max_length=240
    )

    relationship = models.CharField(
        max_length=120
    )

    email = models.EmailField(
        max_length=120
    )

    city = models.ForeignKey(
        City,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.username


class Faculty(models.Model):
    """
    Modelo para representar las facultades.

    Atributos:
        id (IntegerField): Identificador único de la facultad.
        name (CharField): Nombre descriptivo de la facultad.
    """

    id = models.AutoField(
        primary_key=True
    )

    name = models.CharField(
        max_length=255,
    )

    def __str__(self):
        return self.nombre


class Event(models.Model):
    """
    Modelo para representar los eventos

    Atributos:
        id (IntegerField): Identificador único del evento.
        title (CharField): titulo descriptivo del evento.
        description (CharField): descripción del evento.
        categories (CharField): categorias del evento.
        date (CharField): fecha de realización del evento.
        location (CharField): ubicación del evento.
    """

    id = models.AutoField(
        primary_key=True
    )

    title = models.CharField(
        max_length=255,
    )

    description = models.CharField(
        max_length=512,
    )

    categories = models.ManyToManyField(Category)

    date = models.DateTimeField()

    location = models.ForeignKey(
        Location,
        on_delete=models.CASCADE,
    )
    organizingFaculties = models.ManyToManyField(
        Faculty,
        related_name='organizing_faculties'
    )

    organizingPrograms = models.ManyToManyField(
        Programa,
        related_name='organizing_programs'
    )

    speakers = models.ManyToManyField(
        User,
        related_name='speakers'
    )

    attendees = models.ManyToManyField(
        User,
        related_name='attendees'
    )

    comments = models.ManyToManyField(
        Comment,
        related_name='comments'
    )

    def __str__(self):
        return self.title


class Program(models.Model):
    """
    Modelo para representar los programas académicos.

    Atributos:
        id (IntegerField): Identificador único del programa.
        name (CharField): Nombre descriptivo del programa.
        facultyId (IntegerField): Identificador único de la facultad a la que pertenece.
    """

    id = models.AutoField(
        primary_key=True
    )

    name = models.CharField(
        max_length=255,
    )

    facultyId = models.ForeignKey(
        'Facultad', on_delete=models.CASCADE
    )


""""------------------------Modelos de Oracle-------------------------------------------"""


class Country(models.Model):
    """
    Modelo para representar los países.

    Atributos:
        id (AutoField): Identificador único del país.
        name (CharField): Nombre del país.
    """

    id = models.AutoField(
        primary_key=True
    )

    name = models.CharField(
        max_length=20
    )


class Department(models.Model):
    """
    Modelo para representar los departamentos.

    Atributos:
        id (AutoField): Identificador único del departamento.
        name (CharField): Nombre del departamento.
        countryId (ForeignKey): Referencia al país al que pertenece el departamento.
    """

    id = models.AutoField(
        primary_key=True
    )

    name = models.CharField(
        max_length=20
    )

    countryId = models.ForeignKey(
        Country,
        on_delete=models.CASCADE
    )


class City(models.Model):
    """
    Modelo para representar las ciudades.

    Atributos:
        id (AutoField): Identificador único de la ciudad.
        name (CharField): Nombre de la ciudad.
        dptId (ForeignKey): Referencia al departamento al que pertenece la ciudad.
    """

    id = models.AutoField(
        primary_key=True
    )

    name = models.CharField(
        max_length=20
    )

    dptId = models.ForeignKey(
        Department,
        on_delete=models.CASCADE
    )


class Location(models.Model):
    """
    Modelo para representar las sedes.

    Atributos:
        id (AutoField): Identificador único de la sede.
        name (CharField): Nombre de la sede.
        cityId (ForeignKey): Referencia a la ciudad donde se encuentra la sede.
    """

    id = models.AutoField(
        primary_key=True
    )

    name = models.CharField(
        max_length=20
    )

    cityId = models.ForeignKey(
        City,
        on_delete=models.CASCADE
    )


class ContractType(models.Model):
    """
    Modelo para representar los tipos de contratación.

    Atributos:
        name (CharField): Nombre del tipo de contratación.
    """

    name = models.CharField(
        max_length=30,
        primary_key=True
    )


class EmployeeType(models.Model):
    """
    Modelo para representar los tipos de empleado.

    Atributos:
        name (CharField): Nombre del tipo de empleado.
    """

    name = models.CharField(
        max_length=30,
        primary_key=True
    )


class Faculties(models.Model):
    """
    Modelo para representar las facultades.

    Atributos:
        id (AutoField): Identificador único de la facultad.
        name (CharField): Nombre de la facultad.
        location (CharField): Ubicación de la facultad.
        phoneNumber (CharField): Número de teléfono de la facultad.
        deanId (CharField): Identificador del decano de la facultad.
    """

    id = models.AutoField(
        primary_key=True
    )

    name = models.CharField(
        max_length=30
    )

    location = models.CharField(
        max_length=15
    )

    phoneNumber = models.CharField(
        max_length=15
    )

    deanId = models.CharField(
        max_length=15
    )


class Employee(models.Model):
    """
    Modelo para representar los empleados.

    Atributos:
        id (AutoField): Identificador único del empleado.
        name (CharField): Nombre del empleado.
        lastName (CharField): Apellido del empleado.
        email (CharField): Correo electrónico del empleado.
        contractType (ForeignKey): Tipo de contratación del empleado.
        employeeType (ForeignKey): Tipo de empleado.
        facultyId (ForeignKey): Facultad a la que pertenece el empleado.
        locationId (ForeignKey): Ubicación del empleado.
        birthPlace (ForeignKey): Lugar de nacimiento del empleado.
    """

    id = models.AutoField(
        primary_key=True
    )

    name = models.CharField(
        max_length=30
    )

    lastName = models.CharField(
        max_length=30
    )

    email = models.CharField(
        max_length=40
    )

    contractType = models.ForeignKey(
        ContractType,
        on_delete=models.CASCADE
    )

    employeeType = models.ForeignKey(
        EmployeeType,
        on_delete=models.CASCADE
    )

    facultyId = models.ForeignKey(
        Faculties,
        on_delete=models.CASCADE
    )

    locationId = models.ForeignKey(
        Location,
        on_delete=models.CASCADE
    )

    birthPlace = models.ForeignKey(
        City,
        on_delete=models.CASCADE
    )


class Area(models.Model):
    """
    Modelo para representar las áreas.

    Atributos:
        id (AutoField): Identificador único de la área.
        name (CharField): Nombre de la área.
        facultyId (ForeignKey): Facultad a la que pertenece la área.
        coordinatorId (ForeignKey): Coordinador de la área.
    """

    id = models.AutoField(
        primary_key=True
    )

    name = models.CharField(
        max_length=40
    )

    facultyId = models.ForeignKey(
        Faculties,
        on_delete=models.CASCADE
    )

    coordinatorId = models.ForeignKey(
        Employee,
        on_delete=models.CASCADE
    )


class Programas(models.Model):
    """
    Modelo para representar los programas académicos.

    Atributos:
        id (AutoField): Identificador único del programa.
        nam (CharField): Nombre del programa.
        areaId (ForeignKey): Área a la que pertenece el programa.
    """

    id = models.AutoField(
        primary_key=True
    )

    nam = models.CharField(
        max_length=40
    )

    areaId = models.ForeignKey(
        Area,
        on_delete=models.CASCADE
    )
