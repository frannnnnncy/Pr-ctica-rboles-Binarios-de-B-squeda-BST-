#pragma once
#include <string>

struct Estudiante{
    int codigo;
    std::string nombre;
    float ppa;
};

class ArbolAcademico{
public:
    void insertar(Estudiante e);
    Estudiante* buscar(int codigo);
};
